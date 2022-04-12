def summary():
    n = 0
    while True:
        listnum = input("Please enter a number, enter 'x' to exit: ").split()
        for num in listnum:
            if num.lower() == "x":
                return n
            else:
                try:
                    n += int(num)
                except ValueError:
                    print("Enter 'x' to exit the program")
        print(f"The summary is: {n}")

print(summary())
