from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    price: float
    quantity: int
    category: str


class OrderPricing:
    TAX_RATE = 0.18

    def __init__(self, items: List[Item], coupon: str = ""):
        self.items = items
        self.coupon = coupon

    def subtotal(self):
        return sum(item.price * item.quantity for item in self.items)

    def discount(self):
        total = self.subtotal()

        if self.coupon == "SAVE10":
            return total * 0.10

        if self.coupon == "BULK20":
            total_quantity = sum(item.quantity for item in self.items)

            # Intentional bug:
            # Should apply discount only when quantity >= 10
            if total_quantity > 10:
                return total * 0.20

        return 0

    def taxable_amount(self):
        return self.subtotal() - self.discount()

    def tax(self):
        return self.taxable_amount() * self.TAX_RATE

    def final_total(self):
        return round(self.taxable_amount() + self.tax(), 2)
