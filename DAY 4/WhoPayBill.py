# Who will Pay the Bill
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
payer = random.choice(friends)
print(payer)

# Option 2
random_index = random.randint(0, 4)
print(friends[random_index])