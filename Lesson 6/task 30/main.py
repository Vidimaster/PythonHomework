start_progression = int(input("Введите начальное значение прогрессии: "))
step_progression = int(input("Введите шаг прогрессии: "))
nums_progression = int(input("Введите количестиво чисел в прогрессии: "))
list_1 = []
for i in range (1, nums_progression + 1):
    list_1.append(start_progression + (i - 1)*step_progression)
print("Прогессия: ", list_1)