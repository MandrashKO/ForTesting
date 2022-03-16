import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
import csv
import re
import difflib as df
result=[]

# reder = open('Exper5.csv', encoding='utf-8')
# reder = open('ExPerim2.csv', encoding='utf-8')
reder = open('ExPerim2.csv', encoding='utf-8')
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
                    # dip_down = soup.find_all('p', 'popular-professions_item-txt')
                    # print(i + 1, ':', dip_down[0].text.replace(" ", "").rstrip() == check[1].replace(" ", "").rstrip(), response.url)
                    # print(i + 1, ':', dip_down[1].text.replace(" ", "").rstrip() == check[2].replace(" ", "").rstrip(), response.url)
                    profession_head = soup.find_all('h4', 'profess-job-market_title')
                    # print(profession_head[0].get_text(strip=True).replace(" ","")==check[3].replace(" ",""))
                    profession_text = soup.find_all('div', "profess-job-market_text")
                    # print(profession_text[0].get_text(strip=True).replace(" ","")==check[4].replace(" ",''))
                    # print(profession_text[0].get_text(strip=True).replace(" ","").rstrip())
                    # print(profession_text[0].get_text(strip=True).replace(" ","").rstrip() == check[4].replace(" ",'').rstrip())
                    # print(profession_text[0].get_text(strip=True).replace(" ","").rstrip().splitlines() == check[4].replace(" ",'').rstrip().splitlines())
                    # print(profession_text[0].get_text(strip=True).replace(" ","").splitlines() == check[4].replace(" ",'').splitlines())
                    # print(check[4].replace(" ",'').rstrip())
                    # print(check[3].replace(" ",'').replace("\n",''))
                    profession_price = soup.find_all('div', "profess-job-market_price-items")
                    # print(profession_price[0].text.replace(' ','').replace('\n','').replace(' ','')==check[5].replace(' ','').replace('\n',''))
                    print(profession_price[0].get_text(strip=True).replace(' ',""))
                    # print(profession_price[0].text.replace(' ','').replace('\n','').replace(' ',''))
                    print(check[5].replace(' ','').replace('\n',''))
                    # print(check[5].replace(' ','').replace('\n','')==profession_price[0].get_text(strip=True).replace(' ',""))



if __name__ == "__main__":
    now = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("--- %s seconds ---" % (time.time() - now))