from dataclasses import dataclass


@dataclass
class Calculator:
    count: int = 0
    price: float = 0
    state: str = ''

    async def calculate(self) -> tuple:
        order_price = self.price * self.count

        d_percentage = await self._get_discount_percentage(order_price)
        d_cost = order_price - await self._calculate_percentage(order_price, d_percentage)

        t_percentage = await self._get_tax_percentage()
        t_cost = d_cost + await self._calculate_percentage(d_cost, t_percentage)

        return round(d_cost, 3), round(t_cost, 3)

    @staticmethod
    async def _get_discount_percentage(price: float) -> int:
        if price >= 50000:
            discount = 15
        elif price >= 10000:
            discount = 10
        elif price >= 7000:
            discount = 7
        elif price >= 5000:
            discount = 5
        elif price >= 1000:
            discount = 3
        else:
            discount = 0
        return discount

    async def _get_tax_percentage(self) -> float:
        states_taxes = {'UT': 6.85, 'NV': 8, 'TX': 6.25, 'AL': 4, 'CA': 8.25}
        return states_taxes[self.state]

    @staticmethod
    async def _calculate_percentage(price: float, percentage: float) -> float:
        return price / 100 * percentage if percentage else 0
