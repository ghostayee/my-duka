class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")
        print(f"Email is: {self.email}")

    def talks(self):
        print("A person talks")

#person1 object
person1 = Person("Alice",20,"alice@gmail.com")
print(type(person1))
person1.display_info()
person1.talks()

#person2 object
person2 = Person("Job",23,"job@outlook.mail")
print(type(person2))
person2.display_info()
person2.talks()