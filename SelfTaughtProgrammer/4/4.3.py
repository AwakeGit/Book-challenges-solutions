# 4.3 Напишите функцию, которая принимает три обязательных и два необязательных параметра.

from typing import Optional, Tuple


def get_user_input() -> Optional[Tuple[str, Optional[str], int, Optional[str], Optional[str]]]:
    """
    Получает ввод пользователя для имени, города, возраста, профессии и языка программирования.
    Проверяет ввод на корректность и полноту.
    :return: Кортеж значений, если все обязательные поля заполнены корректно, иначе None.
    """
    fields = {
        "Имя": (str.isalpha, "строку"),
        "Город": (str.isalpha, "строку"),
        "Возраст": (str.isdigit, "число"),
        "Профессия": (str.isalpha, "строку"),
        "Язык программирования": (str.isalpha, "строку")
    }
    user_input = []

    for field, (validate_func, value_type) in fields.items():
        while True:
            value: str = input(f"Введите {field}: ")
            if not value.strip() and field in ("Имя", "Возраст"):
                print(f"Поле '{field}' не может быть пустым.")
            elif value.strip() and not validate_func(value):
                print(f"Некорректное значение для поля '{field}'. Необходимо ввести только {value_type}.")
            else:
                user_input.append(value)
                break

    name, city, age, profession, lang = user_input

    try:
        age = int(age)
    except ValueError:
        print("Некорректное значение для поля 'Возраст'. Необходимо ввести только число.")
        return None

    return name, city, age, profession, lang


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    user_input: tuple = get_user_input()
    if user_input:
        name, city, age, profession, lang = user_input

        print()
        print(f"Имя: {name}")
        print(f"Город: {city}" if city else "Город: не указан")
        print(f"Возраст: {age}")
        print(f"Профессия: {profession}" if profession else "Профессия: не указана")
        print(f"Язык программирования: {lang}" if lang else "Язык программирования: не указан")


if __name__ == '__main__':
    main()
