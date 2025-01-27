# learning Conditional Statements
height = int(input("Enter your height in centimeters: "))


if height > 120:
    print(f"Your height of {height} is more than 120 centimeters.")
    age = int(input("Enter your age: "))
    if age > 18:
        print(f"Your age is {age}. Therefore Pay $12")
    else:
        print(f"Your age is {age}. Therefore Pay $7")
else:
    print(f"Sorry height of {height} is less than 120 centimeters.")