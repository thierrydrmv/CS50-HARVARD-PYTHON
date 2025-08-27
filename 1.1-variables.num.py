print(2 ** 5) # 32
print(21 // 5) # integer division 4
print(21 / 5) # pointer division 4.2
print(11 % 5) # module 1

# user input is always a text str, you need to convert to number to sum
print(int("12") + 3)

x = float(input("Write a number to x: "))
y = float(input("Write a number to y: "))


z = round(x + y, 2)

print(z) # 22222.75

# float -> has a decimal point value
# round -> round to the nearest integer

# -> especify commas/points

print(f"{z:,}") # 22,222.75

print(f"{z:.2f}") # two digits after point 22222.75