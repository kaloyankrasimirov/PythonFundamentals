shopping_list = []
shopping_list.append("salt")
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append("cheese")
shopping_list.append("vinegar")

result = ", ".join(shopping_list)

print(result + ".")

#for item in shopping_list:
#    if item != shopping_list[-1]:
#      print(item, end=", ")
#    else:
#      print(item, end=".")
