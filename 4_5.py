#Student: Avakian Andranik

from functools import reduce

def mltpl_func(ind1, ind2):
    return ind1 * ind2

mltpl_list = [num for num in range(100, 1001, 2)]
print(f"Source list\n{mltpl_list}\n Multiplicated list\n{reduce(mltpl_func, mltpl_list)}")
