import random
import re
import string


def return_data(funcname: str):
    # Возвращает данные для тестирования по наименованию теста
    dic = {'enter_name': [(30, '-'), (30, ''), (29, '-'), (29, ''), (3, '-'), (2, '')],
           'enter_name_un': ['а', 'б-', 'в--г', 'дd', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'е  ж', 'з.ий']}
    return dic[funcname]


def generator_valid_text_for_name(n: int, delimiter=''):
    # Возвращает валидные текстовые строки для тестирования полей имени и фамилии
    symbols = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
               'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
               'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    if delimiter:
        result = random.sample(symbols, n - 1)
        index = random.randrange(1, n - 2) if n > 3 else 1
        return ''.join(result[:index] + [delimiter] + result[index:])
    else:
        return ''.join(random.sample(symbols, n))


def correct_phone_number():
    # Генерирует валидные номера телефонов: "7хххххххххх" или "8хххххххххх", или "375ххххххххх"
    head = random.choice(['8', '7', '375'])
    return head + ''.join([str(random.randint(0, 9)) for _ in range(10 if len(head) == 1 else 9)])


def correct_email():
    # Генерирует валидный email для тестирования поля "email или телефон"
    letters = string.ascii_letters + string.digits + "_-"
    username_length = random.randint(1, 10)
    username = ''.join(random.choice(letters) for _ in range(username_length))
    domain_length = random.randint(1, 6)
    domain = ''.join(random.choice(letters) for _ in range(domain_length))
    extension = random.choice(["com", "net", "org", "gov", "edu"])
    email = f"{username}@{domain}.{extension}"
    return email


def incorrect_email():
    # Генерирует невалидный email для тестирования поля "email или телефон"
    domain_length = random.randint(0, 10)
    domain = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(domain_length))
    extension_length = random.randint(0, 4)
    extension = ''.join(random.choice(string.ascii_lowercase) for _ in range(extension_length))

    username_length = random.randint(5, 15)
    username = ''.join(random.choice(string.ascii_letters + string.digits + "_-") for _ in range(username_length))

    at_symbol = random.choice(["@", "#", "$", "%"])

    invalid_email = f"{username}{at_symbol}{domain}.{extension}"

    # Проверка, является ли email-адрес корректным
    if is_valid_email(invalid_email):
        # Перегенерация email-адреса, если он корректный
        invalid_email = incorrect_email()

    return invalid_email


def is_valid_email(email):
    # Проверяет валидность email регулярным выражением
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def incorrect_phone_number():
    # Генерирует невалидный номер телефона для тестирования поля "email или телефон"
    number = ''.join(random.choice("0123456789") for _ in range(random.randint(1, 10)))
    while is_valid_phone_number(number):
        number = ''.join(random.choice("0123456789") for _ in range(random.randint(1, 10)))
    return number


def is_valid_phone_number(phone_number):
    # Проверяет валидность номера телефона
    if phone_number.startswith("7") and len(phone_number) == 11:
        return True
    if phone_number.startswith("375") and len(phone_number) == 12:
        return True
    return False


def correct_password():
    # Генерирует корректный пароль:
    # пароль является корректным, если в нём только латинские буквы,
    # обязательно есть одна строчная буква и одна заглавная, есть цифра или спецсимвол.
    # Длина пароля составляет от 8 до 20 цифр
    lowercase_letter = random.choice(string.ascii_lowercase)
    uppercase_letter = random.choice(string.ascii_uppercase)
    digit_or_symbol = random.choice(string.digits + string.punctuation)
    remaining_length = random.randint(5, 17)  # Общая длина пароля будет от 8 до 20 символов
    password = lowercase_letter + uppercase_letter + digit_or_symbol

    for _ in range(remaining_length):
        character_type = random.randint(1, 3)
        if character_type == 1:
            password += random.choice(string.ascii_lowercase)
        elif character_type == 2:
            password += random.choice(string.ascii_uppercase)
        else:
            password += random.choice(string.digits + string.punctuation)

    return password


def incorrect_password():
    #Генерирует некорректный пароль
    lowercase_letter = random.choice(string.ascii_lowercase)
    uppercase_letter = random.choice(string.ascii_uppercase)
    digit_or_symbol = random.choice(string.digits + string.punctuation)
    cyrillic_letter = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    incorrect_type = random.randint(1, 6)
    if incorrect_type == 1:
        # Некорректность 1: отсутствие строчной буквы
        password = uppercase_letter + digit_or_symbol
    elif incorrect_type == 2:
        # Некорректность 2: отсутствие заглавной буквы
        password = lowercase_letter + digit_or_symbol
    elif incorrect_type == 3:
        # Некорректность 3: отсутствие цифры или спецсимвола
        password = lowercase_letter + uppercase_letter
    elif incorrect_type == 4:
        # Некорректность 4: длина пароля меньше 8 символов
        remaining_length = random.randint(0, 5)
        password = lowercase_letter + uppercase_letter + digit_or_symbol[:remaining_length]
    elif incorrect_type == 5:
        # Некорректность 5: длина пароля больше 20 символов
        extra_length = random.randint(1, 10)
        password_length = 20 - extra_length
        password = lowercase_letter + uppercase_letter + digit_or_symbol + ''.join(
            random.choices(string.ascii_letters + string.digits + string.punctuation, k=extra_length))
    elif incorrect_type == 6:
        # Некорректность 6: наличие кириллических символов
        password = lowercase_letter + uppercase_letter + digit_or_symbol + cyrillic_letter

    while is_password_correct(password):
        password = incorrect_password()

    return password


def is_password_correct(password):
    # Проверка, что пароль соответствует всем требованиям
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit_or_symbol = any(char.isdigit() or char in string.punctuation for char in password)
    has_cyrillic = any(char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for char in password)
    is_correct_length = 8 <= len(password) <= 20

    return (
            has_lowercase
            and has_uppercase
            and has_digit_or_symbol
            and not has_cyrillic
            and is_correct_length
    )

