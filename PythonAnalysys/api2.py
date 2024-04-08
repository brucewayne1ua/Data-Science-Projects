from fastapi import FastAPI

# Создаем экземпляр FastAPI
app = FastAPI()

# Определяем обработчик для корневого URL
@app.get("/")
def read_root():
    return {"message": "Привет, мир!"}
