"""
Given a string, return a string where for every char in the original, there are two chars.
"""

def double_char(str):
    final = ""
    for i in str:
        final += i * 2
    return final
