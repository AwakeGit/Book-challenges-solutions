# 4.1	Напишите функцию, которая принимает число в качестве ввода, возводит его в квадрат и возвращает.

def calculator(a: int) -> int:
    """
    Возвращает квадрат числа
    :param a: Целое число
    :return: int
    """
    if a == 0:
        raise ValueError("У числа 0 нету квадрата")
    return a * a


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    try:
        number_str = input("Введите число: ")
        if not number_str.isdigit():
            raise ValueError("Введено некорректное значение. Ожидаются целое число.")

        number = int(number_str)
        result = calculator(number)
        print(f"{number} в квадрате = {result}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")


if __name__ == '__main__':
    main()
