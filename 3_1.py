#Student Avakian Andranik

def division(divid, divis):    
    try:
        divid = int(divid)
        divis = int(divis)
        div = divid / divis
    except ZeroDivisionError:
        return "You can't divide by zero"
    return int(div) 

print(division(input("Enter the divider: "), input("Enter the division: ")))
