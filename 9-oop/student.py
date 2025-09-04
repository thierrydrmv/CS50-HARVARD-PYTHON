# classes
# properties -> attributes with more control @property
def main():
    bob = Student.new_student()

    print(bob)
    print(bob.cast_spell())
    print(bob.call_familiar())


class Student:
    # instance method
    def __init__(self, name, house, spell, familiar=""):
        # attributes
        if not name:
            raise ValueError("Missing name")
        self.name = name
        # without the _ even when the object is created pass by the validation on the setter
        self.house = house
        self.spell = spell
        self.familiar = familiar

    # methods __str__ is what will be returned when you call the object as a string
    def __str__(self):
        return f"{self.name} from {self.house}, main spell is: {self.spell}, familiar is a {self.familiar}"

    # Getters
    @property
    def house(self):
        return self._house

    # Setter
    # setter is used to create control about changing a value directly, creating consistency
    @house.setter
    def house(self, house):
        if house == "":
            raise ValueError("House is empty")
        self._house = house

    def cast_spell(self):
        return self.spell

    def call_familiar(self):
        if self.familiar == "bat":
            return "🦇"
        elif self.familiar == "rat":
            return "🐀"
        elif self.familiar == "owl":
            return "🦉"
        else:
            return "🐱"

    @classmethod
    def new_student(cls):
        return cls(
            input("Name: "),
            input("House: "),
            input("Main Spell: "),
            input("Familiar: "),
        )


if __name__ == "__main__":
    main()
