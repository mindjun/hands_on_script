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


@app.get('/instances/{instance_id}')
def instances(instance_id: str = Query(None)):
    from a_fast_api_demo.utils import api_host_settings, api_auth_request
    url = f'{api_host_settings["prod"]}/results/vod/'
    return api_auth_request(url, parm={'instance_id': instance_id})


@app.get('/instances/coverage/{instance_id}')
def coverage_instances(instance_id: str = Query(None)):
    from a_fast_api_demo.utils import api_host_settings, api_auth_request
    url = f'{api_host_settings["prod"]}/results/general/'
    resp = api_auth_request(url, parm={'instance_id': instance_id, 'type': 'coverage'})
    return resp


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8081)
