import sys


# basic read/write
print 'enter text you want to echo.'
s = str(sys.stdin.readline())
sys.stdout.write(s)


# # data types
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i2 = int()
d2 = float()
s2 = str()

# Read and save an integer, double, and String to your variables.
print i
print d
print s
print 'enter an integer, a float, and a string to complement the above.'
i2 = int(sys.stdin.readline())
d2 = float(sys.stdin.readline())
s2 = str(sys.stdin.readline())

# Print the sum of both integer variables on a new line.
sys.stdout.writelines('%i \n' % (i+i2))

# Print the sum of the double variables on a new line.
sys.stdout.writelines('%.1f \n' % (d+d2))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
sys.stdout.writelines('%s' % (s+s2))


# enter three lines: meal cost, tip % and tax %
print 'enter three lines: meal cost as float, tip and tax as integers percent.'
meal_cost = float(sys.stdin.readline())
tip_percent = int(sys.stdin.readline())
tax_percent = int(sys.stdin.readline())

total_cost = meal_cost + ((tip_percent * meal_cost)/100) + ((tax_percent * meal_cost)/100)

sys.stdout.write('The total meal cost is %d dollars. \n' % round(total_cost))


# performs a conditional operation on given integer input
N = int(raw_input('Enter an integer. >').strip())


def conditional(n):

    if n % 2 != 0:
        sys.stdout.write("Weird \n")
    else:
        if n > 20:
            sys.stdout.write("Not Weird \n")
        elif n <= 20 and n >= 6:
            sys.stdout.write("Weird \n")
        else:
            sys.stdout.write("Not Weird \n")

conditional(N)


