def calculate_total_price(some_product: str, some_quantity: int) -> float:
    price_per_product = 0
    if some_product == "coffee":
        price_per_product = 1.50
    elif some_product == "water":
        price_per_product = 1.00
    elif some_product == "coke":
        price_per_product = 1.40
    elif some_product == "snacks":
        price_per_product = 2.00

    return price_per_product * some_quantity


product = input()
quantity = int(input())
print(f"{calculate_total_price(product, quantity):.2f}")