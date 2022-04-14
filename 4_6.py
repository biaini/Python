#Student: Avakian Andranik

from itertools import count, cycle

count_list = count(7)
cycle_list = cycle("=#@")

for _ in range(5):
    print("(count_list, cycle_list) = ({},{})".format(next(count_list), next(cycle_list)))
