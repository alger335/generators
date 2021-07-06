import hashlib


# TODO 2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки
#  файла.
def md5(line, encoding='utf-8'):
    hash_md5 = hashlib.md5()
    hash_md5.update(line.encode(encoding))
    return hash_md5.hexdigest()
path = 'country_url.txt'
md5(path)

def gen(path):
    with open(path) as file:
        for line in file:
            yield line

for item in gen(path):
    print(md5(item))










# def md5(line):
#     hash_md5 = hashlib.md5()
#     hash_md5.update(line)
#     # print(hash_md5.hexdigest())
#     return hash_md5.hexdigest()
#
#
# def gen(path):
#     with open(path) as file:
#         for line in file:
#             yield line.upper()
