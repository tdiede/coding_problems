# These are the coding challenges I have worked through.


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
