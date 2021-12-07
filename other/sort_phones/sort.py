import os
import time

CHUNK_SIZE = 10000


class BigFileSort:
    chunk_items: list = []
    chunk_files: list = []
    chunk_num: int = 0
    part_num: int = 0

    def __init__(self, file: str):
        self.file = file

    def create_chunks(self):
        with open(self.file, 'r') as data_file:
            for item in data_file:
                self._write_part_item(item)

            if self.chunk_items:
                self._write_part_to_file()

    def sort_chunks(self):
        i = 0
        while True:
            chunk_file_name = self._merge_sort(
                file_1=self.chunk_files[i],
                file_2=self.chunk_files[i + 1],
            )

            self.chunk_files.append(chunk_file_name)
            self.chunk_num += 1

            # Файлы можно удалить сразу, чтоб не занимать память
            # os.remove(self.chunk_files[i])
            # os.remove(self.chunk_files[i + 1])

            # Если больше файлов нет, значит мы все собрали и последняя запись chunk_files - итоговый файл
            i += 2
            if len(self.chunk_files) < i + 2:
                break

        return self.chunk_files[-1]

    def _write_part_item(self, item):
        """
        Сбор батчей и запись файл при превышении CHUNK_SIZE.
        """
        self.chunk_items.append(item)
        if len(self.chunk_items) == CHUNK_SIZE:
            self._write_part_to_file()

    def _write_part_to_file(self):
        """
        Сортировка и запись в файл батча.
        """
        chunk_file_name = f'files/chunk_part_{self.part_num}'
        with open(chunk_file_name, 'w') as chunk_file:
            self.chunk_items = sorted(self.chunk_items)
            chunk_file.writelines(self.chunk_items)

        self.part_num += 1
        self.chunk_files.append(chunk_file_name)
        self.chunk_items.clear()

    def _write_sorted_item(self, item):
        """
        Сбор батчей и запись файл при превышении CHUNK_SIZE.
        """
        if len(self.chunk_items) < CHUNK_SIZE:
            self.chunk_items.append(item)
            return

        self._write_to_sorted_file()

    def _write_to_sorted_file(self):
        """
        Запись в файл батча.
        """
        self.chunk_file.writelines(self.chunk_items)
        self.chunk_items.clear()

    def _merge_sort(self, file_1, file_2):
        """
        Сортировка слиянием двух файлов.
        """
        chunk_file_name = f'files/chunk_sort_{self.chunk_num}'
        with open(file_1, 'r') as chunk_file_1, open(file_2, 'r') as chunk_file_2:
            with open(chunk_file_name, 'w') as chunk_file:
                self.chunk_file = chunk_file

                item_1 = next(chunk_file_1)
                item_2 = next(chunk_file_2)
                while True:
                    if item_1 < item_2:
                        try:
                            self._write_sorted_item(item_1)
                            item_1 = next(chunk_file_1)
                        except StopIteration:
                            self._write_sorted_item(item_2)  # Остаток от иттерации в другой ветке
                            break
                    else:
                        try:
                            self._write_sorted_item(item_2)
                            item_2 = next(chunk_file_2)
                        except StopIteration:
                            self._write_sorted_item(item_1)  # Остаток от иттерации в другой ветке
                            break

                # Если остались номера
                for phone in chunk_file_1:
                    self._write_sorted_item(phone)

                for phone in chunk_file_2:
                    self._write_sorted_item(phone)

                self._write_to_sorted_file()
        return chunk_file_name


if __name__ == '__main__':
    # file_sort = BigFileSort('phones.csv')
    file_sort = BigFileSort('phones_test.csv')

    start_chunk = time.time()
    file_sort.create_chunks()
    end_chunk = time.time()
    print(f'Chunk create time: {end_chunk - start_chunk}')

    start_sort = time.time()
    file_sort.sort_chunks()
    end_sort = time.time()
    print(f'Sort time: {end_sort - start_sort}')

    print(f'Total: {end_sort - start_chunk}')
