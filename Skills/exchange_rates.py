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

        self.result = f"US Dollar (USD)\n*Ціна*: {dict_all_price['US Dollar (USD)'][0]} грн\n\n" \
                      f"Euro (EUR)\n*Ціна*: {dict_all_price['Euro (EUR)'][0]} грн\n\n" \
                      f"Polish Zloty (PLN)\n*Ціна*: {dict_all_price['Polish Zloty (PLN)'][0]} грн\n\n" \
                      f"British Pound (GBP)\n*Ціна*: {dict_all_price['British Pound (GBP)'][0]} грн\n\n" \
                      f"Kazakhstan Tenge (KZT)\n*Ціна*: {dict_all_price['Kazakhstan Tenge (KZT)'][0]} грн\n\n" \
                      f"Chinese Yuan (CNY)\n*Ціна*: {dict_all_price['Chinese Yuan (CNY)'][0]} грн"
        return self.result

# print(ExchangeRates().get_exchange_rates() )
