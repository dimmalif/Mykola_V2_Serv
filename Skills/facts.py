import re
from random import randrange


def fact():
    with open('Interesting_Facts.txt', encoding='utf-8') as file:
        data = file.read()

    lines = data.split('\n')
    ind = randrange(len(lines))
    fact = lines[ind]

    res = re.findall(f'[\d+]+\w.(.+)', fact)
    return res[0]
