from main import products
from fastapi import HTTPException
from typing import Annotated
from fastapi import Path

def get_product_by_id(product_id : Annotated[int, Path(gt=0)]):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(
        status_code=404,
        detail="Item not found")