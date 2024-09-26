#1
"""
Создайте класс Student, который будет представлять студента университета. 
У студента должны быть следующие атрибуты: name, age, major и gpa. Атрибут 
gpa должен иметь значение по умолчанию равное 0.

Также добавьте метод get_info, который будет выводить информацию о студенте 
в виде строки в следующем формате: "Имя: {имя}, Возраст: {возраст}, Специальность: 
{специальность}, Средний балл: {средний_балл}".
"""

#2
"""
Добавьте в предыдущее задание класса Student новый метод strip_code, который 
будет удалять все цифры из имени студента.
"""

#3
"""
Дополните предыдущее задание с классом Student, создав новый класс GraduateStudent, 
который будет наследоваться от класса Student. В классе GraduateStudent также 
должен быть определен конструктор, который будет вызывать конструктор родительского 
класса Student, чтобы установить имя, возраст, специальность и средний балл для 
выпускника.
"""

#4
"""
Добавьте возможность переопределения методов в классе GraduateStudent, чтобы 
ученики могли переопределять метод get_info(), добавляя дополнительную 
информацию к выводу.
"""

import re


class Student:
    def strip_code(self):
        return re.sub(r'[^\w\s]+|[\d]+', r'', self.name).strip()
    #or
    def strip_code(self):
        return ''.join(filter(str.isalpha, self.name))
    
    def __init__(self, name, age, major, gpa=0):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Специальность: {self.major}, Средний балл: {self.gpa}"
    
class GraduateStudent(Student):
    def __init__(self, name, age, major, gpa, education_level):
        super().__init__(name, age, major, gpa)
        self.education_level = education_level

    def get_info(self):
        return f"{super().get_info()}, Уровень образования: {self.education_level}"
    
    




"""
Создайте три класса: Rectangle, Circle и Triangle. Все эти классы 
должны иметь метод area, который будет возвращать площадь фигуры.
"""

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (3.14 * (r**2))

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        a = self.a
        b = self.b
        c = self.c
        p = (a + b + c)/2
        return ((p * (p - a) * (p - b) * (p - c))^0.5)