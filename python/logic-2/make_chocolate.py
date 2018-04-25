"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each)
and big bars (5 kilos each). Return the number of small bars to use, assuming we
always use big bars before small bars. Return -1 if it can't be done.
"""

def make_chocolate(small, big, goal):

    # check if enough chocolate in the first place
    if goal > big * 5 + small or goal % 5 > small:
        return -1

    # if enough, figure out how many big is needed then small
    elif goal // 5 > big:
        return goal - big * 5

    return goal - (goal // 5) * 5
