import re

def main():
  clean_input()

def clean_input():
  name = input("What's your name? ").strip()
  # returns (what is here)
  if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
  print(f"Hello, {name}")

main()