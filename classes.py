import json 
import xml.etree.ElementTree as et



class Student:
    name = ""
    courses = []
    def __init__(self):
        self.name = ""

        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"

    def get_name(self):
        return f"Имя студента {self.name}."

    def get_courses(self):
        return ", ".join(self.courses)
    
    def set_name(self) -> None:
        self.name = input("Введите имя студента\n")

    def set_course(self) -> None:
        s  = input("Введите название курса\n")
        self.courses.append((s))

    def to_dict(self) -> dict:
        return{
            "name":self.name,
            "courses": self.courses
        }
    def printinf(self) -> str:
        return f"Студент {self.name}, курсы обучения:{self.courses}."

class Professor:
    name = ""
    teaching_courses = []
    def __init__(self):
        self.name = ""

        self.teaching_courses = []

    def teach(self, course):
        self.teaching_courses.append(course)
        return f"{self.name} is teaching {course}"

    def get_teaching_courses(self):
        return ", ".join(self.teaching_courses)
    
    def set_name(self) -> None:
        self.name = input("Введите имя преподавателя.\n")

    def set_teaching_courses(self) -> None:
        self.teaching_courses.append(input("Введите преподаваемые курсы.\n"))

    def to_dict(self) -> dict:
        return{
            "name":self.name,
            "tcourses":self.teaching_courses
        }
    def printinf(self) -> str:
        return f"Преподаватель {self.name}, курсы которые он преподаёт:{self.teaching_courses}."

class Json:
    def load_json() -> dict:
        try:
            with open("data.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"Students": [], "Proffessors": []}
        

    def save_json(data) -> None:
        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            print("Данные успешно сохранены")
        pass


    def print_data(data):
        print("\nДанные из JSON:")
    
        print("\nСтуденты:")
        for students in data['students']:
            print(f"Имя: {students['name']}, Курсы обучения: {students['courses']} ")

        print("\nПреподаватели:")
        for proffesors in data['proffesors']:
            print(f"Имя: {proffesors['name']}, Курсы преподавания: {proffesors['tcourses']}")


    def data_to_dict(data) -> dict:

        while True:
            choice = int(input("Что записать в массив?\n1-Студенты\n2-Преподаватели\n"))
            if choice == 1:
                res = []
                for student in data['students']:
                    res.append(student)
                print("Данные успешно сохранены в массив \n")
                return res
            elif choice == 2:
                res = []
                for prof in data['proffesors']:
                    res.append(prof)
                print("Данные успешно сохранены в массив \n")
                return res
            else:
                print("Неверный выбор")

class XML:

    # Функция для красивых отступов 
    def indent(elem, level = 0) -> None:
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                XML.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
        pass

    # Функция сохранения информации в xml
    def save_to_xml(data) -> None:
        root = et.Element('data')

        students = et.SubElement(root, 'students')
        for student in data['students']:
            student_element = et.SubElement(students, 'student')
            for key, value in student.items():
                child = et.SubElement(student_element, key)
                child.text = str(value)  

        professors = et.SubElement(root, 'professors')
        for professor in data['professors']:
            professor_element = et.SubElement(professors, 'professor')
            for key, value in professor.items():
                child = et.SubElement(professor_element, key)
                child.text = str(value)  

        # Добавляем отступы для красивого форматирования
        XML.indent(root)

        # Создаем дерево XML и записываем его в файл
        tree = et.ElementTree(root)
        tree.write("data.xml", encoding='utf-8', xml_declaration=True)

        print(f"Данные успешно сохранены в файл '{"data.xml"}'")
        pass

    def add_professors(data, professors):
        data['professors'].append(professors.to_dict())

    # Функция чтения информации из xml
    def load_from_xml() -> dict:
        try:
            tree = et.parse("data.xml")
            root = tree.getroot()
        except FileExistsError:
            return {"students" : [], "professors" : []}
        
        data = {"students" : [], "professors" : []}

        for student in root.find("students"):
            student_data = {}
            for child in student:
                student_data[child.tag] = child.text
            data["students"].append(student_data)

        for serial in root.find("professors"):
            serial_data = {}
            for child in serial:
                serial_data[child.tag] = child.text
            data["professors"].append(serial_data)

        return data
    
    def print_data(data):
        print("\nДанные из XML:")

        print("\nСтуденты:")
        for student in data['students']:
            print(f"Имя: {student['name']}, Курсы: {student['courses']}")

        print("\nПреподаватели:")
        for professor in data['professors']:
            print(f"Имя: {professor['name']}, преподаваемые курсы: {professor['tcourses']}")
        
        pass

    def data_to_dict(data) -> dict:
        while True:
            choice = int(input("Что записать в массив?\n1-Студенты\n2-Преподаватели\n"))
            if choice == 1:
                res = []
                for student in data['students']:
                    res.append(student)
                print("Данные успешно сохранены в массив \n")
                break
            elif choice == 2:
                res = []
                for professor in data['professors']:
                    res.append(professor)
                print("Данные успешно сохранены в массив \n")
                break
            else:
                print("Неверный выбор")
        return res
