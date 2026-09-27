from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="入门程序",description="第一个入门程序",version="1.0.0")


class User(BaseModel):
    name: str
    age: int
    id: int



@app.get("/",summary="首页")
async def root():
    return {"message":"Hello World"}

@app.get("/users",summary="展示所有用户",response_model=List[User])
async def question():
    return [
            User(name="张三",age=32,id=1),
            User(name="张四", age=42, id=2),
            User(name="张五", age=52, id=3),
            User(name="张六", age=62, id=4),
    ]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)