#!/usr/bin/env python
# encoding: utf-8
import requests


class Searcher:
    def __init__(self, url: str, token: str, lang: str = 'ru-RU',
                 count_of_results: int =10, spliter: str='\n-----\n'):
        '''
        Lang - язык запроса
        url - ссылка на апи
        token - токен от яндекс.карт
        count_of_results - количество возвращаемых мест
        skip - страница пагинации
        '''
        self.lang = lang
        self.url = url
        self.token = token
        self.results = count_of_results

        self.spliter = spliter

    def search_by_text(self, text: str, skip: int = 0):
        result = ''

        data = self.get_json_data_by_text(text, skip)

        for el in data['features']:
            result += self.make_text_from_element(el)
            result += self.spliter

        return result

    def get_json_data_by_text(self, text: str, skip: int = 0):
        payload = {
            'apikey': self.token,
            'lang': self.lang,
            'text': text,
            'results': self.results,
            'skip': skip
        }
        result =  requests.get(self.url, params=payload)
        return result.json()

    def make_text_from_element(self, el):
        company_meta = el['properties']['CompanyMetaData']
        result = ''

        result += '<b>Имя:</b> ' + company_meta['name'] + '\n'
        result += '<b>Адрес:</b> ' + company_meta['address'] + '\n'

        if 'Phones' in company_meta:
            phone_text = ' '.join([phone['formatted'] for phone in company_meta['Phones']])
        else:
            phone_text = 'Телефон отсутсвует'
        result += '<b>Номер телефона:</b> ' + phone_text + '\n'

        site_url = company_meta['url'] if 'url' in company_meta else 'сайта нет'
        result += '<b>Сайт:</b> ' + site_url + '\n'

        return result


