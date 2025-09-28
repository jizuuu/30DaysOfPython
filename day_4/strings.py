# Exercise 1 with join()
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))

# Exercise 2 with join()
print(' '.join(['Coding', 'For', 'All'])) 

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

#9

cut_word = 'Coding For All'
coding = cut_word[0:6]
print(coding)

#10

coding_word = "Coding For All"
print(coding_word.index("Coding"))
print(coding_word.find('Coding'))

#11

coding_to_python = "Coding For All"
print(coding_to_python.replace("Coding", "Python"))

#12

everyone_to_all = "Python for Everyone"
print(everyone_to_all.replace('Everyone', 'All'))

#13

split_coding = "Coding For All"
print(split_coding.split(' '))

#14

internet_socials = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(internet_socials.split(', '))

#15

char_index = "Coding For All"
print(char_index[0])

#16

last_index = "Coding For All"
print(last_index[-1])

#17

char_ten = "Coding For All"
print(char_ten[10])

#18

PFE = "Python For Everyone"

#19

CFA = "Coding For All"

#20

print(PFE.index('P'))

#21

print(CFA.index('C'))

#22

CFAP = "Coding For All People"
print(CFAP.rfind('l'))

#23

first_because = "You cannot end a sentence with because because because is a conjunction"
print(first_because.find('because'))

#24

last_because = "You cannot end a sentence with because because because is a conjunction"
print(last_because.rfind('because'))

#25

slice_because = "You cannot end a sentence with because because because is a conjunction"
print(slice_because[30:54])

#26

first_position = "You cannot end a sentence with because because because is a conjunction"

print(first_position.find('because'))

#27

slice_because = "You cannot end a sentence with because because because is a conjunction"
print(slice_because[30:54])

#28

start_substring = "Coding For All"
print(start_substring.find('Coding'))

#29

end_substring = "Coding For All"
print(end_substring.rfind('coding'))

#30

spaces = "   Coding For All      "
print(spaces.strip(' '))

#31

challenge = "30DaysOfPython"
print(challenge.isidentifier())
challenge = "thirty_days_of_python"
print(challenge.isidentifier()) # this returns true

#32

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(python_libraries))

#33

print('I am enjoying this challenge.\nI just wonder what is next.')

#34

challenge = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFindland\tHelsinki'
print(challenge.expandtabs(10))

#35

radius = 10
area = int(3.14 * radius ** 2)
print(f"The area of a circle with radius 10 is {area} meters square.")

#36

x = 8
y = 6

print("%d + %d = %d" %(x, y, x + y))
print("{} - {} = {}".format(x, y, x - y))
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")
print(f"{x} % {y} = {x % y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} ** {y} = {x ** y}")