import classes as cl
data = cl.Json.load_json()
data2 = cl.XML.load_from_xml()

T = True
while T == True:
    choice = int(input("Здравствуйте, выберите действие: \n 1-создать студента\n 2-создать преподавателя\
                       \n 3-Считать JSON в массив\n 4-Считать XML в массив\n 5-Вывести JSON\n 6-Вывести XML\
                        \n 7-Выйти из программы\n"))
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
            elif xoj == 2:
                data2['students'].append(studen.to_dict())
                cl.XML.save_to_xml(data2)
                print()
                break
            else:
                print("Неверный выбор")
        continue


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
            elif xoj == 2:
                data2['professors'].append(profes.to_dict())
                cl.XML.save_to_xml(data2)
                print()
                break
            else:
                print("Неверный выбор")
        continue
    elif choice == 3:

        res = cl.Json.data_to_dict(data)
        print(res)
        continue
    elif choice == 4:
        res = cl.XML.data_to_dict(data2)
        print(res)
        continue
    elif choice == 5:
        cl.Json.print_data(data)
        continue
    elif choice == 6:
        cl.XML.print_data(data2)
        continue
    elif choice == 7:
        T = False
        print("Выход")
    else: 
        print("Неверный выбор")