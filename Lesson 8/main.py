def OpenPhoneBook():
    file = open('phone.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()

    data = list(map(lambda x: x.strip(), data))
    return data

def PrintPhoneBook(lst):
    print(f'\n{"Имя и фамилия":25s} {"Телефон":25s} {"Комментарии"}\n')
    for i in range(len(lst)):
        string_1 = lst[i]
        string_1 = string_1.split(';')
        print(f'{string_1[0]:25s} {string_1[1]:25s} {string_1[2]}')

def DeleteContact(lst, str_del):
    for i in range(len(lst)):
        string_1 = lst[i]
        string_1 = string_1.split(';')
        if string_1[0] == str_del:
            lst.pop(i)
            print('\n' + str_del + ': ' + "Контакт удален")
            break
    else:
        print("Нет такого контакта")
    return lst

def ChangeContact(lst, str_change):
    for i in range(len(lst)):
        string_1 = lst[i]
        string_1 = string_1.split(';')
        if string_1[0] == str_change:
            string_2 = str(input('\nВведите имя и фамилию: \n'))
            string_2 = string_2 + ';'
            string_2 = string_2 + str(input('\nВведите телефон: \n'))
            string_2 = string_2 + ';'
            string_2 = string_2 + str(input('\nВведите Комментарий: \n'))           
            print(str('\n' + lst[i]) + '\n' + 'Изменен на: \n' + string_2)
            lst[i] = string_2    
            break
    else:
        print("Нет такого контакта")
    return lst

def FindContact(lst, str_find):
    for i in range(len(lst)):
        
        string_1 = lst[i]
        string_1 = string_1.split(';')
        if string_1[0] == str_find:  
            print("Найден контакт:")
            print(f'\n{"Имя и фамилия":25s} {"Телефон":25s} {"Комментарии"}')        
            print(f'{string_1[0]:25s} {string_1[1]:25s} {string_1[2]}')
            break
    else:
        print("Нет такого контакта")

def SaveContact(lst, str_save):
    temp = []
    for i in range(len(lst)):
        string_1 = lst[i]
        string_1 = string_1.split(';')
        if string_1[0] == str_save:          
            print('\n' + lst[i] + ': ' + "Контакт сохранен в файл phone_save.txt")
            temp = lst.pop(i)
            file = open('phone_save.txt', 'w', encoding='UTF-8')
            file.write(temp + '\n')
            file.close()
            break
    else:
        print("Нет такого контакта")
    return temp
PrintPhoneBook(OpenPhoneBook())

command = int(input('\nВведите команду: \n1 - добавить контакт \n2 - удалить контакт \n3 - изменить контакт \n4 - найти контакт \n5 - сохранить контакт \n6 - выход \n'))

if command == 1:

    string_2 = str(input('\nВведите имя и фамилию: \n'))
    string_2 = string_2 + ';'
    string_2 = string_2 + str(input('\nВведите телефон: \n'))
    string_2 = string_2 + ';'
    string_2 = string_2 + str(input('\nВведите Комментарий: \n'))
    print('\n' + string_2 + ': ' + "Контакт добавлен")
    file = open('phone.txt', 'r', encoding='UTF-8')
    data_1 = file.readlines()
    file.close()
    data_1 = list(map(lambda x: x.strip(), data_1))
    data_1.append(string_2)
    data_1 = '\n'.join(data_1)
    file = open('phone.txt', 'w', encoding='UTF-8')
    file.write(data_1)
    file.close()
    PrintPhoneBook(OpenPhoneBook())
elif command == 2:
    string_2 = str(input('\nВведите имя и фамилию для удаления: \n'))
    data_1 = DeleteContact(OpenPhoneBook(), string_2)
    
    file = open('phone.txt', 'w', encoding='UTF-8')
    for i in range(len(data_1)):
         string_1 = data_1[i]
         file.write(string_1 + '\n')
    file.close()

    PrintPhoneBook(OpenPhoneBook())
elif command == 3:
    string_3 = str(input('\nВведите имя и фамилию, чтобы поменять контакт: \n'))
    data_1 = ChangeContact(OpenPhoneBook(), string_3)

    file = open('phone.txt', 'w', encoding='UTF-8')
    for i in range(len(data_1)):
         string_1 = data_1[i]
         file.write(string_1 + '\n')
    file.close()

    PrintPhoneBook(OpenPhoneBook())
elif command == 4:
    string_4 = str(input('\nВведите имя и фамилию, чтобы найти контакт: \n'))
    FindContact(OpenPhoneBook(), string_4)
elif command == 5:
    string_5 = str(input('\nВведите имя и фамилию, чтобы сохранить контакт: \n'))
    data_1 = SaveContact(OpenPhoneBook(), string_5)

else: 
    print ("Выход")

