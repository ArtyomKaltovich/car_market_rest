from collections import namedtuple
from typing import List, Optional

import pandas as pd
from pydantic import BaseModel


class Car(BaseModel):
    brand: int
    model: int
    city: int


class Sale(BaseModel):
    id: int
    car: Car
    selling_price: int


class Market(BaseModel):
    car: Car
    median_price: float
    sales: List[Sale]


class DB:
    # save all info in one place for testing speedup
    COLUMNS = ["id", "price", "brand", "model", "city"]
    SaleInfo = namedtuple("SaleInfo", COLUMNS)

    def __init__(self, sales: Optional[List[Sale]] = None):
        df = []
        id2sale = {}
        if sales:
            for sale in sales:
                df.append(DB.SaleInfo(sale.id, sale.selling_price, sale.car.brand, sale.car.model, sale.car.city))
            id2sale = {sale.id: sale for sale in sales}
        self._sales = id2sale
        df = pd.DataFrame(df, columns=DB.COLUMNS)
        self._df = df

    async def find_sales(self, car: Car) -> Market:
        df = self._df
        df = df[(df["brand"] == car.brand) & (df["model"] == car.model) & (df["city"] == car.city)]
        sales = [self._sales[i] for i in df["id"]]
        return Market(car=car, median_price=float(df["price"].median()), sales=sales)
