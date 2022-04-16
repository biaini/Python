#Student: Avakian Andranik

with open("wcount5_2.txt", "r", encoding='utf-8') as f_obj:
    wcount = [f'{line}. {count.strip()} - {len(count.split())} words'
        for line, count in enumerate(f_obj, 1)]
    print(*wcount, f"Total strings: {len(wcount)}.", sep="\n")
