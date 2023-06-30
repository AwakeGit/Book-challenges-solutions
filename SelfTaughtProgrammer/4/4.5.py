# 4.5 Напишите функцию, которая преобразовывает строку в тип данных float и возвращает результат. Используйте
# обработку исключений, чтобы перехватить возможные исключения.

def convert_to_float(string: str) -> float:
    """
    Преобразует строку в тип данных float и возвращает результат.
    :param string: Входная строка.
    :return: Результат преобразования в тип float.
    """
    try:
        result = float(string)
        return result
    except ValueError:
        raise ValueError("Ошибка преобразования строки в тип float.")


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    while True:
        try:
            input_string = input("Введите строку для преобразования: ")
            float_value = convert_to_float(input_string)
            print(f"Результат преобразования: {float_value}")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()
