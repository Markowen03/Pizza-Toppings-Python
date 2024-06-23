pizza_toppings = []

while True:
    item = input("Enter a type of toppings to add to the list (or 'q' to quit): ")
    
    if item == 'q':
        break
    else:
        pizza_toppings.append(item)

print("Current Pizza Topping List:", pizza_toppings)

item_to_remove = input("Enter a type of topping to remove from the list: ")

if item_to_remove in pizza_toppings:
    pizza_toppings.remove(item_to_remove)
    print(f"'{item_to_remove}' has been removed from the Pizza Topping list.")
else:
    print(f"'{item_to_remove}' is not in the Pizza Topping list.")

print("Updated List:", pizza_toppings)
