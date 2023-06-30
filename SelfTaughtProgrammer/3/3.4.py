# 3.4 Напишите программу, которая выполняет деление двух чисел и выводит остаток.

def divide_with_remainder(a: float, b: float) -> str:
    """
    Выполняет деление двух чисел и возвращает частное и остаток.
    :param a: Делимое число.
    :param b: Делитель.
    :return: Строку, содержащую результат деления (частное) и остаток.
    """

    quotient: float = a // b
    remainder: float = a % b

    return f"Частное: {quotient}, \nОстаток: {remainder}."


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    while True:
        try:
            a_input: str = input("Введите делимое число: ")
            a = float(a_input)

            b_input: str = input("Введите делитель: ")
            b = float(b_input)

            break
        except ValueError:
            print("Ошибка ввода: Введите корректное число.")

    print(divide_with_remainder(a, b))


if __name__ == '__main__':
    main()
