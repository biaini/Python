#Student: Avakian Andranik

with open('pay5_3.txt', 'r', encoding='utf-8') as f:
    empl ={line.split()[0]: float(line.split()[1]) for line in f}
print(f'Average pay: {round(sum(empl.values()) / len(empl), 3)}\n'
     f'Pay less than 20 000$ {[e[0] for e in empl.items() if e[1] < 20000]}')
