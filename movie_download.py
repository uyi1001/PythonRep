import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
movie = input('请输入你想搜索的电影：')
gbk = movie.encode('gbk')
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbk)
web = requests.get(url)
web.encoding = 'gbk'
analysis = BeautifulSoup(web.text,'html.parser')
part = analysis.find_all('tr',height='24')
for i in part:
    name = i.find('a')
    page_url = 'https://www.ygdy8.com'+name['href']
    download_web = requests.get(page_url)
    download_web.encoding = 'gbk'
    download_ana = BeautifulSoup(download_web.text,'html.parser')
    download_add = download_ana.find(style='WORD-WRAP: break-word')
    address = download_add.find('a')['href']
    print('电影名：{}\n下载链接：{}'.format(name.text,address))