from math import sqrt

x1 = int (input('Введите сумму чисел: X и Y \n'))
y2 = int (input('Введите произведение чисел: X и Y \n'))

desc = x1*x1 - 4*y2
res_y = int((x1 + sqrt(desc)) / 2)
res_x = int(x1 - res_y)
print(f'\nЧисло X = {res_x} \nЧисло Y = {res_y}')