price = 0
user = ""
while True:
    command = input()

    try:
        current_price = float(command)

        if current_price < 0:
            print("Invalid price!")
            continue
        else:
            price += current_price
    except ValueError:
        user = command
        break

tax = price * 0.20
final_price = price + tax

if user == "special":
    final_price = final_price * 0.90
else:
    final_price = final_price

if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
