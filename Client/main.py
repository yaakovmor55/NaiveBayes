from classifier.naive_bayes import NaiveBayesPredictor
from fastapi import FastAPI
import requests

resp = requests.get("http://server:8000/load_and_train")
data = resp.json()
model = data["model"]
target  = data["target"]



app = FastAPI()



@app.get("/{request}")
async def root(request):
    request = request.split(".")
    s_dic = {}
    for i in range(0, len(request), 2):
        s_dic[request[i]] = request[i + 1]
        return {"answer": NaiveBayesPredictor.predict(s_dic, model, target)}



