import json
import wikipediaapi


# TODO 1. Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.

class WikiPage:
    def __init__(self, path, counter):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.counter = counter - 1
        self.wiki = wikipediaapi.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1

        if self.counter == len(self.json):
            raise StopIteration

        country = self.json[self.counter]['name']['common']
        country_page = self.wiki.page(country)
        country_url = country_page.fullurl

        return country, country_url
