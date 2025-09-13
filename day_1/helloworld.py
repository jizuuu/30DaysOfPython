import math

print("Addition(+):", 3 + 4)
print("Subtraction(-):", 4 - 3)
print("Multiplication(*):", 4 * 3)
print("Modulus(%):", 3 % 4)
print("Division(/):", 4 / 2)
print("Exponential(**):", 4 ** 2)
print("Floor Division Operator(//):", 4 // 3) 
print()
name = "Gio"
family_name = "Visoria"
country = "Philippines"

print(f"My name is: {name}")
print(f"My family name is: {family_name}")
print(f"My country: {country}")
print("I am enjoying 30 days of python\n")

# Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Gio"))
print(type("Visoria"))
print(type("Philippines"))
print()
# Example of different python data types:

# Number:
integer_num = 1
float_num = 3.14
complex_num = 1 + 2j

# String:
text = "Hello, Python!"

# Boolean:
is_Alive = True

# List:
perfumes = ['Dior Sauvage', 'Nautica Voyage', 'SWYI']

# Tuple:
tuples = (3, 2 , -5)

# Set:
numbers = {1, 2, 3, 4, 5}

# Dictionary:
person = {
  "name": 'Gio',
  "age": 21,
  "country": 'Philippines',
}

print(integer_num, float_num, complex_num)
print(text)
print(is_Alive)
print(perfumes)
print(tuples)
print(numbers)
print(person)
print()
# Euclidean Distance:
x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance}")