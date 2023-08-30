from typing import List
from fastapi import APIRouter

from homework_6.database import goods, database
from homework_6.models import Product, ProductIn

product_router = APIRouter()


@product_router.get('/goods/', response_model=List[Product])
async def read_goods():
    query = goods.select()
    return await database.fetch_all(query)


@product_router.get('/goods/{order_id}', response_model=Product)
async def read_product(product_id: int):
    query = goods.select().where(goods.c.id == product_id)
    return await database.fetch_one(query)


@product_router.post('/goods/', response_model=Product)
async def create_product(product: ProductIn):
    query = goods.insert().values(**product.model_dump())
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


@product_router.put('/goods/{product_id}', response_model=Product)
async def update_product(new_product: ProductIn, product_id: int):
    query = goods.update().where(goods.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), "id": product_id}


@product_router.delete('/goods/{product_id}')
async def delete_product(product_id: int):
    query = goods.delete().where(goods.c.id == product_id)
    await database.execute(query)
    return {"message": "Product deleted"}
