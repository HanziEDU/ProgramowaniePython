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
    parts = email.split('@')

    if len(parts) != 2:
        return False

    local_part, domain_part = parts
    if not is_letter(local_part[0]):
        return False

    if '.' not in domain_part or not domain_part.split('.')[0].isalpha():
        return False

    return True


def encrypt_name(name):
    encrypted_name = ''
    for char in name:
        if is_letter(char):
            encrypted_name += char.upper()
        else:
            encrypted_name += char
    return encrypted_name


def encrypt_email(email):
    local_part, domain_part = email.split('@')
    encrypted_local = local_part[0].upper() + '*' * (len(local_part) - 1)
    return encrypted_local + '@' + domain_part


def calculate_age(birth_year):
    current_year = 2024
    return current_year - int(birth_year)


def main():
    name = input("Podaj imię i nazwisko: ")
    birth_date = input("Podaj datę urodzenia w formacie dd-mm-rrrr: ")
    email = input("Podaj adres e-mail: ")

    if not validate_date(birth_date):
        print("Nieprawidłowy format daty urodzenia.")
        return

    if not validate_email(email):
        print("Nieprawidłowy format adresu e-mail.")
        return

    encrypted_name = encrypt_name(name)
    encrypted_email = encrypt_email(email)
    age = calculate_age(birth_date.split('-')[-1])

    user_data = {
        'imię i nazwisko': encrypted_name,
        'wiek': age,
        'mail': encrypted_email
    }

    print("Wprowadzone dane:")
    print(user_data)


if __name__ == "__main__":
    main()
