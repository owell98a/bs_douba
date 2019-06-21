from urllib import request
from bs4 import BeautifulSoup

url='https://movie.douban.com/top250'
req=request.urlopen(url)
html=req.read().decode('utf-8')
bs=BeautifulSoup(html,'html5lib')
#print (bs)

content=bs.findAll('div',class_='item')
print(type(content))
for i in content:
    a = i.a
    #print(i)
    img = a.img
    print(img.get('alt'))
    # print(img.get('src'))

    sp = i.find('div', class_='star')
    #print(sp)
    ss = sp.find('span', class_='rating_num')
    print(ss.text)
    has_attr=lambda tag : not tag.attrs    #定义匿名函数，判断是否存在任何属性
    voters=sp.find(has_attr)
    print(voters.text)