import uvicorn
from fastapi import FastAPI

from cleam_table import CleanTable
from model import NaiveBayesClassifier
from naive_bayes import NaiveBayesPredictor
from userinterface import UI

path = "C:/Users/User/Downloads/buy_computer_data.csv"
ct = CleanTable(path)

model = NaiveBayesClassifier(ct.table)
pc = NaiveBayesPredictor
app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "hello world"}

@app.get("/{name}")
async def root(name):
    name = name.split(".")
    s_dic = {}
    for i in range(0, len(name) ,2):
        s_dic[name[i]] = name[i+1]
    return {"answer": pc.predict(s_dic, model.model, model.target_variable())}
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)