budget = int(input())
total_price = 0

while True:
    product = input()
    if product == "End":
        print("You bought everything needed.")
        break

    product_price = int(product)

    if total_price + product_price > budget:
        print("You went in overdraft!")
        break

    total_price += product_price
