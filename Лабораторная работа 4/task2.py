def get_count_char(str_):
    dict = {}
    str_ = str_.lower()
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    for letter in str_:
        count = 0
        if letter.isalpha():
            for i in str_:
                if letter == i:
                    count += 1
            dict[letter] = count
    return dict

def get_procent_char(str_):
    dict = {}
    str_ = str_.lower()
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    for letter in str_:
        str_ = ' '.join(str_.split(' '))
        count = 0
        if letter.isalpha():
            for i in str_:
                if letter == i:
                    count += 1
            dict[letter] = round(count*100/len(str_), 2)
    return dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))