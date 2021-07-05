from iter import *
from generator import *

if __name__ == '__main__':
    output_file = open('country_url.txt', 'w', encoding='utf-8')

    print('Working...')
    for country, item in WikiPage('countries.json', 0):
        output_file.write(str(country) + '\t — \t' + str(item) + '\n')
    print('Done!')

    output_file.close()

    with open('country_url.txt', "rb") as f:
        for line in f:
            md5(line)
