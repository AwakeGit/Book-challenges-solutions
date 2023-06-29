# 3.1 Выведите три различные строки.

def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    fields = [
        ("Введите строку 1: ", "str_one"),
        ("Введите строку 2: ", "str_two"),
        ("Введите строку 3: ", "str_three")
    ]

    data = {}
    is_valid = False

    while not is_valid:
        for prompt, var_name in fields:
            while True:
                value = input(prompt)
                if not value:
                    print("Поле не может быть пустым")
                elif value.isdigit():
                    print("Введена только цифра")
                else:
                    data[var_name] = value
                    break

        is_valid = True

    print("Все данные введены корректно.")
    print("Результаты ввода:")
    for var_name, value in data.items():
        print(f"{var_name}: {value}")


if __name__ == '__main__':
    main()
