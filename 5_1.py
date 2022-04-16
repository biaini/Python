#Student: Avakian Andranik

with open('lesson5_1.txt', 'w', encoding='utf-8') as f:
        while True:
            line = input('Add a string: ')
            if not line:
                break
            print(line, file=f)
