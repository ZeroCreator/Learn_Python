# Aннотации типов в python
def calculate_price(unit_price, quantity):
    return unit_price * quantity


def calculate_price1(unit_price: float, quantity: int) -> float:
    return unit_price * quantity

if __name__ == '__main__':
    print(calculate_price1(73.5, 2))
    print(calculate_price1(2, 73.3))
    print(calculate_price1("Hello", 5))