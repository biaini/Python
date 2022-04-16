#Student: Avakian Andranik

n = list(input("Enter number of the list elements:\n"))
for i in range(1, len(n), 2):
    n[i - 1], n[i]=n[i], n[i-1]
print(n)

