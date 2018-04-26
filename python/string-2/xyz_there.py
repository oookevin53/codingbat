"""
Return True if the given string contains an appearance of "xyz" where the xyz
is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
"""

def xyz_there(str):
    count_xyz = str.count("xyz")
    count_periods = str.count(".xyz")

    return True if count_xyz > count_periods else False
