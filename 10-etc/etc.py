def main():
  set() # -> list without replicates

def set_list(items):
  new_list = set()
  for item in items:
    # for set the add method is used
    new_list.add(item["age"])
  return new_list

animals = [
  {"name": "sofia", "age": 1},
  {"name": "lua", "age": 5},
  {"name": "kajit", "age": 1},
  {"name": "galileu", "age": 12}
]

print(set_list(animals))


if __name__ == "__main__":
  main()