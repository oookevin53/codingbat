"""
Given 3 int values, a b c, return their sum. However, if one of the values
is the same as another of the values, it does not count towards the sum.
"""

def lone_sum(a, b, c):
  total = 0
  
  if a != b and a != c:
    total += a

  if b != a and b != c:
    total += b

  if c != a and c != b:
    total +=c

  return total
