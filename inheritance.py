class Animal:
    def __init__(self,name):
        self.name = name


    def make_sound(self):
        print(f"{self.name} makes sound!!")


class Dog(Animal):
    def make_sound(self):
        return super().make_sound()

class Horse(Animal):
    def make_sound(self):
        return super().make_sound()





















class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def works(self):
        print(f"{self.name} works!!")


class Teacher(Person):
    def works(self):
        print(f"{self.name} Works!!")


class Student(Person):
    def works(self):
        print(f"{self.name} studies")

t1 = Teacher("Joy",34)
