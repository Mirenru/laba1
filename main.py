import classes as cl
data = cl.Json.load_json()
cl.Json.print_data(data)
res = cl.Json.data_to_dict(data)
print(res)

T = True
while T == True:
    choice = int(input("Здравствуйте, выберите действие: \n1-создать студента\n2-создать преподавателя\
                       \n3-Считать JSON в массив\n4-Считать XML в массив\n5-Вывести JSON\n6-Вывести XML\n\
                       7-Выйти из программы\n"))
    if choice == 1:
        #создание студента
        studen = cl.Student()
        studen.set_name()
        x=int(input("Введите количество курсов\n"))
        for i in range(x):
            studen.set_course()
        print("Вы создали объект с данными: ",studen.printinf())

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:    
                data["students"].append(studen.to_dict())
                cl.Json.save_json(data)
                break

            else:
                print("Неверный выбор")
        break


    elif choice == 2:
        profes = cl.Professor()
        profes.set_name()
        x=int(input("Введите количество курсов\n"))
        for i in range(x):
            print("Названия курсов пишутся на английском.\n")
            profes.set_teaching_courses()
        print("Вы создали объект с данными: ",profes.printinf())

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:    
                data["proffesors"].append(profes.to_dict())
                cl.Json.save_json(data)
                break

            else:
                print("Неверный выбор")
        break
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