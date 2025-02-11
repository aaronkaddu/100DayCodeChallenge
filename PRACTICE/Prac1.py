# write a program that prints numbers from 1 to 10

number1 = int(input("Enter starting range number: "))
number2 = int(input("Enter ending range number: "))

for i in range(number1, number2 + 1):
    print(f"Current Number: {i}")

# print the same above using a while loop Try the above exercise using a while loop.
# You’ll need to define a counter and an appropriate stopping condition.
# And you’ll need to manually increment the counter after every loop.

number3 = int(input("Enter starting range number: "))
number4 = int(input("Enter ending range number: "))

counter = 0

while number3 < number4:
    counter += 1
    print(f"Current Number: {counter}")

    if counter == number4:
        break

# solution from the internet

counter2 = 1
while counter2 <= 10:
    print('Current value:', counter2)
    counter2 += 1

