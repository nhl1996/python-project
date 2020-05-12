# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs
import re
import os

# 网址：  https://www.bequgew.com/582/

kv={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'}


def get_content(url):
    with open('万古神帝.txt','w',encoding='utf-8') as f:
        while(1>0):
            r = requests.get(url,kv)
            last_url = url
            print(url)
            if r.status_code!=200:
                continue
            r.encoding = r.apparent_encoding
            html = r.text
            soup = BeautifulSoup(html,"html.parser")
            tishi = soup.title.get_text()[:-11]
            print(tishi)
            f.write(tishi+'\n')
            for xx in soup.find_all('div',{'id':'book_text'}):
                f.write(xx.get_text())
            f.write('\n')
            for i in soup.find_all('a',string='下一页'):
                url = 'https://www.bequgew.com'+i['href']
                break
            if len(url) == len('https://www.bequgew.com/582/'):
                break
        f.close()
    return last_url

if __name__=="__main__":
    first_url = "https://www.bequgew.com/582/42809818.html"
    last_url = get_content(first_url)
    # print(last_url)
    print('完毕')
    flag = input("是否保存，y/n :")
    if flag == 'y':
        with open('万古神帝.py','r',encoding='utf-8') as f:
            lines = f.readlines()
        with open('万古神帝.py','w',encoding='utf-8') as n_f:
            for line in lines:
                # print(line)
                if first_url in line:
                    line = line.replace(first_url,last_url)
                n_f.write(line)
        print("已修改！")
    else:
        print("未修改！")
    os.system("pause")
