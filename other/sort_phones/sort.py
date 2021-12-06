import os
import time

CHUNK_SIZE = 100_000


def write_chunk(phones_chunk, n):
    sorted_phones_chunk = sorted(phones_chunk)
    chunk_file_name = f'files/phones_chunk_{n}'
    with open(chunk_file_name, 'w') as phones_chunk_file:
        phones_chunk_file.writelines(sorted_phones_chunk)

    return chunk_file_name


def create_chunks():
    chunk_files = []

    with open('phones.csv', 'r') as phones_file:

        phones_chunk = []
        n = 1
        for phone in phones_file:
            phones_chunk.append(phone)

            if len(phones_chunk) >= CHUNK_SIZE:
                chunk_file_name = write_chunk(phones_chunk, n)
                phones_chunk.clear()
                n += 1
                chunk_files.append(chunk_file_name)

        if phones_chunk:
            chunk_file_name = write_chunk(phones_chunk, n)
            chunk_files.append(chunk_file_name)

        return chunk_files


def sort_chunks(chunk_files):
    i = 0
    while True:
        chunk_file_name = f'files/sorted_phones_{i}'

        with open(chunk_files[i], 'r') as chunk_file_1, open(chunk_files[i + 1], 'r') as chunk_file_2:
            with open(chunk_file_name, 'w') as sorted_file:
                phone_1 = next(chunk_file_1)
                phone_2 = next(chunk_file_2)
                while True:
                    if phone_1 < phone_2:
                        try:
                            sorted_file.write(phone_1)
                            phone_1 = next(chunk_file_1)
                        except StopIteration:
                            sorted_file.write(phone_2)
                            break
                    else:
                        try:
                            sorted_file.write(phone_2)
                            phone_2 = next(chunk_file_2)
                        except StopIteration:
                            sorted_file.write(phone_1)
                            break

                # if any phone was left
                for phone in chunk_file_1:
                    sorted_file.write(phone)

                for phone in chunk_file_2:
                    sorted_file.write(phone)

        # we don't need this files more
        os.remove(chunk_files[i])
        os.remove(chunk_files[i + 1])

        chunk_files.append(chunk_file_name)
        i += 2
        if len(chunk_files) < i + 2:
            break

    return chunk_files[-1]


if __name__ == '__main__':
    chunks = create_chunks()
    start = time.time()
    result_file = sort_chunks(chunks)
    end = time.time()
    print(result_file)
    print(end - start)
