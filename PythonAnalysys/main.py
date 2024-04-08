from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import tensorflow as tf
# Модель данных для представления товара
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Создание экземпляра FastAPI
app = FastAPI()

# Имитация базы данных с товарами
fake_db = []

# Маршрут для создания нового товара
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    fake_db.append(item)
    return item

# Маршрут для получения всех товаров
@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return fake_db[skip : skip + limit]

# Маршрут для получения конкретного товара по его индексу
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

# Маршрут для обновления информации о товаре
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return item

# Маршрут для удаления товара
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted"}

