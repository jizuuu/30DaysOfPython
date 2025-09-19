import math

# === Basic Variables ===
age = 250
height = 1.73
complex_num = 1 + 1j

# === Triangle Area ===
base = float(input('Enter base: '))
user_height = float(input('Enter height: '))
area = 0.5 * base * user_height
print(f'The area of the triangle is {area}')

# === Triangle Perimeter ===
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}')

# === Rectangle Area & Perimeter ===
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# === Circle Area & Circumference ===
radius = float(input("Enter the radius of a circle: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"Area: {area}")
print(f"Circumference: {circumference}")

# === Line Equation (y = mx + b) ===
slope_eq = 2
b = -2
y_intercept = (0, b)
x = (0 - b) / slope_eq
x_intercept = (x, 0)
print("Slope:", slope_eq)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

# === Slope & Euclidean Distance ===
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_pts = (y2 - y1) / (x2 - x1)
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope:", slope_pts)
print("Euclidean Distance:", d)
if slope_eq == slope_pts:
  print("The Slopes are equal")
else:
  print("The Slopes are not equal")

# === Quadratic Equation Roots (y = x^2 + 6x + 9) ===
x = [-3, 2, 3, 4, 5]
for i in range(len(x)):
  y = x[i]**2 + 6 * x[i] + 9
  if y == 0:
    print(x[i])

# === String Lengths & Substrings ===
word_one = "python"
word_two = "dragon"
print(len(word_one) != len(word_two))

if "on" in word_one and "on" in word_two:
  print("Both words have 'on' word.")
else:
  print("Both words have no word.")

course_text = "I hope this course is not full of jargon"
if "jargon" in course_text:
  print("The text has 'jargon'.")
else:
  print("The text does not have 'jargon'.")

word1 = "dragon"
word2 = "python"
if "on" not in word1 and "on" not in word2:
  print("There is no 'on' in both dragon and python.")
else:
  print("There is 'on' in one or both words.")

# === Type Conversions ===
text = "python"
text_float = float(len(text))
print(type(text_float))
text_string = str(text_float)
print(text_string)
print(type(text_string))

# === Divisibility Check ===
num_input = int(input("Enter a number: "))
if num_input % 2 == 0:
  print(f"The number {num_input} is divisible by 2.")
else:
  print(f"The number {num_input} is not divisible by 2.")

# === Floor Division Check ===
floor = 7 // 3
converted_floor = 2.7
if floor == int(converted_floor):
  print("Both are the same value.")
else:
  print("Both are not the same value.")

# === Type Comparison ===
num_str = '10'
num = 10
if type(num_str) == type(num):
  print("The number type is equal.")
else:
  print("The number type is not equal.")

num_float = 9.8
num = 10
if int(num_float) == num:
  print("The number type is equal.")
else:
  print("The number type is not equal.")

# === Weekly Earnings ===
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# === Seconds Lived ===
number_years = int(input("Enter number of years you have lived: "))
seconds = number_years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds")

# === Table Pattern ===
for num in range(1, 6):
  print(f"{num:<5}{1:<5}{num:<5}{num**2:<5}{num**3:<5}")