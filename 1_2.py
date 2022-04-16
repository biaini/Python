#Student: Avakian Andranik
#Convert seconds into the hours, minutes and seconds using this format hh:mm:ss

sec = int(input())
hours = sec // 3600
remain = sec - (3600*hours)
minutes = remain // 60

if remain < 60:
    seconds = sec - (3600*hours)
    print(f"{hours}:{minutes}:{seconds}")
if remain >= 60:
    seconds = remain - (60*minutes)
    print(f"{hours}:{minutes}:{seconds}")
