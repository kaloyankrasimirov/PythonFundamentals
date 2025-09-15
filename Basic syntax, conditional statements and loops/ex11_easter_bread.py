budget = float(input())
flour_price = float(input())
price_eggs = flour_price * 0.75
price_liter_milk = flour_price* 1.25

number_of_loaves = 0
colored_eggs = 0
money_left = budget

loaf_price = flour_price + price_eggs + (price_liter_milk / 4)

while money_left >= loaf_price:
    money_left -= loaf_price
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
