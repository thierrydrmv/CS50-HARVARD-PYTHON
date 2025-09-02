class Bank:
  def __init__(self, name, gold=0, silver=0, brass=0):
    self.name = name
    self.gold = gold
    self.silver = silver
    self.brass = brass

  def __str__(self):
    return f"{self.name} has: {self.gold} Golds, {self.silver} Silvers, {self.brass} Brasses"

  # operator overloading - recreating sum
  def __add__(self, other):
    gold = self.gold + other.gold
    silver = self.silver + other.silver
    brass = self.brass + other.brass
    return f"New Bank has: {gold} Golds, {silver} Silvers, {brass} Brasses"

bob = Bank("Bob", 1, 12, 399)

tomy = Bank("Tomy", 122, 3041, 21333)

total = bob + tomy

print(bob)
print(tomy)

print(total)