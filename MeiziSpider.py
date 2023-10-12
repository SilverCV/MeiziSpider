#---coding--:--UTF-8---
import os
import requests
from bs4 import BeautifulSoup

def getHtml(url,encoding='utf-8'):
    headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    try:        
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = encoding
        return r.text
    except Exception as e:
        return None
def getPictUrls(html):
    soup = BeautifulSoup(html)
    for single in soup.find_all('img',attrs={'class':'lazy'}):
        yield single.get('data-original')
def DownLoadPic(picUrl):
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    bathdir = os.path.dirname(__file__)
    dir = os.path.join(bathdir,"img")
    if not os.path.exists(dir):
        os.mkdir(dir)
    fileName = os.path.join(dir,picUrl.split('/')[-1])
    with open(fileName,'wb') as f:
        f.write(requests.get(picUrl,headers=headers).content)

if __name__ == "__main__":
    for i in range(300):
        url = 'https://www.mzitu.com/zipai/comment-page-{}/#comments'.format(i)
        html = getHtml(url)
        for PicUrl in getPictUrls(html):
            DownLoadPic(PicUrl)
