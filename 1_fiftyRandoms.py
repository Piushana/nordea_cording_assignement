# Program to generate 50 randoms between 0-1000

# importing the random module
import random

# Initialization
lower, upper = 0, 1000
numRandomNumbers = 50

for x in range(numRandomNumbers):
    print(random.randint(lower, upper))
