import string
import random


def generate_password(length: int = 8, use_upper: bool = False,
                      use_lower: bool = False, use_digit: bool = False,
                      use_punctuation: bool = False) -> str:
    pool = ""
    password_characters = []

    if use_upper:
        pool += string.ascii_uppercase
        password_characters.append(random.choice(string.ascii_uppercase))
    if use_lower:
        pool += string.ascii_lowercase
        password_characters.append(random.choice(string.ascii_lowercase))
    if use_digit:
        pool += string.digits
        password_characters.append(random.choice(string.digits))
    if use_punctuation:
        pool += string.punctuation
        password_characters.append(random.choice(string.punctuation))

    if len(pool) == 0:
        pool += string.ascii_uppercase + string.ascii_lowercase

    num_used_characters = len(password_characters)
    password_characters = random.choices(
        population=pool, k=length-num_used_characters) + password_characters
    random.shuffle(password_characters)

    password = "".join(password_characters)

    return password
