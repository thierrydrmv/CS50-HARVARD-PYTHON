import random

class Rh:
  # class variable, bind to the class, not instances
  positions = ["Sales", "Programming", "Rh", "Manager"]

  # bind to the class, not instances
  @classmethod
  def sort(cls, name):
    position = random.choice(cls.positions)
    return f"{name} is hired in {position}"

print(Rh.sort("Bob"))