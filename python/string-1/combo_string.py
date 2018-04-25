"""
Given 2 strings, a and b, return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).
"""

def combo_string(a, b):
    return "{}{}{}".format(a,b,a) if len(a) < len(b) else "{}{}{}".format(b,a,b)
