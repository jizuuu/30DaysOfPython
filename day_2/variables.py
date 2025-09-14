# Day 2: 30 Days of python programming

# -----------------------------------
# Exercises: Level 1
# -----------------------------------
first_name = "King Gio"
last_name = "Visoria"
full_name = first_name + ' ' + last_name
country = "Philippines"
city = "Somewhere"
age = 250
year = 2002
is_married = False
is_true = True
is_light_on = False

# multiple variables in one line
ear_phones, monitor, mouse = 'tangzu', 'gamdias', 'M700A'

# -----------------------------------
# Exercises: Level 2
# -----------------------------------

# check data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

if len(first_name) == len(last_name):
  print("Equal")
else:
  print("Not Equal")

# arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_two * num_one
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

# circle calculations
radius = 30
area_of_circle = 3.14 * radius**2
circum_of_circle = 2 * 3.14 * radius

print("Area with radius 30:", area_of_circle)
print("Circumference with radius 30:", circum_of_circle)

# user input for radius
radius = float(input("Enter radius: "))
area_of_circle = 3.14 * radius**2
print("Area with user radius:", area_of_circle)

# user input for personal info
first_name = str(input("Enter your first name: "))
print(first_name)

last_name = str(input("Enter your last name: "))
print(last_name)

country = str(input("Country: "))
print(country)

age = int(input("Age: "))
print(age)

# check Python reserved keywords
help('keywords')