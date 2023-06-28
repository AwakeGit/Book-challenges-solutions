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

    try:
        a_input: str = input("Введите делимое число: ")
        b_input: str = input("Введите делитель: ")

        if not a_input.isdigit() or not b_input.isdigit():
            raise ValueError("Введено некорректное значение. Ожидаются целые числа.")

        a: int = int(a_input)
        b: int = int(b_input)

        if a == 0:
            raise ZeroDivisionError("Делимое не может быть нулем.")
        elif b == 0:
            raise ZeroDivisionError("Делитель не может быть нулем.")
        elif not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Введено некорректное значение. Ожидаются целые числа.")
        else:
            print(divide_with_remainder(a, b))

    except ValueError as v_error:
        print(f"Ошибка ввода: {v_error}")
    except ZeroDivisionError as error:
        print(f"Ошибка ввода: {error}")


if __name__ == '__main__':
    main()
