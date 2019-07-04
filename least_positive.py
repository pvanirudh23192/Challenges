# The input:
# "[-46.41, -55.11, 40.64]"
# should return: 40.64
#
#
# The input:
# "[-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]"
# should return: 39.82
#
#
# The input:
# "[-3.53, -56.3, 11.17, -25.21, 96.21, -44.62, 94.95, 65.85, 26.79, -88.16]"
# should return: 11.17


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    least = None
    act_least = 0
    l = len(in_list)
    for number in in_list:
        if number > 0:
            if least == None or number < least:
                least = number
    return least



# Test cases

print(smallest_positive([-46.41, -55.11, 40.64]))
# Correct output: 2

print(smallest_positive([-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]))
# Correct output: 0.2
