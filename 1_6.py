#Student: Avakian Andranik

a = float(input("Input the result on the very first day:\n"))
b = float(input("Input the result he wanted to reach after improving his result by 10% each day:\n"))
day = 0
while a < b:
    a = a + (a*0.1)
    day = day +1
    print(f"{a} km")
    if a >= b:
      print(f"He reached the result on {day}th day")
      break
    if a < b:
        continue
