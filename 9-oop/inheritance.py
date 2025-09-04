class Person:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Name is missing")
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, material):
        super().__init__(name, age)
        self.material = material

    ...


class Professor(Student):
    def __init__(self, name, age, material, subject):
        super().__init__(name, age, material)
        self.subject = subject

    ...


person = Person("Angelo", 19)
student = Student("Bob", 22, "Pen and paper")
professor = Professor("Kobe", 44, "Whiteboard", "Science")
