import math


age = 250
height = 1.73
complex = 1 + 1j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = int(0.5 * base * height)
print(f'The area of the triangle is {area}')

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}')

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

radius = float(input("Enter the radius of a circle: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius

print(f"Area: {area}")
print(f"Circumference: {circumference}")

# y = mx + b
slope_eq = 2
b = -2

y_intercept = (0, b)

x = (0 - b) / slope_eq
x_intercept = (x, 0)

print("Slope:", slope_eq)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

x1, y1 = 2, 2
x2 , y2 = 6, 10

# slope formula
slope_pts = (y2 - y1) / (x2 - x1)

# euclidean distance formula
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", slope_pts)
print("Euclidean Distance:", d)

if slope_eq == slope_pts:
  print("The Slopes are equal")
else:
  print("The Slopes are not equal")

x = [-3, 2, 3, 4, 5]

for i in range(len(x)):
  y = x[i]**2 + 6 * x[i] + 9
  if y == 0:
    print(x[i])

word_one = "python"
word_two = "dragon"

print(len(word_one) != len(word_two))

# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# n**1 n n**1 n**2 n**3

num = int(input("Enter a number: "))
for num in range(1, 6):
  print(f"{num:<5}{1:<5}{num:<5}{num**2:<5}{num**3:<5}")