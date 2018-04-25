"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""

def string_splosion(str):
    final = ""
    for i in range(len(str)):
        final += str[:i+1]
    return final
