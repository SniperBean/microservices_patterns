from typing import Optional
from fastapi import FastAPI, Request
from fastapi_opentracing import get_opentracing_span_headers
from fastapi_opentracing.middleware import OpenTracingMiddleware

app = FastAPI()
app.add_middleware(OpenTracingMiddleware)

dummy_dict = {
    "item-1": {"name": "Microservice patterns", "detail": "Introduce modern architecture pattern."},
    "item-2": {"name": "Release it! 2nd edition", "detail": "Case study and consulting skills share."},
    "item-3": {"name": "Designing Event-Driven Systems", "detail": "Design event-driven architecture in action."}
}


@app.get("/")
async def root():
    carrier = await get_opentracing_span_headers()
    return {'span': carrier}


@app.get("/api/items")
def read_items():
    dummy_list = []
    for item_id, data in dummy_dict.items():
        dummy_list.append({"item_id": item_id, "data": data})
    return dummy_list


@app.get("/api/item/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id, "data": dummy_dict[item_id]}
