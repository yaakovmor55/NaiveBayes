import uvicorn
from fastapi import FastAPI

from cleam_table import CleanTable
from model import Model
from naive_bayes import ProbabilityCalculating
from userinterface import UI

path = "C:/Users/User/Downloads/buy_computer_data.csv"
ct = CleanTable(path)

model = Model(ct.table)
pc = ProbabilityCalculating
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
    return {"answer": pc.result(s_dic, model.model, model.target_variable())}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)