import  requests
from    bs4 import BeautifulSoup
def Getnews(newsurl):
    reslut={}
    req =requests.get(newsurl)
    req.encoding = 'gbk'
    soup = BeautifulSoup(req.text, 'html.parser')
    reslut['新闻标题'] =soup.select('.post_content_main h1')[0].text
    reslut['新闻来源']=soup.select('.post_time_source a')[0].text
    reslut['新闻内容']='  '.join([p.text.strip() for p in soup.select('.post_text p')[0:-1]])
    return reslut
print(Getnews('http://news.163.com/17/1018/20/D12A99E200018AOQ.html'))
