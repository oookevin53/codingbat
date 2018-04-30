"""
Return the sum of the numbers in the array, returning 0 for an empty
array. Except the number 13 is very unlucky, so it does not count and
numbers that come immediately after a 13 also do not count.
"""

def sum13(nums):
  total = 0
  for i in range(len(nums)):
    if nums[i] != 13:
      if i == 0 or nums[i-1] != 13:
        total += nums[i]
  return total
