class Student:

    student_count = 0

    def __init__(self,name,spec):
        self.name = name
        self.spec = spec
        Student.student_count += 1

class Service:
    #classmethod
    name = 'class name'

    def __init__(self):
        self.name = 'object name'

    @staticmethod
    # Декоратор статикметод нужен для того чтобы из метода объекта сделать обычную функцию(отменяя передачу и привязку к параметру self)

    def printed():
        print('static method')


    @classmethod
    # Декоратор классметод нужен для того чтобы из метода объекта сделать метод привязанный к классу(первый параметр такого метода - сам класс)
    def sep(cls,self):
        print(cls.name)
        print(self.name)

s1 = Service()
Service.sep(s1)