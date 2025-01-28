# Photo Application

height = int(input("Enter your height in metres: "))
age = int(input("Enter your age in years: "))
bill = 0

if height > 120:
    print("You can ride")

    # check for age
    if age < 12:
        bill = 5
        # print("You will pay $5")
    elif age <= 18:
        bill = 7
        # print("You will pay $7")
    else:
        bill = 12
        # print("You will pay $12")

    wants_photos = input("Would you like to take photos? (Y/N): ")
    if wants_photos == "Y":
        bill += 3
    else:
        bill += 0

    print(f"Your total bill will be {bill}")
else:
    print("Sorry you have to grow taller before you can ride")