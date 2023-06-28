# 3.5 Напишите программу, которая принимает две переменные, делит одну на другую и выводит частное.

def divide(a: int, b: int) -> str:
    """
    Выполняет деление двух чисел и возвращает частное.
    :param a: Делимое число.
    :param b: Делитель.
    :return: Строку, содержащую результат деления (частное) и остаток.
    """

    quotient: int = a // b

    return f"Частное: {quotient}"


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
        else:
            print(divide(a, b))

    except ValueError as v_error:
        print(f"Ошибка ввода: {v_error}")
    except ZeroDivisionError as error:
        print(f"Ошибка ввода: {error}")


if __name__ == '__main__':
    main()
