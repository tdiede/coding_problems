# These are the coding challenges I have worked through.


# medium, below

# # Concepts: Dictionaries, General
# def is_anagram_of_palindrome(word):
#     """Is a word an anagram of a palindrome?
#         >>> is_anagram_of_palindrome("a")
#         True

#         >>> is_anagram_of_palindrome("ab")
#         False

#         >>> is_anagram_of_palindrome("aab")
#         True

#         >>> is_anagram_of_palindrome("arceace")
#         True

#         >>> is_anagram_of_palindrome("arceaceb")
#         False
#     """
#########################################################
########################################################
#     # want to count whether each letter appears an even number of times
#     # one letter can appear an odd number of times

#     # seen = []

#     # i = 0
#     # for i in range(len(word)):
#     #     if word[i] not in seen:
#     #         seen.append(word[i])
#     #     else:
#     #         seen.remove(word[i])

#     # if len(seen) <= 1:
#     #     return True

#     # return False

#     seen = {}

#     i = 0
#     for i in range(len(word)):
#         count = seen.get(word[i], 0) + 1
#         seen[word[i]] = count

#     seen_odd = False

#     for value in seen.itervalues():
#         if value % 2 != 0:
#             if seen_odd:
#                 return False
#             seen_odd = True

#     return True


# # Binary Search
# def binary_search(val):
#     """Using binary search, find val in range 1-100. Return # of guesses.
#         >>> binary_search(50)
#         1

#         >>> binary_search(25)
#         2

#         >>> binary_search(75)
#         2

#         >>> binary_search(31) <= 7
#         True

#         >>> max([binary_search(i) for i in range(1, 101)])
#         7
#     """

#     assert 0 < val < 101, "Val must be between 1-100"

#     num_guesses = 0

#     return num_guesses


# Concepts: Recursion
def count_recursively(lst):
    """Return the number of items in a list, using recursion.
        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3
    """

    if not lst:
        return 0

    lst.pop()
    return count_recursively(lst) + 1


# Concepts: Loops
def decode(s):
    """Decode a string into the original text.
        >>> decode("0h")
        'h'

        >>> decode("2abh")
        'h'

        >>> decode("0h1ae2bcy")
        'hey'
    """

    text = ''

    for idx, char in enumerate(s):
        if char.isdigit():
            letter_index = idx + int(char) + 1
            text += s[letter_index]

    return text


# Concepts: Runtime, General
def missing_number_scan(nums, max_num):
    """Find the missing number in a list.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
        >>> missing_number_scan([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
        8
        >>> missing_number_scan([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
        8
    """

    # my initial solution has potentially terrible runtime!?!
    temp_stack = set()
    idx = 0

    # O(n)
    for idx in range(1, max_num+1):
        temp_stack.add(idx)

    # O(n) to create set from nums, plus O(n) to check between sets
    diff = temp_stack - set(nums)
    (missing,) = diff

    return missing


    # 1st solution, O(n) and requires additional storage:
    # Keep track of what you've seen in a separate list, at False index is missing number.
def missing_number_n_extralist(nums, max_num):

    seen = [False] * max_num

    for n in nums:
        seen[n - 1] = True

    return seen.index(False) + 1


    # 2nd solution, O(n log n) and does not require additional storage:
    # Sort list first, then scan for missing number.
def missing_number_nlogn(nums, max_num):

    nums.append(max_num + 1)
    nums.sort()
    last = 0

    for num in nums:
        if num != last + 1:
            return last + 1
        last += 1

    raise Exception("None are missing!")


    # 3rd solution: find missing number by comparing expected sum vs actual
def missing_number_n(nums, max_num):

    expected = sum(range(max_num + 1))

    # sum of 1..n
    # expected = ( n + 1 ) * ( n / 2 )

    return expected - sum(nums)


# Concepts: General, Math
def print_digits(num):
    """Given an integer, print digits in reverse order, starting with the ones place.
        >>> print_digits(1)
        1
        >>> print_digits(314)
        4
        1
        3
        >>> print_digits(12)
        2
        1
    """

    number = str(num)

    idx = -1

    while abs(idx) <= len(number):
        print number[idx]
        idx += -1


