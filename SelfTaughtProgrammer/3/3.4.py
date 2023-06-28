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
        a: int = int(input("Введите делимое число: "))
        b: int = int(input("Введите делитель: "))

        if a == 0:
            raise ZeroDivisionError("Делимое не может быть нулем.")
        elif b == 0:
            raise ZeroDivisionError("Делитель не может быть нулем.")
        elif not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Введено некорректное значение. Ожидаются целые числа.")
        else:
            print(divide_with_remainder(a, b))

    except ValueError:
        print("Некорректный ввод. Введите целое число.")
    except ZeroDivisionError as error:
        print(error)


if __name__ == '__main__':
    main()
