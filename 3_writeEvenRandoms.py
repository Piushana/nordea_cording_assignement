# Program to write sorted even numbers from ques2 to a file

# read data from file
file = open("randNumFile.txt", "r")

# split to a string array
strArray = file.read().split()
file.close()

# map string array to int array
intArray = list(map(int, strArray))

# sorting the array
sIntArray = sorted(intArray)

# write even numbers
file = open("evenNumFile.txt", "w")

for num in sIntArray:
    if num % 2 == 0:
        file.write(str(num) + '\n')

# close the file
file.close()











