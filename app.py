from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import dataset


app = FastAPI()


# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  
    allow_methods=["*"],    
    allow_headers=["*"]       
)


# DB Settings
db = dataset.connect("sqlite:///hello.db")
table = db["todo"]


@app.get("/list")
def lists():
  todos = table.find(name="gamma")
  result = []
  for todo in todos:
    result.append(todo)
  print(result)
  return { "todo" : result }


@app.post("/post")
def posts(name: str, todo: str):
  table.insert({"name":name, "todo":todo})
  return { "send": { "name":name, "todo":todo } }

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=5000)
