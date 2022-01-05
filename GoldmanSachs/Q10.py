import random

# Initialize Array 
arr = []
for i in range(10000000):
    arr.append(random.randint(1, 10000000))

arr.sort()
print(arr[-10:])