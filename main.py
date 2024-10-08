from fastapi import FastAPI, Query # type: ignore
from pydantic import BaseModel
from typing import Annotated

# from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# GET /items/{item_id} Endpoint 
@app.get("/items/{item_id}")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(item_id: int, 
                      item: Item, 
                      q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# http://localhost:8080
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/")
# async def read_items(item_query: Annotated[str | None, 
#                                   Query(
#                                       title="ABCDfefe",
#                                       description="This is",
#                                       alias="item-query",
#                                       deprecated=True                                 
#                                         )] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if item_query:
#         results.update({"item_query": item_query})
#     return results

# # http://localhost:8080/items/{item_id}?q={q}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# http://localhost:8080/users

# class UserId(int, Enum):
#     Alice = 1
#     Bob = 2
#     Eve = 3

# @app.get("/users/{user_id}")
# async def get_users(user_id: UserId, q: int=10):
#     if user_id is UserId.Alice:
#         return {"user_id": user_id, "user_info": "Alice"}
#     if user_id.value == 2:
#         return {"user_id": user_id, "user_info": "Bob"}
    
#     return{"user_id": user_id, "user_info": ""}

# http://localhost:8080/users/{user_id}

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user(user_id: int, item_id: int, q1: int = 10, q2: int = 1):
#     return {"user_id": user_id,"item_id": item_id, "q1": q1, "q2": q2}

