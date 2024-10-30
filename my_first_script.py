#print("Hello World")

#store = input("Where do you shop?")

#Currancy = "$"
#milk_price = 6.54
#bread_price = 4.99
#eggs_price = 2.60

#Total = (milk_price + bread_price + eggs_price)

#print("Your " + store.upper() + """ Basket: Milk, Eggs, Bread.

#Basket total: """ + Currancy + str(Total))

apples_tuple = ("apples", 0.50, 5)
milk_tuple = ("milk", 1.75, 2)
bread_tuple = ("bread", 2.15, 3)

grocery_list = [apples_tuple[0], milk_tuple[0], bread_tuple[0]]

print(grocery_list[0] + " - Qty: " + str(apples_tuple[2]))
print(grocery_list[1] + " - Qty: " + str(milk_tuple[2]))
print(grocery_list[2] + " - Qty: " + str(bread_tuple[2]))

apple_total = apples_tuple[2] * apples_tuple[1]
milk_total = milk_tuple[2] * milk_tuple[1]
bread_total = bread_tuple[2] * bread_tuple[1]

basket_total = apple_total + milk_total + bread_total
print("Basket Total: $" + str(basket_total))
