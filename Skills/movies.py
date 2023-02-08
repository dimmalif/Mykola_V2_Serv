import requests
import re
import random

from skills import BFunction

link_for_search = 'https://uaserials.pro/films/f/year=2022;2022/imdb=0;10'


class Movies(BFunction):
    def __init__(self, text_data, genre=None):
        super().__init__(text_data)

        self.genre = genre

    @staticmethod
    def get_film():
        html_code = requests.get(link_for_search).text
        links_films = re.findall(r'<a class="short-img img-fit" href="(\S+)">', html_code)
        names_of_films = re.findall(r'alt="(.+)">', html_code)
        dict_of_films = tuple(zip(names_of_films, links_films))
        selected_film = random.choice(dict_of_films)
        return selected_film


m = Movies('коля порекомендуй фільм')
print(m.get_film())
