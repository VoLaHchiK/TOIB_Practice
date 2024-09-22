import re

""" Москаленко Алексей Леонидович 3 вариант """

def check_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#$%&]', password):
        return False

    return True

password = input()
if check_password(password):
    print("Действительный пароль")
else:
    print("Пароль не соответствует требованиям")
