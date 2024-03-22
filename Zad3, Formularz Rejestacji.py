def is_letter(char):
    return char.isalpha()

def is_digit(char):
    return char.isdigit()

def validate_date(date_str):
    day, month, year = date_str.split('-')
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > 31:
        return False
    return True

def validate_email(email):
    if email.count('@') != 1:
        return False
    if email[0].isdigit():
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True

def encrypt_name(name):
    parts = name.split()
    encrypted_name = ''
    for part in parts:
        encrypted_part = part[0].upper() + '*' * (len(part) - 1)
        encrypted_name += encrypted_part + ' '
    return encrypted_name.strip()

def encrypt_email(email):
    local_part, domain_part = email.split('@')
    encrypted_local_part = local_part[0].upper() + '*' * (len(local_part) - 1)
    return encrypted_local_part + '@' + domain_part

def calculate_age(year_of_birth):
    current_year = 2024
    return current_year - year_of_birth

name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")
date_of_birth = input("Podaj datę urodzenia(dd-mm-rrrr): ")
email = input("Podaj adres e-mail: ")


if not validate_email(email):
    print("Błędny format adresu e-mail!")
    exit()

if not validate_date(date_of_birth):
    print("Błędny format daty urodzenia!")
    exit()

encrypted_name = encrypt_name(name + ' ' + surname)
age = calculate_age(int(date_of_birth.split('-')[2]))
encrypted_email = encrypt_email(email)


user_data = {
    "Imię i Nazwisko": encrypted_name,
    "Wiek": age,
    "Mail": encrypted_email
}

print(user_data)