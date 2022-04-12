#Student: Avakian Andranik
#Simple calculator wich can add, multiply, subtract and divide

operand1 = int(input())
operator = input()
operand2 = int(input())

if operator == "+":
    print(operand1+operand2)
if operator == "-":
    print(operand1-operand2)
if operator == "/":
    print(operand1/operand2)
if operator == "*":
    print(operand1*operand2)
