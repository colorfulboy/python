import requests
from   bs4 import BeautifulSoup

urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(1,10,25)]
def get_douban_top250(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Cookie':'ll="118106"; bid=WNTm4Jy1Cu8; __yadk_uid=FZrtwuwYwteA5OqMyI9yRyLQBhbydSiO; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1509196457%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DwhHWlYTbBX71ZuThPocRYZCJoxF7v2Bpxr0ryYrRLeoGyy-VNUBtEkQb7NA8AZPe%26wd%3D%26eqid%3D9fac7f9e00044cb50000000259f482a5%22%5D; _vwo_uuid_v2=1594C81486A31FDCC24B8C338E367DD4|c9344edc36455ecdb27320b075f6a8ec; _pk_id.100001.4cf6=e3aee7a9bde0d407.1508567667.2.1509196561.1508569056.; _pk_ses.100001.4cf6=*; __utma=30149280.938570623.1508567663.1508567663.1509196457.2; __utmb=30149280.0.10.1509196457; __utmc=30149280; __utmz=30149280.1509196457.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.516546784.1508567668.1508567688.1509196457.3; __utmb=223695111.0.10.1509196457; __utmc=223695111; __utmz=223695111.1509196457.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
    }
    url = 'https://movie.douban.com/top250'
    req=requests.get(url,headers=headers)
    soup=BeautifulSoup(req.text,'lxml')
    title=soup.select('.hd')
    grade=soup.select('.rating_num')
    classic_line=soup.select('.inq')
    for t,g,c in zip(title,grade,classic_line):
        data={
            '标题':t.get_text(),
            '评分':g.get_text(),
            '经典台词':c.get_text()
        }
        print(data)
get_douban_top250('https://movie.douban.com/top250')
for single_url in urls:
    get_douban_top250(single_url)




