from order_pricing import Item, OrderPricing


def test_save10_coupon():
    items = [
        Item("Keyboard", 1000, 1, "electronics"),
        Item("Mouse", 500, 1, "electronics"),
    ]

    order = OrderPricing(items, coupon="SAVE10")

    assert order.subtotal() == 1500
    assert order.discount() == 150
    assert order.final_total() == 1593.0


def test_bulk20_coupon_when_quantity_is_exactly_10():
    items = [
        Item("Notebook", 50, 10, "stationery"),
    ]

    order = OrderPricing(items, coupon="BULK20")

    assert order.subtotal() == 500
    assert order.discount() == 100
    assert order.final_total() == 472.0


def test_no_coupon():
    items = [
        Item("Pen", 20, 5, "stationery"),
    ]

    order = OrderPricing(items)

    assert order.subtotal() == 100
    assert order.discount() == 0
    assert order.final_total() == 118.0
