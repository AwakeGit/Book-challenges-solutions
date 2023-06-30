# 3.5 Напишите программу, которая принимает две переменные, делит одну на другую и выводит частное.

def divide(a: float, b: float) -> str:
    """
    Выполняет деление двух чисел и возвращает частное.
    :param a: Делимое число.
    :param b: Делитель.
    :return: Строку, содержащую результат деления (частное) и остаток.
    """

    quotient: float = a / b

    return f"Частное: {quotient}"


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    while True:
        try:
            a_input: str = input("Введите целое число: ")
            b_input: str = input("Введите целое число: ")
            a: float = float(a_input)
            b: float = float(b_input)

            if a == 0:
                raise ZeroDivisionError("Делимое не может быть нулем.")
            elif b == 0:
                raise ZeroDivisionError("Делитель не может быть нулем.")

            print(divide(a, b))
            break

        except ValueError:
            print("Ошибка ввода. Ожидаются только целые числа.")
        except ZeroDivisionError as e:
            print(f"Ошибка деления. {e}")


if __name__ == '__main__':
    main()
