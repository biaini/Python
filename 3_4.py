def randomf(x,y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Try to enter the correct information:\n"
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f"Raising x to the y  power is: {round(result, 6)}"
    except ValueError:
        return "You should add the correct number"

number1 = input("Add the number x:")
number2 = input("Add the number y:")

print(randomf(number1, number2))
