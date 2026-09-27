import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/users")
async def question():
    return [
        {"name":"张三","age":22,"id":1},
        {"name":"张四","age":32,"id":2},
        {"name": "张五", "age": 42, "id": 4},
    ]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)