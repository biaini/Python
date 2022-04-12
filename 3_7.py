#Student: Avakian Andranik

def int_func(word):
    latin_char = "qwertyuiopasdfghjklzxcvbnm"
    return word.title() if not set(word).difference(latin_char) else False
words = input("Enter some words separated with spaces: ").split()
for w in words:
    result = int_func(w)
    if result:
        print(result, '')
