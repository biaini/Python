#Student: Avakian Andranik

def factorial_num(num):
    factnum = 1
    for i in range (num +1):
        yield f'{i}! = {factnum}'
        factnum *= i +1 
for el in factorial_num(int(input("Add any number: "))):
    print(el)