# Concepts: Recursion
def print_recursively(lst):
    """Print items in a list using recursion.
        >>> print_recursively([1, 2, 3])
        1
        2
        3
    """

    if lst:
        print lst[0]
        print_recursively(lst[1:])

print_recursively([1, 2, 3])


# if idx also passed as argument to function...
def print_recursive(lst, idx):

    if idx == len(lst):
        return

    print_recursive(lst, idx+1)

    print lst[idx],

print_recursive([1, 2, 3], 0)


# Concepts: Recursion
def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.
        >>> lst = ['hey', 'there', 'you']
        >>> recursive_index('hey', lst)
        0
        >>> recursive_index('you', lst)
        2
        >>> recursive_index('porcupine', lst) is None
        True
    """

    def _recursive_index(needle, haystack, idx):

        if idx == len(haystack):
            return None

        if haystack[idx] == needle:
            return idx

        return _recursive_index(needle, haystack, idx + 1)

    return _recursive_index(needle, haystack, 0)

#########################################################
########################################################




# Remove Linked List Node
# Remove a node from the start/middle of a linked list.
# Concepts: Linked Lists

# Reverse Linked List
# Reverse a linked list, returning a new list.
# Concepts: Linked Lists

# Sort Sorted Lists
# Merge together two already-sorted lists.
# Concepts: Loops, Sorting

#########################################################
########################################################

# Concepts: Loops, Strings
def split_string(string, delimiter):
    """Split a string on another, like the Python built-in split.
        >>> split_string("i love balloonicorn", " ")
        ['i', 'love', 'balloonicorn']

        >>> split_string("that is which is that which is that", " that ")
        ['that is which is', 'which is that']

        >>> split_string("that is which is that which is that", "that")
        ['', ' is which is ', ' which is ', '']

        >>> split_string("hello world", "nope")
        ['hello world']
    """

    # my initial solution, only works if delimiter is a single character
    # split_string = []
    # prev = 0

    # for idx, char in enumerate(string+delimiter):
    #     if char == delimiter:
    #         split_string.append(string[prev:idx])
    #         prev = idx

    # # split_string.append(string[prev:])

    # return split_string

    split_string = []
    idx = 0

    while idx <= len(string):

        curr_idx = idx
        idx = string.find(delimiter, idx)

        if idx != -1:
            split_string.append(string[curr_idx:idx])
            idx += len(delimiter)

        else:
            split_string.append(string[curr_idx:])
            break

    return split_string


# easier, below

def sum_list(num_list):
    """Return the sum of all numbers in list.
        >>> sum_list([5, 3, 6, 2, 1])
        17
    """

    sum_num = 0

    for num in num_list:
        sum_num += num

    return sum_num


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.
        >>> lst = [1, 2, 3, 4, 6, 8]
        >>> show_evens(lst)
        [1, 3, 4, 5]
    """

    evens = []
    i = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evens.append(i)

    return evens


def rev_string(astring):
    """Return reverse of string.
        >>> rev_string("porcupine")
        'enipucrop'
    """

    i = 0
    rev_string = ""
    for i in range(len(astring)):
        rev_string += astring[-1-i]

    return rev_string


def rev_list_in_place(lst):
    """Reverse list in place.
        >>> lst = [1, 2, 3]
        >>> rev_list_in_place(lst)
        >>> lst
        [3, 2, 1]
    """

    i = 0
    for i in range(len(lst)/2):
        lst[i], lst[-1-i] = lst[-1-i], lst[i]


def pig_latin(phrase):
    """Turn a phrase into pig latin.
        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'

        >>> pig_latin('porcupine are cute')
        'orcupinepay areyay utecay'

        >>> pig_latin('give me an apple')
        'ivegay emay anyay appleyay'
    """

    pig_latin_string = ""
    phrase = phrase.split(" ")

    for word in phrase:

        pig_latin_word = ""

        if word[0] not in ['a', 'e', 'i', 'o', 'u']:
            pig_latin_word = word[1:] + word[0] + 'ay' + ' '
        else:
            pig_latin_word = word + 'yay' + ' '

        pig_latin_string += pig_latin_word

    return pig_latin_string.rstrip(' ')


