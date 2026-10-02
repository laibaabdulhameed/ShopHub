from fastapi import FastAPI
from schemas.product import Product
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
    }
]


@app.get("/products")
def view_products():
    return products 

@app.get("/products/{product_id}")
def get_product(product_id : int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"Product Not Found!"}

@app.post("/product")
def add_product(product : Product):
    products.append(product)
    return product
        
@app.delete("/product/{product_id}")
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

            
