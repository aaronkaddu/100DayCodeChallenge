# Customer ordering a Pizza
print("Welcome to Python Pizza Deliveries!!!!")
size = input("What size pizza do you want? S, M or L? : ")
pepperoni = input("Do you want pepperoni on your Pizza Y or N : ")
extra_cheese = input("Do you want extra cheese on your Pizza Y or N : ")
price = 0

if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    price += 25
    if pepperoni == "Y":
        price += 3
else:
    print("You didnt order anything on our Menu")

if extra_cheese == "Y":
    price += 1
else:
    print("You didnt add extra cheese on your Pizza")

print(f"The total bill is {price}")


