from random import randint


def get_unique_list_numbers() -> list[int]:
    start = -10
    end = 10
    count = 15
    random_values = []
    while len(random_values) != count:
        value = randint(start, end)
        if value not in random_values:
            random_values.append(value)

    return random_values


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
