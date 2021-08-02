import hashlib


# TODO 2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки
#  файла.

def gen(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()
