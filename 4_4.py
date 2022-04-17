Student: Avakian Andranik

from random import *

random_list = [randint(-10,10) for _ in range(20)]
unique_list = [num for num in random_list if random_list.count(num) == 1]
print(f"Random list\n{random_list}\n Unique list\n{unique_list}")
