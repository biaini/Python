#Student: Avakian Andranik

from random import randint

with open("nums5_5.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

print(f"The summary: {sum(my_list)}")
