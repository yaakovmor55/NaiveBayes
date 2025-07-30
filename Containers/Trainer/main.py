import logging
from fastapi import FastAPI
import os

from App.test_model import TestTable
from App.cleam_table import CleanTable
from App.loader import Loader
from App.model import NaiveBayesClassifier



def setup_logging():
    log_dir = os.path.join(os.path.dirname(__file__), "Logs")
    os.makedirs(log_dir, exist_ok=True)
    file_handler = logging.FileHandler(os.path.join(log_dir, "project.log"))
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        handlers=[file_handler, stream_handler]
    )


def load_data():
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # data_dir = os.path.join(base_dir, "data")
    # path = os.path.join(data_dir, "FlavorSense.csv")
    # logger.info(f"Loading CSV file from path: {path}")
    return Loader("data/FlavorSense.csv")


def prepare_model(table):
    cleaned = CleanTable(table)
    logger.info("CleanTable created")
    test = TestTable(cleaned.table)
    test = test.test()
    if test < 85:
        logger.warning("Model accuracy is too low. Server will not start.")
        exit(1)
    model = NaiveBayesClassifier(cleaned.table)
    logger.info("Model created")
    return model


setup_logging()
logger = logging.getLogger(__name__)
logger.info("Starting application")
app = FastAPI()


@app.get("/")
async def root():
    logging.info("Root endpoint called")
    return {"message":"wellcome to the Bayesian model"}

@app.get("/load_and_train")
async def load_and_train():
    file = load_data()
    model = prepare_model(file.table)
    return {"model": model.model, "target": model.target_variable()}








