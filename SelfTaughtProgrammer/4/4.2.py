# 4.2 Создайте функцию, которая принимает строку в качестве параметра и возвращает ее.

def return_string(input_string: str) -> str:
    """
    Возвращает переданную строку.
    :param input_string: Входная строка.
    :return: Входная строка.
    """
    return input_string


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    while True:
        try:
            result: str = input("Введите строку: ").strip()
            if not result:
                raise ValueError("Введена пустая строка.")

            print(return_string(result))
            break

        except ValueError as e:
            print(f"Ошибка ввода: {e}")


if __name__ == '__main__':
    main()
