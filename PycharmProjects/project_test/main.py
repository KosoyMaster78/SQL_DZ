class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self,other):
        if self.average_grade() < other.average_grade():
            return (f"Средняя оценка {self.name} ниже чем у {other.name}")
        else:
            return (f"Средняя оценка {self.name} выше чем у {other.name}")

    def average_grade(self):
        result = 0
        if self.grades:
            for grade in self.grades.values():
                result += sum(grade) // len(grade)
            return result / len(self.grades)
        else:
            return 0

    def __str__(self):
        return (f"Имя:{self.name}\n Фамилия:{self.surname}\n Оценки:{self.grades}\n Средняя оценка за домашние задания:"
                f"{self.average_grade()}\n  Курсы в процессе изучения:{self.courses_in_progress}\n Завершенные курсы:"
                f"{self.finished_courses}\n\n")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}



class Lecturer(Mentor):

    def average_grade(self):
        result = 0
        if self.grades:
            for grade in self.grades.values():
                result += sum(grade) // len(grade)
            return result / len(self.grades)
        else:
            return 0

    def __str__(self):
        return (f"Имя:{self.name}\n Фамилия:{self.surname}\n Оценки от студентов:{self.grades}\n Средняя оценка "
                f"за лекцию:"
                f"{self.average_grade()}\n")

    def __lt__(self,other):
        if self.average_grade() < other.average_grade():
            return (f"Средняя оценка {self.name} ниже чем у {other.name}")
        else:
            return (f"Средняя оценка {self.name} выше чем у {other.name}")



class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student1 = Student('Ruoy', 'Eman', 'woman')
best_student2 = Student('Rick', 'Morty', 'male')
best_student3 = Student('Alf', 'Alfik', 'Ufo')

best_student1.finished_courses += ['First step on Python']
best_student2.finished_courses += ['First step on Python']
best_student3.finished_courses += ['First step on Python']


cool_mentor = Reviewer('Erick', 'Pedigree')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']
cool_mentor.courses_attached += ['CSharp']
cool_mentor.courses_attached += ['Pascal']
cool_mentor.courses_attached += ['C++']

cool_lector = Lecturer('John', 'Snow')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Java']
cool_lector.courses_attached += ['CSharp']
cool_lector.courses_attached += ['Pascal']

cool_lector1 = Lecturer('Luke', 'Skywalker')
cool_lector1.courses_attached += ['Python']
cool_lector1.courses_attached += ['Java']
cool_lector1.courses_attached += ['CSharp']
cool_lector1.courses_attached += ['Pascal']


best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Java']
best_student1.courses_in_progress += ['Pascal']
best_student1.courses_in_progress += ['CSharp']
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Pascal']
best_student2.courses_in_progress += ['CSharp']
best_student3.courses_in_progress += ['Python']
best_student3.courses_in_progress += ['Pascal']
best_student3.courses_in_progress += ['C++']

best_student1.rate_lecturer(cool_lector, 'Python', 6)
best_student2.rate_lecturer(cool_lector, 'Python', 10)
best_student3.rate_lecturer(cool_lector, 'Python', 8)

best_student1.rate_lecturer(cool_lector1, 'Pascal', 7)
best_student2.rate_lecturer(cool_lector1, 'Pascal', 6)
best_student3.rate_lecturer(cool_lector1, 'Pascal', 8)


cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student2, 'Python', 7)
cool_mentor.rate_hw(best_student3, 'Python', 8)

cool_mentor.rate_hw(best_student1, 'Java', 4)
cool_mentor.rate_hw(best_student2, 'CSharp', 3)
cool_mentor.rate_hw(best_student3, 'C++', 10)

cool_mentor.rate_hw(best_student1, 'Pascal', 6)
cool_mentor.rate_hw(best_student2, 'Pascal', 5)
cool_mentor.rate_hw(best_student3, 'Pascal', 9)

print(cool_mentor)
print(best_student1)
print(best_student2)
print(best_student3)
print(cool_lector)
print(cool_lector1)
print(best_student1 < best_student2)
print(best_student1 < best_student3)
print(cool_lector < cool_lector1)
print(cool_lector1 < cool_lector)

