# -*- coding:utf-8 -*-

# url https://www.biquge.info/15_15058/

from bs4 import BeautifulSoup
import requests
import codecs
import re
import os
import time



kv={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def get_content(url):
    with open('妖神记.txt','w',encoding='utf-8') as f:
        zh = 1
        while(1>0):
            time.sleep(1)
            r = requests.get(url,kv)
            if r.status_code!=200:
                continue
            print(url)
            r.encoding = r.apparent_encoding
            html = r.text
            print(html)
            soup = BeautifulSoup(html,"html.parser")
            tishi = soup.title.get_text()[0:-13].strip('\n')
            print(tishi)
            f.write('\n'+tishi+'\n')
            txt = soup.find_all('div',{'id':'content'})
            f.write(txt[0].text)
            f.write('\n')
            for i in soup.find_all('a',string='下一章'):
                url = i['href']
                break
            if len(url) == len('http://www.biquge.info/15_15058/'):
                break
            zh+=1
        f.close()

if __name__=="__main__":
    get_content("http://www.biquge.info/15_15058/11631596.html")
    print('完毕')
    os.system("pause")
