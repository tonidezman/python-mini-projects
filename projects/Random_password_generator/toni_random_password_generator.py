import random
import string


def generate_random_number():
    try:
        password_length = int(input("Length of the password: "))
    except ValueError as err:
        print(f"You need to type numbers: {err}")
        return

    res = []
    while len(res) < password_length:
        if random.randint(0, 1):
            idx = random.randint(0, len(string.ascii_letters))
            res.append(string.ascii_letters[idx])
        else:
            if random.randint(0, 1):
                idx = random.randint(0, len(string.digits))
                res.append(string.digits[idx])
            else:
                idx = random.randint(0, len(string.punctuation))
                res.append(string.punctuation[idx])
    return "".join(res)


if __name__ == "__main__":
    print(generate_random_number())
