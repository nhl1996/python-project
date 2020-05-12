#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
 
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

print(phone)
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print ("电话号码是 : ", num)




'''
kv={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'}
b=[]

f = open('m.txt','w',encoding = 'utf-8')

def get_content():
    for x in b:
        url = str(x)
        #print(url)
        r = requests.get(url)
        #print(r.status_code)
        r.encoding = 'gbk'
        html = r.text
        soup = BeautifulSoup(html,'html.parser')
        #print(soup)
        hh = soup.find_all('div',{'id':'chaptercontent'})
        tishi = soup.title.get_text()[:-9]
        print(tishi)
        f.write(tishi+'\n')
        for xx in hh:
            f.write(xx.get_text())
        #time.sleep(2)

def get_url(url):
    r = requests.get(url)
    #print(r.status_code)
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    #print(soup)
    hh = soup.find_all('a')
    sun =1
    for i in hh:
        a = i['href']
        #print(sun)
        if sun>=4:
            #print(a)
            b.append('http://m.fusuxs.com'+a)
        if sun==146:
            break
        sun+=1
    print("获取完毕")


if __name__=='__main__':
    get_url("http://m.fusuxs.com/18_18723/all.html")
    #time.sleep(10)
    get_content()
'''
