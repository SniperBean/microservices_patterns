from typing import Optional
from fastapi import FastAPI, Request
from fastapi_opentracing import get_opentracing_span_headers
from fastapi_opentracing.middleware import OpenTracingMiddleware

app = FastAPI()
app.add_middleware(OpenTracingMiddleware)

dummy_list = [
        {
            "id": "1",
            "name": "Jose Miguel"
        },
        {
            "id": "2",
            "name": "Souch Hsu"
        },
        {
            "id": "3",
            "name": "John Cena"
        },
        {
            "id": "4",
            "name": "Takahashi Hitoshi"
        },
        {
            "id": "5",
            "name": "Elon Musk"
        }
    ]


@app.get("/")
async def root():
    carrier = await get_opentracing_span_headers()
    return {'span': carrier}


@app.get("/api/users")
def read_users(request: Request):
    return dummy_list


@app.get("/api/user/{id}")
def read_user(id: int, request: Request):
    return next(item for item in dummy_list if item["id"] == str(id))
