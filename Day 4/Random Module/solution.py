import random

# Random integer
print(random.randint(0, 10))

# Random float between 0 and 1
print(random.random())

# Random float between 1 and 10
print(random.uniform(1, 10))

# Random choice from a list
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))

# Random sample
print(random.sample(my_list, 3))

# Random seed
# Note: The result will always be the same (using the same seed). It can be useful for debugging.
random.seed(1)
print(random.randint(0, 10))
random.seed(1)
print(random.randint(0, 10))
random.seed(1)
print(random.randint(0, 10))

# Reset the seed
random.seed()

# Head or tails ?
if random.randint(0, 1) == 0: # Why is it always 0 here ?
    print("Heads")
else:
    print("Tails")

print(random.choice(["Heads", "Tails"]))



