import classes as cl
data = cl.Json.load_json()

res = cl.Json.data_to_dict(data)
print(res)

T = True
while T == True:
    choice = int(input("Здравствуйте, выберите действие: \n1-создать студента\n2-создать преподавателя\
                       \n3-Считать JSON в массив\n4-Считать XML в массив\n5-Вывести JSON\n6-Вывести XML\n\
                       7-Выйти из программы\n"))
    if choice == 1:
        #создание студента
        student = cl.Student()

        print()
    elif choice == 2:
        print()
    elif choice == 3:
        print()
    elif choice == 4:
        print()
    elif choice == 5:
        print()
    elif choice == 6:
        print
    elif choice == 7:
        T = False
    else: 
        print("Неверный выбор")