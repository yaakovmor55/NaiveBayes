import logging
import uvicorn
from fastapi import FastAPI
from App.cleam_table import CleanTable
from App.loader import Loader
from App.model import NaiveBayesClassifier
from App.naive_bayes import NaiveBayesPredictor
import os

# Create the Logs directory if it doesn't exist
os.makedirs("Logs", exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("Logs/project.log"),
        logging.StreamHandler()
    ]
)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

logger = logging.getLogger(__name__)
logger.info("Starting application")

DATA_DIR = os.path.join(BASE_DIR, "data")
path = os.path.join(DATA_DIR, "buy_computer_data.csv")

logger.info(f"Loading CSV file from path: {path}")
file = Loader(path)

ct = CleanTable(file.table)
logger.info("CleanTable created")

model = NaiveBayesClassifier(ct.table)
pc = NaiveBayesPredictor
logger.info("Model created")
app = FastAPI()


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

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
