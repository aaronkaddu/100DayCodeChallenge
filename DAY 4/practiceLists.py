a = []

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Append elements to the list
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("List:", a)