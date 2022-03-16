import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
import csv
import re
result=[]

reder = open('Exper5.csv', encoding='utf-8')
expt = csv.reader(reder)


with open('text_links.txt') as f:
    contents = f.readlines()


async def main():
    async with aiohttp.ClientSession() as session:
        for i,check in enumerate(expt):
            async with session.get(contents[i]) as response:
                if response.status==404:
                    continue
                else:

                    html = await response.text(encoding='utf-8', errors="ignore")
                    soup = BeautifulSoup(html, 'lxml')

                    # Head = soup.find('h1', 'course-title').text
                    # print(i+1,':',Head.replace(" ","") == check[0].replace(" ",""), response.url)
                    # dip_down = soup.find('p', 'popular-professions_item-txt').text
                    dip_down = soup.find_all('p', 'popular-professions_item-txt')
                    # print(i + 1, ':', dip_down[0].text.replace(" ", "").rstrip() == check[1].replace(" ", "").rstrip(), response.url)
                    # print(i + 1, ':', dip_down[1].text.replace(" ", "").rstrip() == check[2].replace(" ", "").rstrip(), response.url)




if __name__ == "__main__":
    now = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("--- %s seconds ---" % (time.time() - now))