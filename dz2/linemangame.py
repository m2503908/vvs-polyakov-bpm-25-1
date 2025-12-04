def show_menu():
    """Функция показывает главное меню игры"""
    print("=" * 50)
    print("ИГРА 'СТРОЧНИК'")
    print("=" * 50)
    print("Доступные уровни: 1, 2, 3, 4, 5")
    print("Для выхода введите 'выход'")
    print("-" * 50)


def show_level_info(level: int):
    """Функция показывает информацию о выбранном уровне"""
    print(f"\nУРОВЕНЬ {level}")
    print("-" * 30)

    if level == 1:
        print("Проверочный текст: 'прИвЕт МИР'")
        print("Доступные методы: upper(), lower(), capitalize()")
        print("Пример ввода: строка метод")
        print("Пример: 'прИвЕт МИР upper()'")

    elif level == 2:
        print("Проверочный текст: 'Ботать – это круто. Очень круто!'")
        print("Доступные методы: find(), replace(), count()")
        print("Пример ввода: строка метод")
        print("Пример: 'Ботать – это круто. Очень круто! find(круто)'")

    elif level == 3:
        print("Проверочный текст: '1,2,3,4,5,6'")
        print("Доступные методы: split(), join()")
        print("Пример ввода: строка метод")
        print("Пример: '1,2,3,4,5,6 split(,)'")

    elif level == 4:
        print("Проверочные тексты:")
        print("text_4a = '123456'")
        print("text_4b = 'abc'")
        print("text_4c = ' abc^&* '")
        print("Доступные методы: isdigit(), isalpha(), strip(), rstrip(), lstrip()")
        print("Пример ввода: строка метод")
        print("Пример: '123456 isdigit()'")

    elif level == 5:
        print("Проверочный текст: ' python;IS;AWEsomE;! '")
        print("Используйте методы с предыдущих уровней")
        print("Цель: превратить в 'Python is awesome!'")
        print("Пример ввода: строка 'python;IS;AWEsomE;! '")


def level_1(user_string: str, method: str) -> str:
    """Функция для уровня 1"""
    if method == "upper()":
        return user_string.upper()
    elif method == "lower()":
        return user_string.lower()
    elif method == "capitalize()":
        return user_string.capitalize()
    else:
        return f"Метод '{method}' не найден. Доступные: upper(), lower(), capitalize()"


def level_2(user_string: str, method: str) -> str:
    """Функция для уровня 2"""
    if method.startswith("find(") and method.endswith(")"):
        # Извлекаем подстроку для поиска из метода
        find_str = method[5:-1]
        #print(find_str)
        position = user_string.find(find_str)
        return str(position)

    elif method.startswith("replace(") and method.endswith(")"):
        # Извлекаем аргументы для замены
        args = method[8:-1].split(",")
        #print(args)
        if len(args) == 2:
            old_str = args[0]
            new_str = args[1]
            return user_string.replace(old_str, new_str)
        else:
            return "Ошибка: replace() требует два аргумента (что заменить, на что заменить)"

    elif method.startswith("count(") and method.endswith(")"):
        # Извлекаем подстроку для подсчета
        count_str = method[6:-1]
        count = user_string.count(count_str)
        return str(count)

    else:
        return f"Метод '{method}' не найден или неверный формат. Примеры: find(слово), replace(старое,новое), count(о)"


def level_3(user_string: str, method: str) -> str:
    """Функция для уровня 3"""
    if method.startswith("split(") and method.endswith(")"):
        # Извлекаем разделитель
        separator = method[6:-1]
        #print(separator)
        parts = user_string.split(separator)
        return f"Результат разделения: {parts}"

    elif method.startswith("join(") and method.endswith(")"):
        # Извлекаем разделитель и предполагаем, что строка уже разделена
        separator = method[5:-1]
        # Для join() нужно передать список, поэтому создадим его из строки
        # Сначала разделим строку, потом соединим
        temp_parts = user_string.split(",")
        result = separator.join(temp_parts)
        return result

    else:
        return f"Метод '{method}' не найден. Примеры: split(,), join(;)"


def level_4(user_string: str, method: str) -> str:
    """Функция для уровня 4"""
    if method == "isdigit()":
        result = user_string.isdigit()
        return str(result)

    elif method == "isalpha()":
        result = user_string.isalpha()
        return str(result)

    elif method == "strip()":
        result = user_string.strip()
        return result

    elif method == "rstrip()":
        result = user_string.rstrip()
        return result

    elif method == "lstrip()":
        result = user_string.lstrip()
        return result

    else:
        return f"Метод '{method}' не найден. Доступные: isdigit(), isalpha(), strip(), rstrip(), lstrip()"


def level_5(user_string: str) -> str:
    """Функция для уровня 5"""
    # Убираем лишние пробелы в начале и конце
    step1 = user_string.strip()

    # Разделяем по точке с запятой
    step2 = step1.split(";")

    # Собираем обратно с пробелами
    step3 = " ".join(step2)

    # Приводим к нижнему регистру
    step4 = step3.lower()

    # Убираем лишний пробел перед восклицательным знаком
    step5 = step4.replace(" !", "!")

    # Делаем первую букву заглавной
    step6 = step5.capitalize()

    return step6


def main():
    """Основная функция игры"""
    print("Добро пожаловать в игру 'Строчник'!")
    print("Выберите уровень и введите строку с методом для обработки.")
    print("=" * 50)

    while True:
        show_menu()

        # Запрос уровня у пользователя
        level_input = input("Введите номер уровня (1-5) или 'выход': ")

        if level_input.lower() == "выход":
            print("Спасибо за игру! До свидания!")
            break

        # Проверка корректности ввода уровня
        if not level_input.isdigit():
            print("Ошибка: уровень должен быть числом от 1 до 5")
            continue

        level = int(level_input)

        if level < 1 or level > 5:
            print("Ошибка: уровень должен быть от 1 до 5")
            continue

        show_level_info(level)

        # Запрос строки и метода у пользователя
        if level == 5:
            user_string = input("Введите строку для обработки: ")
            method = ""  # Для 5 уровня метод не нужен
        else:
            user_input = input("Введите строку и метод (пример: 'строка метод'): ")

            # Разделяем строку и метод (метод - последнее слово)
            parts = user_input.split()
            if len(parts) < 2:
                print("Ошибка: нужно ввести строку и метод")
                continue

            method = parts[-1]
            user_string = " ".join(parts[:-1])

        # Обработка в зависимости от уровня
        result = ""

        if level == 1:
            result = level_1(user_string, method)
        elif level == 2:
            result = level_2(user_string, method)
        elif level == 3:
            result = level_3(user_string, method)
        elif level == 4:
            result = level_4(user_string, method)
        elif level == 5:
            result = level_5(user_string)

        # Вывод результата
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТ:")
        if level == 5:
            print(f"{user_string} -> {result}")
        else:
            print(f"{user_string} {method} = {result}")
        print("=" * 50 + "\n")

        # Предложение продолжить
        continue_game = input("Хотите продолжить? (да/нет): ")
        if continue_game.lower() != "да":
            print("Спасибо за игру! До свидания!")
            break


if __name__ == "__main__":
    main()
