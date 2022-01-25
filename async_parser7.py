import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
result=[]
async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(7):
            async with session.get(f"https://pentaschool.ru/trainer/p/{i}") as response:
                html = await response.text(encoding='utf-8', errors="ignore")
                soup = BeautifulSoup(html, 'lxml')
                items = soup.find_all('article', class_='trainers-card')
                # print(html)
                for n,item in enumerate(items):
                    name = item.find('p', class_='trainers-card_name').text.strip()
                    directions = item.find('ul', class_='trainers-card_title-course-list')
                    # result.append(name)
                    # result.append(directions)
                    if directions is not None:
                        result.append(f'{n}: {name} преподаёт: {directions.text}')
                    else:
                        result.append(f'{n}: {name} у преподавателя ещё нет направлений.')
                for i in result:
                    print(i)
if __name__ == "__main__":
    now = time.time()

    # pages =
    # asyncio.(main())
    # print(result)
    loop = asyncio.get_event_loop()
    # loop.create_task(main())
    # loop.run_forever()

    loop.run_until_complete(main())
    print("--- %s seconds ---" % (time.time() - now))
    # print(result)
    #