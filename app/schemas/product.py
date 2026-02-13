from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: Optional[str] = None

class SupplierBase(BaseModel):
    name: str
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    id: int
    created_at: Optional[str] = None

class ProductBase(BaseModel):
    sku: str = Field(..., min_length=1, max_length=50)
    barcode: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., max_length=200)
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    cost_price: Decimal = Field(..., ge=0)
    selling_price: Decimal = Field(..., ge=0)
    quantity_in_stock: int = Field(0, ge=0)
    reorder_threshold: int = Field(5, ge=0)
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    barcode: Optional[str] = None
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    cost_price: Optional[Decimal] = None
    selling_price: Optional[Decimal] = None
    reorder_threshold: Optional[int] = None
    is_active: Optional[bool] = None

class ProductResponse(ProductBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category_name: Optional[str] = None
    supplier_name: Optional[str] = None