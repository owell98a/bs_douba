from urllib import request
from bs4 import BeautifulSoup

class get_Comment:
    def __init__(self,list_url=[]):
        self.list_url = list_url
    def get_conent(self,url):
        req=request.urlopen(url)
        conent=req.read().decode('utf-8')
        bs = BeautifulSoup(conent, 'html5lib')
        return bs
    def get_data(self,html):
        #bs = BeautifulSoup(html, 'html5lib')
        content = html.findAll('div', class_='item')
        for i in content:
            a = i.a
            # print(i)
            img = a.img
            print(img.get('alt'))
            # print(img.get('src'))
            sp = i.find('div', class_='star')
            # print(sp)
            ss = sp.find('span', class_='rating_num')
            print(ss.text)
            has_attr = lambda tag: not tag.attrs  # 定义匿名函数，判断是否存在任何属性
            voters = sp.find(has_attr)
            print(voters.text)

    def get_parse_url(self,url):

        parse_list = []
        for i in range(10):
            html_url = url + f'?start={25 * i}&amp;filter='
            parse_list.append(html_url)
        return parse_list

    def start(self,start_url):
        t=self.get_parse_url(start_url)
        for i in t:
            html=self.get_conent(i)
            self.get_data(html)

if __name__=='__main__':
    url='https://movie.douban.com/top250'
    gd=get_Comment()
    gd.start(url)
