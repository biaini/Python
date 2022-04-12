#Student Avakian Andranik

str = input("Write any sentence:\n").split()

for n, i in enumerate(str, 1):
    print(f"{n}. {i:.10}")
