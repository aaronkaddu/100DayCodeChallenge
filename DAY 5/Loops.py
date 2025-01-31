# learning loops

fruits = ["Apples", "Mangoes", "Peach"]

for fruit in fruits:
    print(fruit)

# Exam Score
student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

max_score = 0

for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)

# Loops with range
sum = 0

for number in range(1, 101):
    sum += number
print(sum)