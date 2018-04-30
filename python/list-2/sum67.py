"""
Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 7 (every 6 will be followed by at
least one 7). Return 0 for no numbers.
"""

def sum67(nums):
  total = 0
  is_6 = False

  for i in nums:
    if i == 6:
      is_6 = True
    elif not is_6:
      total += i
    elif i == 7:
      is_6 = False

  return total
