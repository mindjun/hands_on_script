import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items")
def read_item(result: dict):
    print(f'get result is {result}')
    import time
    time.sleep(5)
    return {"item_id": "item_id"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
