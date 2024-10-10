from fastapi import FastAPI, Query, Path, HTTPException # type: ignore
from pydantic import BaseModel
from typing import Annotated
from enum import Enum
from decimal import Decimal

app = FastAPI()
# http://localhost:8080/docs


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float| None = None


# 定義一個 Enum 來表示 sort_order 的合法值
class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

@app.get("/")
async def root():
    return {"message": "Hello World"}

# GET /items/{item_id} Endpoint 
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[Decimal, Path(ge=1, le=1000,
                                        description="Item ID must be between 1 and 1000.")], 
    q: Annotated[str | None, Query(description = "Query 'q' must be between 3 and 50 characters.",
                                   min_length=3,
                                   max_length=50)] = None,
    sort_order: SortOrder = SortOrder.asc
):
    results = {"item_id": item_id}
    if q:
        results.update({"description": f"This is a sample item that matches the query {q}"})
    else:
        results.update({"description": "This is a sample item."})
    
    if sort_order:
        results.update({"sort_order": sort_order})
    return results


@app.put("/items/{item_id}")
async def update_item(
                      item_id: Annotated[Decimal, Path(ge=1, le=1000, description="Item ID must be between 1 and 1000.")], 
                      item: Item = None, 
                      q: Annotated[str | None, Query(min_length=3, max_length=50, description="Query 'q' must be between 3 and 50 characters.")] = None
                      ):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result