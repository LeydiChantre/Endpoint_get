"""Schemas for Stock API"""
from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal


class StockSchema(BaseModel):
   date: Optional[datetime] = None
   name: str = Field(..., max_length=100)
   symbol: str = Field(..., max_length=20)
   open: Decimal = Field(..., le=9999.99)
   high: Decimal = Field(..., le=9999.99)
   low: Decimal = Field(..., le=9999.99)
   close: Decimal = Field(..., le=9999.99)

   class config:
      orm_mode=True



