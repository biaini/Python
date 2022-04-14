#Sudent: Avakian Andranik

def int_func():
    for word in input("Enter lower case latin letters words:\n ").split():
        letters = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                letters += 1
        print(word.title() if letters == len(word) else f"{word} type lower case letters")

int_func()
