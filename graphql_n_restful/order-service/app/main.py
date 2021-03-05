from typing import Optional
from fastapi import FastAPI, Request
from fastapi_opentracing import get_opentracing_span_headers
from fastapi_opentracing.middleware import OpenTracingMiddleware

from app.settings import (
    USER_SVC,
    ITEM_SVC
)
import copy
import requests

app = FastAPI()
app.add_middleware(OpenTracingMiddleware)


dummy_list = [
        {
            "order_id": 1,
            "user": "1",
            "item": "item-1",
            "quantity": 1
        },
        {
            "order_id": 2,
            "user": "1",
            "item": "item-2",
            "quantity": 1
        },
        {
            "order_id": 3,
            "user": "1",
            "item": "item-3",
            "quantity": 1
        },
        {
            "order_id": 4,
            "user": "2",
            "item": "item-1",
            "quantity": 3
        },
        {
            "order_id": 5,
            "user": "3",
            "item": "item-2",
            "quantity": 1
        },
        {
            "order_id": 6,
            "user": "3",
            "item": "item-3",
            "quantity": 1
        },
        {
            "order_id": 7,
            "user": "4",
            "item": "item-3",
            "quantity": 1
        },
        {
            "order_id": 8,
            "user": "5",
            "item": "item-2",
            "quantity": 1
        }
    ]

@app.get("/")
async def root():
    headers = await get_opentracing_span_headers()
    print(headers)
    return {'span': headers}


@app.get("/api/orders")
async def read_users():
    headers = await get_opentracing_span_headers()
    protocol = "http"
    user_domain = USER_SVC
    user_path = "api/users"
    item_domain = ITEM_SVC
    item_path = "api/items"
    mapping_list = copy.deepcopy(dummy_list)
    users_response = requests.request(
        "GET",
        f"{protocol}://{user_domain}/{user_path}",
        headers=headers
    )
    items_response = requests.request(
        "GET",
        f"{protocol}://{item_domain}/{item_path}",
        headers=headers
    )
    users = eval(users_response.content.decode("utf-8"))
    items = eval(items_response.content.decode("utf-8"))

    for order in mapping_list:
        order["user"] = next(user for user in users if user["id"] == str(order["user"]))
        order["item"] = next(item for item in items if item["item_id"] == str(order["item"]))

    return mapping_list


# TODO: TBD in the future
@app.get("/api/order/{id}")
def read_user(id: int, request: Request):
    pass

