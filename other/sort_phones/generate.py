import random

PHONES_COUNT: int = 1_000_000


with open('phones.csv', 'w') as phones_file:
    for _ in range(PHONES_COUNT):
        random_nums = [str(num) for num in random.sample(range(9), 7)]
        phone = '+79' + ''.join(random_nums) + "\n"

        phones_file.writelines(phone)
