#Student: Avakian Andranik
import re


class NotNumeric(Exception):
    def __init__(self, text):
        self.text = text


num = re.compile(r'^[-+]?\d+[,.]?\d*$')
result = []

while True:
    try:
        el = input('Enter a list item as a number: ')
        if el.lower() == 'take a break':
            break
        elif num.match(el):
            result.append(el)
        else:
            raise NotNumeric('A number!')
    except NotNumeric as err:
        print(err)
print(result)

