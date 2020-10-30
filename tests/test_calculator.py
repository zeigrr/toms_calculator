import pytest

from calculator import Calculator


data = [
    dict(
        count=0,
        price=0,
        state='UT',
        discount_result_cost=0,
        tax_cost=0
    ),
    dict(
        count=5,
        price=35,
        state='UT',
        discount_result_cost=175,
        tax_cost=186.988
    ),

    dict(
        count=2,
        price=60000,
        state='UT',
        discount_result_cost=102000,
        tax_cost=108987
    ),
    dict(
        count=1,
        price=11000,
        state='NV',
        discount_result_cost=9900,
        tax_cost=10692
    ),
    dict(
        count=1,
        price=7500,
        state='TX',
        discount_result_cost=6975,
        tax_cost=7410.938
    ),
    dict(
        count=1,
        price=6999,
        state='AL',
        discount_result_cost=6649.05,
        tax_cost=6915.012
    ),
    dict(
        count=3,
        price=500,
        state='CA',
        discount_result_cost=1455,
        tax_cost=1575.037
    )
]


@pytest.mark.asyncio
async def test_calculate():
    for obj in data:
        cost_with_discount, cost_with_tax = await Calculator(
            count=obj['count'],
            price=obj['price'],
            state=obj['state']
        ).calculate()
        assert cost_with_discount == obj['discount_result_cost']
        assert cost_with_tax == obj['tax_cost']
