from random import randint

number = 6
list_1 = []
res = []
count = 0

for i in range (number):
	list_1.append(randint(1, 10))

print(list_1)

for i in range (number - 1):
    if (i < number):
        res.append(list_1[i] + list_1[i - 1] + list_1[i + 1])
    else:
        res.append(list_1[i] + list_1[i - 1] + list_1[0])
print(max(res))