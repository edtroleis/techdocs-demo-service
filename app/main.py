from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Demo API", version="0.1.0")


class ItemIn(BaseModel):
    name: str
    quantity: int = 1


class Item(ItemIn):
    id: int


_items: dict[int, Item] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items")
def list_items() -> list[Item]:
    return list(_items.values())


@app.post("/items", status_code=201)
def create_item(data: ItemIn) -> Item:
    item = Item(id=len(_items) + 1, **data.model_dump())
    _items[item.id] = item
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="item not found")
    return _items[item_id]
