import logging
import uvicorn
from fastapi import FastAPI
import os

from test_model import TestTable
from cleam_table import CleanTable
from loader import Loader
from model import NaiveBayesClassifier
from naive_bayes import NaiveBayesPredictor


def setup_logging():
    os.makedirs("Logs", exist_ok=True)

    file_handler = logging.FileHandler("Logs/project.log")
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        handlers=[file_handler, stream_handler]
    )


def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data")
    path = os.path.join(data_dir, "FlavorSense.csv")
    logger.info(f"Loading CSV file from path: {path}")
    return Loader(path)


def prepare_model(table):
    cleaned = CleanTable(table)
    logger.info("CleanTable created")
    test = TestTable(cleaned.table).test()
    if test < 85:
        logger.warning("Model accuracy is too low. Server will not start.")
        exit(1)
    model = NaiveBayesClassifier(cleaned.table)
    logger.info("Model created")
    return model


setup_logging()
logger = logging.getLogger(__name__)
logger.info("Starting application")

file = load_data()
model = prepare_model(file.table)
pc = NaiveBayesPredictor

app = FastAPI()


@app.get("/")
async def root():
    logging.info("Root endpoint called")
    return {"wellcome to the baysian model"}


@app.get("/{predict}")
async def root(predict):
    logger.info("Root endpoint called")
    if predict == "favicon.ico":
        return {"answer": "favicon.ico ignored"}
    predict = predict.split(".")
    s_dic = {}
    for i in range(0, len(predict), 2):
        s_dic[predict[i]] = predict[i + 1]
    return {"answer": pc.predict(s_dic, model.model, model.target_variable())}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
