import re
def get_binary_strings():
    while True:
        user_input = input("Введите строку (для завершения введите 'q'): ")
        if user_input.lower() == 'q':
            break
        if not re.fullmatch(r'[01]*', user_input): # checks if the input string is a binary string
            print("Ошибка¯\_(ツ)_/¯: Неверный ввод. Введите строку без пробелов, содержащую только символы '0' и '1'.")
            continue
        if int(user_input, 2) % 3 == 0: # checks if the binary number is a multiple of three
            print(f"Строка '{user_input}' содержит двоичную запись числа, кратного 3.")
get_binary_strings()
