#Student: Avakian Andranik

def max_func(dig1, dig2, dig3):
     max_list = [dig1, dig2, dig3]
     try:
         max_list.remove(min(max_list))
         return sum(max_list)
     except TypeError:
        return "Please enter the correct info"

print(max_func(70, -110, 300))
