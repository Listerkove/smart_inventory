from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ReplenishmentSuggestionBase(BaseModel):
    product_sku: str
    forecasted_demand: int
    current_stock: int
    suggested_quantity: int

class ReplenishmentSuggestionCreate(BaseModel):
    lookback_days: int = 30
    forecast_days: int = 7
    safety_stock_factor: float = 1.5

class ReplenishmentSuggestionResponse(ReplenishmentSuggestionBase):
    id: int
    date_generated: date
    is_acted_upon: bool
    acted_upon_at: Optional[datetime] = None
    
    # Additional fields from join
    product_name: Optional[str] = None
    product_barcode: Optional[str] = None

class ReplenishmentAction(BaseModel):
    suggestion_id: int
    action: str  # 'accept' or 'ignore'