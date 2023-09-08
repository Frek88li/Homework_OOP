from statistics import mean


class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

        
    def lectures(self, lecturs, course, grade): # выставляем оценки лекторам.
            if isinstance(lecturs, Lecturer) and course in lecturs.courses_attached \
        and course in self.courses_in_progress:
                if course not in lectur1.marks:
                    lecturs.marks[course] = [grade]
                else:
                    lecturs.marks[course].append(grade)
            else:
                return "Ошибка"
            
    def average_marks(self): # Находим среднюю оценку по курсам.
        sum_grades = 0
        count_grades = 0
        for lst in self.grades.values():
            sum_grades = sum(lst)
            count_grades = len(lst)
            if count_grades != 0:
                resul = sum_grades / count_grades
                return round(resul, 1)
            else:
                return None

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
            f"Средняя оценка: {self.average_marks()}\n"
            f"Курсы в процессе изучения: {self.courses_in_progress}\n"
            f"Завершенные курсы: {self.finished_courses}")

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.average_marks() == other.average_marks()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.average_marks() < other.average_marks()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    


class Lecturer(Mentor):
    lecturers_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks = {}
        Lecturer.lecturers_list.append(self)


    def average_marks(self):
        sum_marks = 0
        count_marks = 0
        for lst in self.marks.values():
            sum_marks = sum(lst)
            count_marks = len(lst)
            if count_marks != 0:
                resul = sum_marks / count_marks
                return round(resul, 1)
            else:
                return None

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_marks()}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.average_marks() == other.average_marks()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.average_marks() < other.average_marks()


        

class Reviewer(Mentor):
    """Класс ментора выставляет оценки студентам"""
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка, неверный ввод данных!')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



def average_studentmarks_for_cours(students: list, cours: str):
    count = 0
    summ = 0
    for student in students:
        if not isinstance(student, Student):
            raise TypeError('Список должен содержать только объекты типа "Student"')
        if cours in student.grades:
            summ += mean(student.grades[cours])
            count += 1
    return round(summ / count, 1)

def average_lectormarks_for_cours(lecturers: list, cours: str):
    count = 0
    summ = 0
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer):
            raise TypeError('Список должен содержать только объекты типа "Lecturer"')
        if cours in lecturer.marks:
            summ += mean(lecturer.marks[cours])
            count += 1
    return round(summ / count, 1)




student1 = Student('Rudy', 'Eman', 'male')
student2 = Student("Entony", "Bayden", "male") 
reviewer1 = Reviewer("Bob", "Hatson")
reviewer2 = Reviewer("Nika", "Jordan")
lectur1 = Lecturer("Stiv", "Jobs")
lectur2 = Lecturer("Mark", "Zuckerberg")

student1.courses_in_progress += ['Python', "Git"]  # добавляем курс 
student2.courses_in_progress += ["Python"]

student1.finished_courses.append("Python")  # добавляем финальный курс 
student2.finished_courses.append("Python")

lectur1.courses_attached += ["Python"]   # добавляем курс 
lectur2.courses_attached += ["Python", "Git"]

reviewer1.courses_attached += ["Python"]
reviewer2.courses_attached += ["Python", "Git"]

student1.lectures(lectur2, "Python", 9)
student1.lectures(lectur2, "Python", 8)  # добавляем  оценки лекторам
student1.lectures(lectur2, "Python", 5)

print(lectur2)
print()
student2.lectures(lectur1, "Python", 8)
student2.lectures(lectur1, "Python", 5)
student2.lectures(lectur1, "Python", 2)

print(lectur1)
print()
reviewer1.rate_hw(student2, "Python", 3)
reviewer1.rate_hw(student2, "Python", 3)  # добавляем  оценки студентам
reviewer1.rate_hw(student2, "Python", 8)
reviewer1.rate_hw(student2, "Python", 4)
reviewer1.rate_hw(student2, "Python", 3)
reviewer2.rate_hw(student1, "Git", 5)
reviewer2.rate_hw(student1, "Git", 6)
reviewer2.rate_hw(student1, "Git", 8)
reviewer2.rate_hw(student1, "Python", 3)
reviewer2.rate_hw(student1, "Python", 4)


print(student2)
print()



print(student1 == student2)
print(student1 < student2)  
print(lectur1 == lectur2)
print(lectur1 < lectur2)



reviewer1 = Reviewer('Adam', 'Sendler')
reviewer2 = Reviewer('Nicol', 'Kidman')
reviewer1.courses_attached = ['Python', 'Django', 'Flask', 'React']
reviewer2.courses_attached = ['Python', 'Django', 'Flask', 'React', 'API']
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 5)
print(student1.grades)
print(student2.grades)
print(student1)
print(student2)
print(student1 == student2)
print(student1 < student2)

student3 = Student('Jeff', 'Bezos', 'male')
student3.courses_in_progress = ['Python', 'Django', 'Flask', 'React', 'Sql', 'API']
reviewer2.rate_hw(student3, 'API', 2)
reviewer2.rate_hw(student3, 'Django', 3)
reviewer2.rate_hw(student3, 'Python', 3)
reviewer2.rate_hw(student3, 'Python', 2)

print(student1.grades)
print(student2.grades)
print(student3.grades)
print(average_studentmarks_for_cours(Student.student_list, 'Python'))

print(lectur1.marks)
print(lectur2.marks)
print(average_lectormarks_for_cours(Lecturer.lecturers_list, 'Python'))













