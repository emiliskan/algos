import random
import time

MAX_NUM = 999_999_999
CHUNK_SIZE = 10_000_000


def generate_phones():
    num = 1_000_000_000
    with open('phones_test', 'w') as phones_file:

        phones_chunk = []

        for i in range(MAX_NUM):
            phone = '+79' + str(num)[1:] + "\n"
            phones_chunk.append(phone)
            num += 1

            if len(phones_chunk) > CHUNK_SIZE:
                random.shuffle(phones_chunk)
                phones_file.writelines(phones_chunk)
                phones_chunk.clear()
                print(f"{i / CHUNK_SIZE} chunk")

        random.shuffle(phones_chunk)
        phones_file.writelines(phones_chunk)


if __name__ == '__main__':
    start = time.time()
    generate_phones()
    end = time.time()
    print(end - start)
