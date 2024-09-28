from fastapi import FastAPI # type: ignore

app = FastAPI()


# http://localhost:8080
@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://localhost:8080/items/{item_id}?q={q}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# http://localhost:8080/items/{item_id}/reviews