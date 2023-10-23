# TY版爬10頁

import requests
from bs4 import BeautifulSoup
url = 'http://ptt.cc/bbs/TY_Research/index.html'


for i in range(10):
    print(f"第{i+1}頁")
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'html.parser')
    datas = sp.find_all('div', class_='r-ent')
    for data in datas:
        if data.a:  # 有些頁面被刪除會顯示空白導致無法爬取，需建立一個判斷式避免出現error
            print(data.find('div', class_='date').text, end=' ')
            print('https://www.ptt.cc' + data.a.get('href'), end=' ')
            print(data.a.text)
    url = 'http://ptt.cc' + sp.find_all('a', class_='btn wide')[1].get('href')
