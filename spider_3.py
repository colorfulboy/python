from bs4 import BeautifulSoup
import requests
import time
url='http://wh.xiaozhu.com/'
urls=['http://wh.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,10,1)]
headers={
    'Users-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; gr_user_id=ef233a15-bda3-4b28-a78d-4977aa2a232c; __utmt=1; xzuuid=8a790670; _ga=GA1.2.1014012791.1508919565; _gid=GA1.2.1407873559.1508919565; __utma=29082403.1014012791.1508919565.1508919649.1508926988.4; __utmb=29082403.3.10.1508926988; __utmc=29082403; __utmz=29082403.1508926988.4.4.utmcsr=baidu|utmccn=BDPZ|utmcmd=cpc|utmctr=PC%E6%A0%87%E9%A2%98|utmcct=pinzhuan; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=85933189-de09-4edd-b453-16e1588a07a6',
}
def get_1(url):
    web_data=requests.get(url,headers=headers)
    time.sleep(2)
    soup=BeautifulSoup(web_data.text,'lxml')
    titles=soup.select('.result_intro a')
    money=soup.select('.result_price')
    for title,m in zip(titles,money):
            data={
                '酒店名':title.get_text(),
                '价格':m.get_text(),
            }
            print(data)

for single_url in urls:
    get_1(single_url)