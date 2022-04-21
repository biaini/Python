#Student: Avakian Andranik

from sys import argv

def pay():
    try: 
        time, rate, bonus = map(float, argv[1:])
        print(f"The pay is: {time * rate + bonus}")
    except ValueError:
        print("Use only numbers")

pay()
