import random
import string

def generate_password(length=8, min_letters=4, min_digits=2):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if sum(c.isdigit() for c in password) >= min_digits and sum(c.isalpha() for c in password) >= min_letters:
            yield password

generator_haseł = generate_password(length=10, min_letters=5, min_digits=3)
for _ in range(5):
    print(next(generator_haseł))