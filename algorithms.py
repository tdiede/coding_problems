# These are the coding challenges I have worked through.


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


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
        >>> lucky_numbers(2)
        [3, 7]

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


=======
>>>>>>> fbcd4a73a275063c166f026347520731e52ebfe9
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
