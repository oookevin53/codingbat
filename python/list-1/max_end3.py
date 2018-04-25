"""
Given an array of ints length 3, figure out which is larger, the
first or last element in the array, and set all the other elements
to be that value. Return the changed array.
"""

def max_end3(nums):
    return [nums[-1]] * 3 if nums[-1] > nums[0] else [nums[0]] * 3
