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
m = 2
b = -2

y_intercept = (0, b)

x = (0 - b) / m
x_intercept = (x, 0)

print("Slope:", m)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

x1, y1 = 2, 2
x2 , y2 = 6, 10

# slope formula
m = (y2 - y1) / (x2 - x1)

# euclidean distance formula
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", m)
print("Euclidean Distance:", d)