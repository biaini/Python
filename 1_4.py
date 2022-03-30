#Student: Avakian Andranik
#Find the maximum digit of the number

intnum = int(input("Input any integer number:\n"))
maxnum = 0
num = intnum

while num > 0:
  digit = num % 10
  if digit > maxnum:
    maxnum = digit
    if maxnum == 9:
      break
  num = num // 10

print(f"The greatest digit in {intnum} is {maxnum}")
