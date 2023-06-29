# 4. Напишите программу с двумя функциями. Первая функция должна принимать в качестве параметра целое число и
# возвращать результат деления этого числа на 2. Вторая функция должна принимать в качестве параметра целое число и
# возвращать результат умножения этого числа на 4. Вызовите первую функцию, сохраните результат в переменной и
# передайте ее в качестве параметра во вторую функцию.

def divide_number(x: int) -> float:
    """
    Делит число на 2.
    :param x: Целое число.
    :return: Результат деления.
    """
    return x / 2


def multiply_number(x: float) -> float:
    """
    Умножает число на 4.
    :param x: Число.
    :return: Результат умножения.
    """
    return x * 4


def get_input_number() -> int:
    """
    Получает от пользователя целое число.
    :return: Введенное целое число.
    """

    while True:
        try:
            number: str = input("Введите число: ")

            if number == '0':
                raise ValueError("Введен 0")
            elif not number or not number.isdigit():
                raise ValueError("Введена пустая строка или не цифра")
            else:
                return int(number)

        except ValueError as e:
            print(f"Ошибка ввода: {e}.")


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """

    number = get_input_number()
    result_division = divide_number(number)
    print(f"Результат первой функции: {result_division}")
    result_multiplication = multiply_number(result_division)
    print(f"Результат второй функции: {result_multiplication}")


if __name__ == '__main__':
    main()
