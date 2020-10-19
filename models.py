from typing import Literal

from pydantic import BaseModel


class Index(BaseModel):
    count: int
    price: float
    state: Literal['UT', 'NV', 'TX', 'AL', 'CA']


class PriceWithDiscount(BaseModel):
    count: int
    price: float

    class Config:
        schema_extra = {
            'example': {
                'count': 5,
                'price': 350.4,
            }
        }


class PriceWithTax(BaseModel):
    price: float
    state: Literal['UT', 'NV', 'TX', 'AL', 'CA']

    class Config:
        schema_extra = {
            'example': {
                'price': 1699.44,
                'state': 'UT',
            }
        }


class ResultCost(BaseModel):
    result_cost: float
