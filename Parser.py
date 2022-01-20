import json
import requests
from bs4 import BeautifulSoup
import time
start_time = time.time()
value = []
pages = 6
n = 0
s = 1
params = {'p': 1}
while params['p'] <= pages:
    response = requests.get(f'https://pentaschool.ru/trainer/p/{s}')
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('article', class_='trainers-card')

    s +=1
    for n, i in enumerate(items, start=n+1):
        trainerName = i.find('p', class_='trainers-card_name').text.strip()
        trainerCourse = i.find('ul', class_='trainers-card_title-course-list')
        if trainerCourse != None:
            value.append(f'{n}: {trainerName} преподаёт: {trainerCourse.text}')
        else:
            value.append(f'{n}: {trainerName} у преподавателя ещё нет направлений.')
    last_page_num = 6
    pages = last_page_num if pages < last_page_num else pages
    params['p'] += 1

with open('data.json', 'w',encoding='utf-8') as outfile:

    json.dump(value,outfile,ensure_ascii=False, indent=4)

print("--- %s seconds ---" % (time.time() - start_time))

