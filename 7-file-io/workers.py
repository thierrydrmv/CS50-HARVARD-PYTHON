import csv

def main():
  # write_csv("workers.csv")
  open_csv("workers.csv")

def open_csv(path):
  workers = []
  with open(path) as file:
    reader = csv.DictReader(file)
    for row in reader:
      workers.append(row)
      # workers.append({ "name": row["name"], "position": row["position"], "age": row["age"] })
  print(workers)

def write_csv(path):
  name = input("What's your name? ")
  position = input("What you do? ")
  age = input("What's your age? ")
  with open(path, "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "position", "age"])
    writer.writerow({"name": name, "position": position, "age": age})

main()