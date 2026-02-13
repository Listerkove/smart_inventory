from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel

class LowStockAlert(BaseModel):
    sku: str
    name: str
    quantity_in_stock: int
    reorder_threshold: int
    alert_message: str

class DailySalesSummary(BaseModel):
    transaction_date: date
    transaction_count: int
    unique_products_sold: int
    total_items_sold: int
    total_revenue: Decimal

class CurrentInventoryItem(BaseModel):
    sku: str
    name: str
    category: Optional[str]
    quantity_in_stock: int
    reorder_threshold: int
    selling_price: Decimal
    potential_revenue: Decimal
    is_active: bool

class ProductPerformance(BaseModel):
    sku: str
    name: str
    category_name: Optional[str]
    quantity_in_stock: int
    total_sold_30d: int
    avg_daily_sales: float
    status: str

class DashboardSummary(BaseModel):
    total_products: int
    total_stock_value: Decimal
    low_stock_count: int
    out_of_stock_count: int
    today_sales: Optional[DailySalesSummary]