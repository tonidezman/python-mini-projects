import string
import random


def random_char() -> string:
    idx = random.randint(0, len(string.ascii_letters)-1)
    return string.ascii_letters[idx]


def random_punctuation() -> string:
    idx = random.randint(0, len(string.punctuation)-1)
    return string.punctuation[idx]


def random_digit() -> string:
    idx = random.randint(0, len(string.digits)-1)
    return string.digits[idx]


def generate_random_int(password_length: int) -> string:
    res = []
    while len(res) < password_length:
        if random.randint(0, 1):
            res.append(random_char())
        else:
            if random.randint(0, 1):
                res.append(random_punctuation())
            else:
                res.append(random_digit())
    return "".join(res)


if __name__ == "__main__":
    try:
        password_length = int(input("Password length: "))
    except ValueError as e:
        print(f"Input needs to be an integer: error: {e}")

    print(generate_random_int(password_length))
