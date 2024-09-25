class Student:
    def __init__(self, name):
        self.name = name

        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"

    def get_courses(self):
        return ", ".join(self.courses)

class Professor:
    def __init__(self, name):
        self.name = name

        self.teaching_courses = []

    def teach(self, course):
        self.teaching_courses.append(course)
        return f"{self.name} is teaching {course}"

    def get_teaching_courses(self):
        return ", ".join(self.teaching_courses)
