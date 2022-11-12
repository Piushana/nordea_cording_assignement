# Program to write 50 randoms between 0-1000 to textfile

# importing the  modules
import random

# Initialization
lower, upper = 0, 1000
numRandomNumbers = 50

# create a new file
file = open("randNumFile.txt", "w")

for x in range(numRandomNumbers):
    num = random.randint(lower, upper)

    # write the numbers
    file.write(str(num) + '\n')

# close the file
file.close()



