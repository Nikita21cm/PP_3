def is_binary_string(s):
    return all(char in '01' for char in s)


def is_multiple_of_three(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 3 == 0


def get_binary_strings():
    while True:
        user_input = input("Введите строку (для завершения введите 'q'): ")
        if user_input.lower() == 'q':
            break

        if not is_binary_string(user_input):
            print("Ошибка¯\_(ツ)_/¯: Неверный ввод. Введите строку без пробелов, содержащую только символы '0' и '1'.")
            continue

        if is_multiple_of_three(user_input):
            print(f"Строка '{user_input}' содержит двоичную запись числа, кратного 3.")


get_binary_strings()
