from typing import Literal

from pydantic import BaseModel, validator


class Base(BaseModel):
    count: int
    price: float
    state: Literal['UT', 'NV', 'TX', 'AL', 'CA']


class CalculateCost(Base):
    class Config:
        schema_extra = {
            'example': {
                'count': 5,
                'price': 350.4,
                'state': 'UT',
            }
        }

    @validator('count')
    def check_count(cls, count):
        assert count > 0, 'count must be greater than zero'
        return count

    @validator('price')
    def check_price(cls, price):
        assert price > 0, 'price must be greater than zero'
        return price


class ResultCost(BaseModel):
    cost_with_discount: float
    cost_with_tax: float
