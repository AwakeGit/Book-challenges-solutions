# 3.4 Напишите программу, которая выполняет деление двух чисел и выводит остаток.

def divide_with_remainder(a: int, b: int) -> str:
    """
    Выполняет деление двух чисел и возвращает частное и остаток.
    :param a: Делимое число.
    :param b: Делитель.
    :return: Строку, содержащую результат деления (частное) и остаток.
    """

    quotient: int = a // b
    remainder: int = a % b

    return f"Частное: {quotient}, \nОстаток: {remainder}."


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    while True:
        try:
            a_input: str = input("Введите делимое число: ")
            b_input: str = input("Введите делитель: ")

            if a_input.isdigit():
                a = int(a_input)
            else:
                raise ValueError("Только цифры")

            if b_input.isdigit():
                b = int(b_input)
            else:
                raise ValueError("Только цифры")

            break
        except ValueError as v_error:
            print(f"Ошибка ввода: {v_error}")

    print(divide_with_remainder(a, b))


if __name__ == '__main__':
    main()
