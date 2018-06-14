# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import requests
import re


if __name__ == "__main__":
    url = []
    download_url = 'http://www.360doc.com/index.html'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url=download_url, headers=head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('utf-8','ignore')
    soup = BeautifulSoup(download_html, 'lxml')
    texts = soup.find_all("ul",class_="tab zcomdiv tabn2")
    texts = BeautifulSoup(str(texts), 'lxml')
    texts = texts.find_all(href=True)
    for x in texts:
        x = x.get('href')
        url.append(x)
    #print(url)
    print("0: 社会")
    print("1: 文化")
    print("2: 人生")
    print("3: 生活")
    print("4: 健康")
    print("5: 教育")
    print("6: 职场")
    print("7: 财经")
    print("8: 娱乐")
    print("9: 艺术")
    print("10: 上网")
    print("11: 原创")
    a = input("请输入数字：")
    download_req = request.Request(url=url[int(a)], headers=head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('utf-8','ignore')
    soup = BeautifulSoup(download_html, 'lxml')
    texts = soup.find_all("ul",class_="arti_classical_u")
    texts = BeautifulSoup(str(texts), 'lxml')
    #print(texts)
    texts = texts.find_all(href=re.compile("shtml"), limit=5)
    aimurl=[]
    for x in texts:
        aimurl.append(x.get('href'))
    #print(aimurl)
    num = 0
    for x in aimurl:
        num += 1
        download_req = request.Request(url=x, headers=head)
        download_response = request.urlopen(download_req)
        download_html = download_response.read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(download_html, 'lxml')
        texts = soup.find_all("td", id="artContent")
        soup_text = BeautifulSoup(str(texts), 'lxml')
        # print(soup_text)
        write_flag = True
        soup_texts = soup_text.get_text('\n', 'br/').replace('[', '').replace(']', '')
        file = open('txt/' + str(num) + '.txt', 'w', encoding='utf-8')
        for x in soup.find_all(id='titiletext'):
            if x.string != None:
                title = soup.find(id='titiletext').string
                file.write(title)
        # 将爬取内容写入文件
        for each in soup_texts:
            if each == 'h':
                write_flag = False
            if write_flag == True and each != ' ':
                file.write(each)
            if write_flag == True and each == '\n':
                file.write('\n')
        file.write('\n\n')
        file.close()

        imgurllist = []
        url = soup_text.find_all("img")
        url = BeautifulSoup(str(url), 'lxml')
        for child in url.find_all('img'):
            if child.get('data-before-oversubscription-url') != None:
                imgurllist.append(child.get('data-before-oversubscription-url'))
        #print(imgurllist)
        x = 0
        for imgurl in imgurllist:
            req = requests.get(imgurl)
            with open('images/' + str(num) + '_' + str(x) + '.jpeg', 'wb') as wr:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        wr.write(chunk)
                        wr.flush()
            x += 1









