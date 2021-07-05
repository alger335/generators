import hashlib


# TODO 2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки
#  файла.
def md5(line):
    hash_md5 = hashlib.md5()
    hash_md5.update(line)
    print(hash_md5.hexdigest())
    return hash_md5.hexdigest()
