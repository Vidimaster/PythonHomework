from random import randint

number = int(input ('Введите количество монет: \n'))
i = 0
side1 = 0
side2 = 0
res = 0
while i < number:
    r = randint(0, 1)
    print('\n', r)
    i += 1
    if r == 0:
        side1 += 1
    else:
        side2 += 1
res = min(side1, side2)
print(f'\nНеобходимо перевернуть всего {res} монет.')