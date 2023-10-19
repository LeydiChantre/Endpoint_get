""" Main module of Finance Application"""

from typing import List
from fastapi import FastAPI

from finance_project.models.stocks import Stock

from finance_project.schemas.stock_schemas import StockSchema

from finance_project.database.database import SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stocks")
def get_stocks():
    print(str(stocks))
    return stocks

## Endpoint Get
@app.get("/stocks/{name}")
def get_stocks(name: str):
    for objeto in stocks:
        if name==objeto.name:
            return objeto
    return None
    
   


@app.post("/stocks/create-stock")
def create_stocks(stock_body: StockSchema):
    stock = Stock(**stock_body.model_dump()) # Kwargs: Keyword arguments
    stocks.append(stock)