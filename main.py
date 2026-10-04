from fastapi import FastAPI
from schemas.product import Product
from enum import Enum
from typing import Optional
app = FastAPI()

products = [
  {
    "id": 1,
    "name": "Laptop",
    "price": 85000,
    "category": "Electronics",
    "stock": 10
  },
  {
    "id": 2,
    "name": "Mouse",
    "price": 2500,
    "category": "Accessories",
    "stock": 25
  },
  {
    "id": 3,
    "name": "Keyboard",
    "price": 4500,
    "category": "Accessories",
    "stock": 15
  },
  {
    "id": 4,
    "name": "Smartphone",
    "price": 65000,
    "category": "Electronics",
    "stock": 8
  },
  {
    "id": 5,
    "name": "Headphones",
    "price": 7500,
    "category": "Accessories",
    "stock": 30
  },
  {
    "id": 6,
    "name": "Smart Watch",
    "price": 12000,
    "category": "Electronics",
    "stock": 12
  },
  {
    "id": 7,
    "name": "Monitor",
    "price": 32000,
    "category": "Electronics",
    "stock": 7
  },
  {
    "id": 8,
    "name": "External Hard Drive",
    "price": 14000,
    "category": "Accessories",
    "stock": 20
  },
  {
    "id": 9,
    "name": "Gaming Chair",
    "price": 28000,
    "category": "Furniture",
    "stock": 5
  },
  {
    "id": 10,
    "name": "Desk Lamp",
    "price": 3500,
    "category": "Home Decor",
    "stock": 40
  },
  {
    "id": 11,
    "name": "Backpack",
    "price": 5000,
    "category": "Accessories",
    "stock": 18
  },
  {
    "id": 12,
    "name": "Bluetooth Speaker",
    "price": 6000,
    "category": "Electronics",
    "stock": 22
  },
  {
    "id": 13,
    "name": "Webcam",
    "price": 8500,
    "category": "Accessories",
    "stock": 14
  },
  {
    "id": 14,
    "name": "Graphic Tablet",
    "price": 19500,
    "category": "Electronics",
    "stock": 9
  },
  {
    "id": 15,
    "name": "Microphone",
    "price": 11000,
    "category": "Accessories",
    "stock": 11
  },
  {
    "id": 16,
    "name": "Router",
    "price": 5500,
    "category": "Electronics",
    "stock": 16
  },
  {
    "id": 17,
    "name": "USB Flash Drive",
    "price": 1800,
    "category": "Accessories",
    "stock": 50
  },
  {
    "id": 18,
    "name": "Power Bank",
    "price": 4000,
    "category": "Accessories",
    "stock": 35
  },
  {
    "id": 19,
    "name": "HDMI Cable",
    "price": 1200,
    "category": "Accessories",
    "stock": 60
  },
  {
    "id": 20,
    "name": "Laptop Stand",
    "price": 3800,
    "category": "Accessories",
    "stock": 25
  }
]

class Category(str,Enum):
    ELECTRONICS = "Electronics"
    ACCESSORIES = "Accessories"
    FURNITURE = "Furniture"

@app.get("/products")
def view_products(category : Category | None = None, search : str | None = None, min_price : Optional[float] = None, max_price : Optional[float] = None , limit : Optional[int] = None):
        matched_products = products
        if category is not None:
            matched_products = [product for product in matched_products if product["category"] == category]
        if search:
            matched_products = [product for product in matched_products if search.lower() in product["name"].lower()]
        if min_price is not None:
            matched_products = [product for product in matched_products if product["price"] >= min_price]
        if max_price is not None:
            matched_products = [product for product in matched_products if product["price"] <= max_price]
        if limit is not None:
            matched_products = matched_products[:limit]

        return matched_products


@app.get("/products/{product_id}")
def get_product(product_id : int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"Product Not Found!"}

@app.post("/products")
def add_product(product : Product):
    product = {
        "id" : product.id,
        "name" : product.name,
        "price" : product.price,
        "category" : product.category,
        "stock" : product.stock
    }
    products.append(product)
    return product
        
@app.delete("/products/{product_id}")
def delete_product(product_id : int):
    products[:] = [p for p in products if p["id"] != product_id]

@app.put("/products/{product_id}")
def update_product(product_id : int, product : Product):
    updated_data = {
        "id" : product_id,
        "name" : product.name,
        "price" : product.price,
        "category" : product.category,
        "stock" : product.stock
    }

    products[:] = [updated_data if product["id"] == product_id else product for product in products]

            
