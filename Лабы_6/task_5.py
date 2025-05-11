"""
Задача 5:

Создайте систему для университета:

    • Класс Student (свойства: имя, группа)

    • Класс Course (свойства: название, преподаватель)

    • Класс University (композиция: содержит список студентов и курсов)

    • Методы:
        o Student.add_student(name, group) - добавление студентов
        o Course.add_course (name, teacher) – добавление курсов
        o University .sign_up(student, course) – запись студента на
        курс
        o University.get_participants(course) - вывод списка
        студентов курса

    • Требования:
        o Использовать композицию (университет содержит студентов и курсы)
        o Реализовать взаимодействие между объектами
"""

class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
    
    def __str__(self):
        return f"{self.name} (группа {self.group})"

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def __str__(self):
        return f"Курс: {self.name}, Преподаватель: {self.teacher}"

class University:
    def __init__(self):
        self.students = []
        self.courses = []
    
    def add_student(self, name, group):
        student = Student(name, group)
        self.students.append(student)
        return student
    
    def add_course(self, name, teacher):
        course = Course(name, teacher)
        self.courses.append(course)
        return course
    
    def sign_up(self, student, course):
        if student not in self.students:
            raise ValueError("Студент не зарегистрирован в университете")
        if course not in self.courses:
            raise ValueError("Курс не существует в университете")
        course.add_student(student)
    
    def get_participants(self, course):
        if course not in self.courses:
            raise ValueError("Курс не существует в университете")
        return course.students
    
    def __str__(self):
        return f"Университет: {len(self.students)} студентов, {len(self.courses)} курсов"

university = University()

student1 = university.add_student("Иван Иванов", "Группа 101")
student2 = university.add_student("Петр Петров", "Группа 102")
student3 = university.add_student("Мария Сидорова", "Группа 101")

math = university.add_course("Математика", "Проф. Смирнов")
physics = university.add_course("Физика", "Доц. Козлов")

university.sign_up(student1, math)
university.sign_up(student2, math)
university.sign_up(student3, physics)
university.sign_up(student1, physics)

print(f"Участники курса {math.name}:")
for student in university.get_participants(math):
    print(f" - {student}")

print(f"\nУчастники курса {physics.name}:")
for student in university.get_participants(physics):
    print(f" - {student}")

print(f"\n{university}")