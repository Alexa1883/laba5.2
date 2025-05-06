array = [0] * 15

for i in range(14):
    array[i] = int(input(f"Введите элемент {i + 1}: "))

array[14] = sum(array[:14])
print("Элементы массива: ")
for element in array:
    print(element)
