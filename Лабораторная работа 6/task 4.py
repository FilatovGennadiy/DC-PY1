import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename, encoding='utf-8') as file:  # TODO реализовать конвертер из csv в json
        data = []  # Список для форматирования из текстового формата в вид списка

        for line_ in file:
            data.append([x.rstrip(new_line) for x in
                         line_.split(delimiter)])  # Разделяем строки на элементы и помещаем в список

    list_of_dict = []  # Список для итогового списка словарей

    for i in range(1, len(data)):
        new_dict = {}  # Создаём словарь для i-й строки

        for j in range(len(data[0])):
            new_dict.update({data[0][j]: data[i][j]})  # Добавляем новые сочетания в словарь для строки

        list_of_dict.append(new_dict)  # Добавляем строку в новый список

    return list_of_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
