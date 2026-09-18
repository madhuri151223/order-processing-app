from app import calculate_order_total

def test_order_total():
    assert calculate_order_total(100, 3) == 300
