from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class SaleItemCreate(BaseModel):
    sku: str
    quantity: int = Field(..., gt=0)
    unit_price: Decimal = Field(..., ge=0)

class SaleCreate(BaseModel):
    transaction_number: str
    transaction_date: datetime
    items: List[SaleItemCreate]

class SaleItemResponse(BaseModel):
    id: int
    transaction_id: int
    product_sku: str
    product_name: Optional[str] = None
    quantity: int
    unit_price: Decimal
    line_total: Decimal

class SaleTransactionResponse(BaseModel):
    id: int
    transaction_number: str
    user_id: int
    username: Optional[str] = None
    total_amount: Decimal
    transaction_date: datetime
    created_at: datetime
    items: Optional[List[SaleItemResponse]] = None

class SaleSummaryResponse(BaseModel):
    total_transactions: int
    total_revenue: Decimal
    total_items_sold: int