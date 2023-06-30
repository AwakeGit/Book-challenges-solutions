# 3.6 Напишите программу, которая будет выводить разные строки в зависимости от того, какое целое число было вами
# присвоено переменной age, содержащейся в этой программе

def check(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Только целое число.")

    if age < 0:
        raise ValueError("Возраст не может быть отрицательным.")
    elif age < 18:
        return "Вы еще несовершеннолетний."
    elif 18 <= age < 65:
        return "Вы взрослый."
    else:
        return "Вы пенсионер."


def main() -> None:
    """
    Вызов главной функции.
    :return: None
    """

    while True:
        try:
            age_input: str = input("Введите возраст: ")
            print(check(age_input))
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}")


if __name__ == '__main__':
    main()
