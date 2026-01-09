# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    result += ("*" * n)
    result += "\n"
    for i in range(n-2):
        result += ( "*" + (n-2) * " " + "*")
        result += "\n"
    if not(n == 1):
        result += ("*" * n)
    return result.rstrip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(n):
        count = 1
        for k in range( i + 1):
            result += str(count)
            count += 1
        result += "\n"
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
# Example for n = 4:
#    *def sum_of_natural_numbers(n):
def sum_of_natural_numbers(n):
    result = 0
    count = 1
    while (n >= count):
            result += count
            count += 1
    return result
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    result += (n - 1) * " "
    result += "*"
    result += "\n"
    for i in range(n - 1):
        result += " " * (n - i -2)
        result += "*" * ((i + 1) * 2 + 1)
        result += "\n"
    return result.rstrip()
