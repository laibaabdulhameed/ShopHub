from pydantic import BaseModel,Field

class Product(BaseModel):
    id : int = Field(gt=0 , description="Must be greater than zero.")
    name : str = Field(min_length=2, description="Minimum length is two.")
    price : float = Field(gt=0 , description="Must be greater than zero.")
    category :str
    stock : int = Field(ge=0 , description="Must be greater than or equal zero.")
    supplier : Supplier

class Supplier(BaseModel):
    name : str = Field(min_length=2, description="Minimum length is two.")
    country : str = Field(min_length=4, description="Minimum length is four.")

class ProductResponse(BaseModel):
    id : int
    name : str
    price : float
    category : str
    stock : int
    supplier : Supplier

class ProductResponse2(BaseModel):
    id = int