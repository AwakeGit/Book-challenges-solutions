# 3.6 Напишите программу, которая будет выводить разные строки в зависимости от того, какое целое число было вами
# присвоено переменной age, содержащейся в этой программе

def main():
    try:

        age: str = input("Введите делимое число: ")

        if not age.isdigit():
            raise ValueError("Введено некорректное значение. Ожидаются целые числа.")

        age: int = int(age)

        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        elif age < 18:
            print("Вы еще несовершеннолетний.")
        elif 18 <= age < 65:
            print("Вы взрослый.")
        else:
            print("Вы пенсионер.")

    except ValueError as v_error:
        print(f"Ошибка ввода: {v_error}")


if __name__ == '__main__':
    main()
