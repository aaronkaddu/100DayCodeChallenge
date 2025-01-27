#  A Tip calculator
print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip / 100)
# print("Your total bill is:", total_bill)

# what will each person pay
bill_per_person = total_bill / people

print("Each person should pay: ${:.2f}".format(bill_per_person))


