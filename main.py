from fastapi import FastAPI # type: ignore
from enum import Enum

app = FastAPI()


# http://localhost:8080
@app.get("/")
async def root():
    return {"message": "Hello World"}

# # http://localhost:8080/items/{item_id}?q={q}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# http://localhost:8080/users

class UserId(int, Enum):
    Alice = 1
    Bob = 2
    Eve = 3

@app.get("/users/{user_id}")
async def get_users(user_id: UserId):
    if user_id is UserId.Alice:
        return {"user_id": user_id, "user_info": "Alice"}
    if user_id.value == 2:
        return {"user_id": user_id, "user_info": "Bob"}
    
    return{"user_id": user_id, "user_info": ""}

# http://localhost:8080/users/{user_id}