menu = {"Latte": 4.50, "Espresso": 3.00, "Cold Brew": 4.00, "Mocha": 4.75}
receipt = {"customer": "", "drink": "", "price": 0.0}

name = input("Your name: ")
drink = input("Drink (Latte, Espresso, Cold Brew, Mocha): ")

receipt["customer"] = name
receipt["drink"] = drink
receipt["price"] = menu[drink]

print("Customer:", receipt["customer"])
print("Drink:", receipt["drink"])
print("Price: $", receipt["price"])
