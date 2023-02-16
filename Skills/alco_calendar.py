import datetime
import re
import requests
from bs4 import BeautifulSoup as BS


def get_holydays():
    link = 'https://daytoday.ua/sogodni/'
    filepath = '/home/dmytro/Desktop/Mykola/Bot_Mykola/today_holyday.txt'

    with open('today_holyday.txt', 'r', encoding='utf-8') as f: # check date, if today return path to file
        date_file = re.findall(r'(\w+)', f.readline())
        date_now = re.findall(r'(\w+)', datetime.datetime.now().strftime('%x'))

    if date_now[1] == date_file[1]:
        print('get holydays')
        return filepath

    req_res = requests.get(link)
    soup = BS(req_res.text, 'lxml')
    search_res = soup.findAll('div', {'class': 'pt-cv-pinmas'})  # get raw data
    finaly_res = []
    for i in range(len(search_res)):
        intermediate_result = search_res[i].find('a', {'class': '_self pt-cv-href-thumbnail pt-cv-thumb-left cvplbd'})
        if intermediate_result: # intermediate_result can be None
            intermediate_result = intermediate_result.find(
                class_='pt-cv-thumbnail img-rounded pull-left no-lazyload skip-lazy')
            finaly_res.append(re.findall(r'img alt="(\w*\s+[^"]+)', str(intermediate_result))) # filter data

    print('write holydays')
    with open('today_holyday.txt', 'w', encoding='utf-8') as file: # write new date and data
        file.write(f"{datetime.datetime.now().strftime('%x')}\n")
        for i in range(len(finaly_res)):
            if finaly_res[i]: # finaly_res[i] can be []
                file.write(f"{str(finaly_res[i][0])}\n")
    return filepath






