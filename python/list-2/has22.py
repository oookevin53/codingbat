"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
"""

def has22(nums):
    is_2 = False
    for i in nums:
        if is_2:
            if i == 2:
                return True
            is_2 = False
        elif i == 2:
            is_2 = True
    return False
