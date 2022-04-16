#Student Avakian Andranik


month = int(input("Enter the number of the month:\n"))
month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "Dectember"}
season_dict = {"Winter": [12, 1, 2], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
#if month in month_dict:
if month in sum(season_dict.values(),[]):
    for i in season_dict.items():
        if month in i[1]:
            print(f"{month} month of the year is {month_dict[month]} and it's {i[0]}")
            break
else:
    print("There's no such a month!")
