import json 


class Student:
    def __init__(self, name):
        self.name = name

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
        self.courses = self.courses.append(input("Введите название курса\n"))

    def to_dict(self) -> dict:
        return{
            "name":self.name,
            "courses":self.courses
        }
    


class Professor:
    def __init__(self, name):
        self.name = name 

        self.teaching_courses = []

    def teach(self, course):
        self.teaching_courses.append(course)
        return f"{self.name} is teaching {course}"

    def get_teaching_courses(self):
        return ", ".join(self.teaching_courses)
    
    def set_name(self) -> None:
        self.name = input("Введите имя преподавателя.\n")

    def set_teaching_courses(self) -> None:
        self.teaching_courses = self.teaching_courses.append(input("Введите преподаваемые курсы.\n"))

    def to_dict(self) -> dict:
        return{
            "name":self.name,
            "courses":self.teaching_courses
        }

class Json:
    def load_json() -> dict:
        try:
            with open("data.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"Students": [], "Proffessors": []}
        

    def save_json(data) -> None:
        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print("Данные успешно сохранены")
        pass


    def print_data(data):
        print("\nДанные из JSON:")
    
        print("\nСтуденты:")
        for students in data['students']:
            print(f"Имя: {students['name']}, Курсы обучения: {students['courses']} ")

        print("\nПреподаватели:")
        for proffesors in data['proffesors']:
            print(f"Имя: {proffesors['title']}, Курсы преподавания: {proffesors['num_of_ep']}")


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