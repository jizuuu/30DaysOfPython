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