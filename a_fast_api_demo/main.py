import uvicorn
from starlette.responses import StreamingResponse
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
def read_root():
    return {"Hello": "World"}


async def slow_numbers():
    with open('./index.html', 'r', encoding='utf-8') as f:
        yield f.read()


@app.get("/items")
def read_item(bvid: str = Query(None), cid: str = Query(None)):
    print(f'{bvid}, {cid}')
    generator = slow_numbers()
    response = StreamingResponse(generator, media_type='text/html')
    return response


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
