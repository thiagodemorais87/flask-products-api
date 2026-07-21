from pydantic import BaseModel, Field, PositiveFloat
from typing import Optional

class ProductCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: PositiveFloat
    stock: int = Field(default=0, ge=0)


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    price: Optional[PositiveFloat] = None
    stock: Optional[int] = Field(None, ge=0)