def max_of_three(num1, num2, num3):
    """Returns the largest of three integers.
        >>> max_of_three(1, 5, 2)
        5

        >>> max_of_three(10, 1, 11)
        11
    """

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    elif num3 >= num1 and num3 >= num2:
        return num3


def max_num(num_list):
    """Returns largest integer from given list.
        >>> max_num([5, 3, 6, 2, 1])
        6
    """

    max_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num

    return max_num


def is_palindrome(word):
    """Return True/False if this word is a palindrome.
        >>> is_palindrome("a")
        True

        >>> is_palindrome("noon")
        True

        >>> is_palindrome("racecar")
        True

        >>> is_palindrome("porcupine")
        False

        >>> is_palindrome("Racecar")
        False
    """

    for i in range(len(word)/2):
        if word[i] != word[-1-i]:
            return False

    return True


def is_prime(num):
    """Is a number a prime number?
        >>> is_prime(0)
        False

        >>> is_prime(1)
        False

        >>> is_prime(2)
        True

        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

        >>> is_prime(11)
        True

        >>> is_prime(999)
        False
    """

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.
        >>> fizzbuzz()
        1
        2
        fizz
        4
        buzz
        fizz
        7
        8
        fizz
        buzz
        11
        fizz
        13
        14
        fizzbuzz
        16
        17
        fizz
        19
        buzz
    """

    i = 1
    while i <= 20:
        if (i % 3 == 0) and (i % 5 == 0):
            print 'fizzbuzz'
        elif (i % 3 == 0):
            print 'fizz'
        elif (i % 5 == 0):
            print 'buzz'
        else:
            print i
        i += 1

fizzbuzz()


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.
        >>> find_range([3, 4, 2, 5, 10])
        (2, 10)

        >>> find_range([43, 3, 44, 20, 2, 1, 100])
        (1, 100)

        >>> find_range([])
        (None, None)

        >>> find_range([7])
        (7, 7)
    """

    min_current = None
    max_current = None

    for item in nums:
        if min_current is None or item < min_current:
            min_current = item
        if max_current is None or item > max_current:
            max_current = item

    return min_current, max_current


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
        # >>> lucky_numbers(2)
        # [3, 7]

        >>> lucky_numbers(0)
        []

        >>> sorted(lucky_numbers(10))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    import random

    nums = range(1, 11)
    lucky_nums = []

    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)

    return lucky_nums


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::
        >>> is_leap_year(1904)
        True

    Except every hundred years::
        >>> is_leap_year(1900)
        False

    Except-except every 400::
        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?
        >>> for i in range(1, 13):
        ...     date = str(i) + " 2016"
        ...     print "%s has %s days." % (date, days_in_month(date))
        1 2016 has 31 days.
        2 2016 has 29 days.
        3 2016 has 31 days.
        4 2016 has 30 days.
        5 2016 has 31 days.
        6 2016 has 30 days.
        7 2016 has 31 days.
        8 2016 has 31 days.
        9 2016 has 30 days.
        10 2016 has 31 days.
        11 2016 has 30 days.
        12 2016 has 31 days.

        >>> days_in_month("02 2015")
        28
    """

    month, year = date.split(" ")
    month = int(month)
    year = int(year)

    thirtyone = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]

    if month in thirtyone:
        days = 31
    elif month in thirty:
        days = 30
    else:
        leap_year = is_leap_year(year)
        if leap_year is True:
            days = 29
        else:
            days = 28

    return days


def concat_lists(list1, list2):
    """Combine lists.
        >>> concat_lists([1, 2], [3, 4])
        [1, 2, 3, 4]

        >>> concat_lists([], [1, 2])
        [1, 2]

        >>> concat_lists([1, 2], [])
        [1, 2]

        >>> concat_lists([], [])
        []
    """

    for item in list2:
        list1.append(item)

    return list1


def add_to_zero(nums):
    """Given list of ints, return True if any two nums in list sum to 0.
        >>> add_to_zero([])
        False

        >>> add_to_zero([1])
        False

        >>> add_to_zero([1, 2, 3])
        False

        >>> add_to_zero([1, 2, 3, -2])
        True

        >>> add_to_zero([0, 1, 2])
        True
    """

    set_nums = set(nums)

    for n in nums:
        if -n in set_nums:
            return True

    return False


#############################################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
