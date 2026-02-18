x = "hello world"
print(x.upper())
print(type(x))


class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


dee = Dog("ghost",34)
print(dee.get_name())
dee2 = Dog("lenny",24)
print(dee2.get_name())
