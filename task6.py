"""Программа запрашивает у пользователя пароль и записывает в переменную password.
Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке,
максимальное количество баллов - 5
Проверки:
Длина пароля больше или равно 8 символам
В пароле есть хотя бы одна цифра
В пароле есть хотя бы одна большая
В пароле есть хотя бы одна маленькая буква
В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же
рекомендации по улучшению пароля."""

password = input()
i = 0
is_length = False
is_digit = False
is_capital = False
is_low = False
is_special = False

if len(password) >= 8:
    is_length = True
    i += 1

for a in password:
    if a.isdigit():
        is_digit = True
        i += 1
        break

if password < password.lower():
    is_capital = True
    i += 1

if password > password.upper():
    is_low = True
    i += 1

for b in password:
    if b.isalnum():
        is_special = True
        continue
    else:
        i += 1
        break

print(f'Password score: {i}')
if is_length:
    True
else:
    print('The minimum password length is 8')
if is_digit:
    True
else:
    print('Use digits')
if is_capital:
    True
else:
    print('Use capital letters')
if is_low:
    True
else:
    print('Use little letters')
if b.isalnum():
    print('Use special characters')











