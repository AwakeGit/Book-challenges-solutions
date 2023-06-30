# 4.1	Напишите функцию, которая принимает число в качестве ввода, возводит его в квадрат и возвращает.

def calculator(a: str) -> float:
    """
    Возвращает квадрат числа
    :param a: Целое число
    :return: int
    """
    a = float(a)

    if a == 0:
        raise ValueError("У числа 0 нет квадрата.")
    elif not a:
        raise ValueError("Только цифры.")
    return a * a


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    while True:
        try:
            a_input: str = input("Введите целое число: ")
            print(calculator(a_input))
            break

        except ValueError as e:
            print(f"Ошибка ввода: {e}")


if __name__ == '__main__':
    main()
