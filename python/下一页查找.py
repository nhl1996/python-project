# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs
import re
import os

# 网址：  https://www.bequgew.com/582/

kv={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'}


def get_content(url):
    with open('FN.txt','w',encoding='utf-8') as f:
        while(1>0):
            r = requests.get(url)
            last_url = url
            if r.status_code!=200:
                continue
            r.encoding = r.apparent_encoding
            html = r.text
            soup = BeautifulSoup(html,"html.parser")
            tishi = soup.title.get_text()

            print(tishi)
            f.write(tishi+'\n')
            for xx in soup.find_all('div',{'class':'page-content font-large'}).find('a')[:
                f.write(xx.get_text())
            f.write('\n')
            for i in soup.find_all('a',string='下一页'):
                print(i['href'])
                url = i['href']
                break
            if len(url) == len("/book/7064/0.html"):
                break
            print(url)
    return last_url

if __name__=="__main__":
    first_url = "https://www.diyibanzhu.tw/wap.php?action=article&id=999&uid="
    last_url = get_content(first_url)
    # print(last_url)
    print('完毕')
    
