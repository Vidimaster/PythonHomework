from random import randint
list_1 = []
list_2 = []
list_1_lenght = 20

for i in range (list_1_lenght):
    list_1.append(randint(-10, 20))

print(list_1)

min_value = int(input("Введите минимальное значение для диапазона: "))
max_value = int(input("Введите максимальное значение для диапазона: "))

for i in range (list_1_lenght):
    if list_1[i] >= min_value and list_1[i] <= max_value:
        list_2.append(i)
print("Индексы значений диапазона: ", list_2)
