string_1 = "пар-ра-рам рам-пам-пам ра-па-дям"
string_1 = string_1.upper()
letters = ['А', 'И', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'Ю', 'Я']
letters_sum = lambda x: sum(1 for i in x if i in letters)
rhyme = letters_sum(list(string_1.split(' '))[0])
string_1 = enumerate(string_1.split(' '))

for i, word in string_1:
    if letters_sum(word) != rhyme:
        print('Пам парам')
        break
else:
    print('Парам пам-пам')