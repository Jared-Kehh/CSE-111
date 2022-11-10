# print("hello, i", 21, sep = " am ", end = " bye", flush = True)

# import math
# power = round(17**9 / 3, 1)
# number = power - 6
# if number % 2 == 0:
    # print("True")
# else:
    # print("False")

# def random_math():
    # return (math.ceil(math.pow(17, 9) / 3) - 6) % 2 == 0

# print(random_math())

# import random
# num_list = []

# while len(num_list) < 10:
    # num_list.append(random.randint(0, 20))

# num_list.sort(reverse = True)

# print(num_list)

from datetime import datetime
now = datetime.now()
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "odd minute"

print(display_message)
