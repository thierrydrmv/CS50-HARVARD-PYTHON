def main():
  student = get_student()
  if student["name"] == "Thierry":
    student["house"] = "🌎"
  print(f"{student["name"]} from {student["house"]}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  # tuple (immutable)
  # return (name, house)
  # list (mutable)
  # return [name, house]
  # dictionary
  return {"name": name, "house": house}

if __name__ == "__main__":
  main()