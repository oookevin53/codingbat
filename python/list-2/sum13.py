"""
Return the sum of the numbers in the array, returning 0 for an empty
array. Except the number 13 is very unlucky, so it does not count and
numbers that come immediately after a 13 also do not count.
"""

def sum13(nums):
    idx_after = 0
    for idx, i in enumerate(nums):
        if i == 13:
            i = 0
            idx_after = idx + 1
