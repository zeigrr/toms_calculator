from dataclasses import dataclass


@dataclass
class Calculator:
    count: int = 0
    price: float = 0
    state: str = ''

    async def calculate_with_discount(self):
        price = self.price * self.count
        percentage = await self._get_discount_percentage(price)
        result_price = price - await self._calculate_percentage(price, percentage)
        return round(result_price, 3)
    
    async def calculate_with_tax(self):
        percentage = await self._get_tax_percentage()
        result_price = self.price + await self._calculate_percentage(self.price, percentage)
        return round(result_price, 3)

    @staticmethod
    async def _get_discount_percentage(price):
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

    async def _get_tax_percentage(self):
        states_taxes = {'UT': 6.85, 'NV': 8, 'TX': 6.25, 'AL': 4, 'CA': 8.25}
        return states_taxes[self.state]

    @staticmethod
    async def _calculate_percentage(price, percentage):
        return price / 100 * percentage if percentage else 0
