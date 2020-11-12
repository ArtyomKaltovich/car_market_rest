from abc import ABC, abstractmethod
from typing import List

from pydantic import BaseModel


class Car(BaseModel):
    brand: int
    model: int
    city: int


class Sale(BaseModel):
    id: int
    car: Car
    selling_price: int


class SalesClient(ABC):
    @abstractmethod
    async def find_sales(self, car: Car) -> List[Sale]:
        pass
