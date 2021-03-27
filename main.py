from random import randint

MIN_NUMBER = -10000
MAX_NUMBER = 10000
AMOUNT_NUMBER = 5000000


if __name__ == "__main__":
    number_list = []

    for i in range(AMOUNT_NUMBER):
        random_number = randint(MIN_NUMBER, MAX_NUMBER)
        number_list.append(random_number)

