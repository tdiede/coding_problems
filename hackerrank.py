import sys


# # basic read/write
# print 'enter text you want to echo.'
# s = str(sys.stdin.readline())
# sys.stdout.write(s)


# # # data types
# i = 4
# d = 4.0
# s = 'HackerRank '

# # # Declare second integer, double, and String variables.
# # i2 = int()
# # d2 = float()
# # s2 = str()

# # Read and save an integer, double, and String to your variables.
# print i
# print d
# print s
# print 'enter an integer, a float, and a string to complement the above.'
# i2 = int(sys.stdin.readline())
# d2 = float(sys.stdin.readline())
# s2 = str(sys.stdin.readline())

# # Print the sum of both integer variables on a new line.
# sys.stdout.writelines('%i \n' % (i+i2))

# # Print the sum of the double variables on a new line.
# sys.stdout.writelines('%.1f \n' % (d+d2))

# # Concatenate and print the String variables on a new line
# # The 's' variable above should be printed first.
# sys.stdout.writelines('%s' % (s+s2))


# # enter three lines: meal cost, tip % and tax %
# print 'enter three lines: meal cost as float, tip and tax as integers percent.'
# meal_cost = float(sys.stdin.readline())
# tip_percent = int(sys.stdin.readline())
# tax_percent = int(sys.stdin.readline())

# total_cost = meal_cost + ((tip_percent * meal_cost)/100) + ((tax_percent * meal_cost)/100)

# sys.stdout.write('The total meal cost is %d dollars. \n' % round(total_cost))


# # performs a conditional operation on given integer input
# N = int(raw_input('Enter an integer. >').strip())


# def conditional(n):

#     if n % 2 != 0:
#         sys.stdout.write("Weird \n")
#     else:
#         if n > 20:
#             sys.stdout.write("Not Weird \n")
#         elif n <= 20 and n >= 6:
#             sys.stdout.write("Weird \n")
#         else:
#             sys.stdout.write("Not Weird \n")

# conditional(N)


# # class vs. instance
# class Person:
#     def __init__(self, initialAge):
#         # Add some more code to run some checks on initialAge
#         if initialAge < 0:
#             self.age = 0
#             sys.stdout.write('Age is not valid, setting age to 0. \n')
#         else:
#             self.age = initialAge

#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if self.age < 0:
#             sys.stdout.write('You are young. \n')
#         elif self.age < 13:
#             sys.stdout.write('You are young. \n')
#         elif self.age < 18:
#             sys.stdout.write('You are a teenager. \n')
#         else:
#             sys.stdout.write('You are old. \n')

#     def yearPasses(self):
#         # Increment the age of the person in here
#         self.age += 1


# t = int(raw_input())
# for i in range(0, t):
#     age = int(raw_input())
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print('')


# # loops
# N = int(raw_input().strip())

# i = 1
# for i in range(i, 11):
#     multiple = N * i
#     sys.stdout.write('%i x %i = %i \n' % (N, i, multiple))


# review loops (string)
count = int(sys.stdin.readline())

for line in range(count):
    s = str(sys.stdin.readline()).strip()
    sys.stdout.write('%s %s \n' % ("".join(s[::2]), "".join(s[1::2])))


# arrays
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

seq = ' '.join(map(str, arr[::-1]))

sys.stdout.write('%s' % seq)


# dictionaries/maps/hashmaps
n = int(sys.stdin.readline())

phonebook = {}

i = 0
for entry in range(i, n):
    entry = sys.stdin.readline()
    entry_item = entry.strip().split(' ')
    phonebook[entry_item[0]] = entry_item[1]
    # sys.stdout.write('%s' % phonebook)

loop = True
while loop is True:
    query = sys.stdin.readline()
    if query:
        name = query.strip()
        number = phonebook.get(name, 'Not found')
        if name in phonebook:
            sys.stdout.write('%s=%s \n' % (name, number))
        else:
            sys.stdout.write('%s \n' % (number))
    else:
        loop = False


# recursion
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

N = int(sys.stdin.readline())
factorial = factorial(N)
sys.stdout.write('%i' % factorial)
