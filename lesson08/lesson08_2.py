import requests


class SomeError(Exception):
    def __init__(self, text:None):
        self.text = text

class Product:
    id  = ''
    name  = ''
    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id} : {self.name}'

    def parse(self):
        url = self.__start_url
        while url:
            response = requests.get(url, params=self.__params, headers = self.__headers)
            data = response.json()
            url = None #url = data['next']
            self.products.extend(Product(itm) for itm in data['result'])

class Parser:
    def __init__(self, stat_url:str):
        __params = {""}
        __headers = {"records_per_page":50,
                     "categories" : 20}

class Header(self):
    pass

if __name__ == '__main__':
    print('0')
    parser = Parser('https://5ka.ru/api/v2/special_offers/')
    print('1')
    print('2')