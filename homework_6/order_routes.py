from typing import List
from fastapi import APIRouter

from homework_6.database import orders, database
from homework_6.models import Order, OrderIn

order_router = APIRouter()


@order_router.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@order_router.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@order_router.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@order_router.put('/orders/{order_id}', response_model=Order)
async def update_order(new_order: OrderIn, order_id: int):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@order_router.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "Order deleted"}
