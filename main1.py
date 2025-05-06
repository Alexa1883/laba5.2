import random

array = [0] * 15
for i in range(15):
    array[i] = random.randint(1, 100)

for element in array:
    print(element)