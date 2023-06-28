# 3.1 Выведите три различные строки.
def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """
    a: str = input("Введите строку - 1: ")
    b: str = input("Введите строку - 2: ")
    c: str = input("Введите строку - 3: ")

    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    main()
