from random import randint

list_1_len = randint(1, 10)

list_2_len = randint(1, 10)

list_1 = []
list_2 = []

for i in range (list_1_len):
	list_1.append(randint(1, 20))

for i in range (list_2_len):
	list_2.append(randint(1, 20))

print(list_1)

print(list_2)

list_1 = set(list_1)

list_2 = set(list_2)

list_3 = list_1.intersection(list_2) 

list_3 = list(list_3)

list_3 = sorted(list_3)
print(list_3)