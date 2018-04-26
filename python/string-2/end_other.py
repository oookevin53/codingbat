"""
Given two strings, return True if either of the strings appears at the
very end of the other string, ignoring upper/lower case differences
(in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.
"""

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return b.endswith(a) or a.endswith(b)

# Without string method

def end_other(a, b):
    if len(a) > len(b):
        shorter = b.lower()
        longer = a.lower()
    elif len(a) < len(b):
        shorter = a.lower()
        longer = b.lower()
    else:
        shorter = a.lower()
        longer = b.lower()

    return longer[-len(shorter):] == shorter
