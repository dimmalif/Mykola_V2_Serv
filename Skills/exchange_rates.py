import re
import requests
from bs4 import BeautifulSoup as BS
import lxml
from Skills.BFunction import BFunction


class ExchangeRates(BFunction):
    def __init__(self, text_data=None):
        super().__init__(text_data)
        self.result = None

    def get_exchange_rates(self):
        req_res = requests.get('https://currency.me.uk/rates/uah-ukraine-hryvnia')
        soup = BS(req_res.text, 'lxml')
        find_res = soup.find('table').text.strip().split('\n')
        dict_all_price = {}
        for i in range(len(find_res)):
            if find_res[i] == 'UAH':
                dict_all_price[find_res[i + 1]] = [round(1 / float(find_res[i + 2]), 3)]
            i += 6

        self.result = f"US Dollar (USD)\nЦіна: {dict_all_price['US Dollar (USD)'][0]} ГРН\n\n" \
                      f"Euro (EUR)\nЦіна: {dict_all_price['Euro (EUR)'][0]} ГРН\n\n" \
                      f"Polish Zloty (PLN)\nЦіна: {dict_all_price['Polish Zloty (PLN)'][0]} ГРН\n\n" \
                      f"Russian Rouble (RUB)\nЦіна: {dict_all_price['Russian Rouble (RUB)'][0]} ГРН\n\n" \
                      f"British Pound (GBP)\nЦіна: {dict_all_price['British Pound (GBP)'][0]} ГРН\n\n" \
                      f"Kazakhstan Tenge (KZT)\nЦіна: {dict_all_price['Kazakhstan Tenge (KZT)'][0]} ГРН\n\n" \
                      f"Chinese Yuan (CNY)\nЦіна: {dict_all_price['Chinese Yuan (CNY)'][0]} ГРН"
        return self.result

# print(ExchangeRates().get_exchange_rates() )
