import os

def char_to_int(char_variable):
    try:
        result = int(char_variable)
        return result
    except ValueError:
        return None  # Возвращаем None в случае ошибки

if __name__ == "__main__":
    # Чтение символа из переменной окружения
    char_variable = os.getenv('INPUT_CHAR_VARIABLE', None )
    print(f"Значение переменной INPUT_CHAR_VARIABLE : {char_variable}")
    if char_variable is None:
        print("Переменная окружения CHAR_VARIABLE не определена.")
    else:
        result = char_to_int(char_variable)
        if result is not None:
            print(result)
        else:
            print("Ошибка: Введенный символ не является цифрой.")

