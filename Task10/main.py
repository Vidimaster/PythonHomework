import random

number = int(input ())
r = 0
i = 0
side1 = 0
side2 = 0
res = 0
while i < number:
    r = random.randrange(0, 2)
    print(r)
    i += 1
    if r == 0:
        side1 += 1
    else:
        side2 += 1
res = min(side1, side2)
print(res)