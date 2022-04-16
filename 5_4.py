#Student: Avakian Andranik

rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("ruseng5_4_2.txt", "w", encoding='utf-8') as new_file:
    with open("ruseng5_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])

