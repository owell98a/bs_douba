from urllib import request
from bs4 import BeautifulSoup

url='https://movie.douban.com/top250'
req=request.urlopen(url)
html=req.read().decode('utf-8')
bs=BeautifulSoup(html,'html5lib')
#print (bs)

con=bs.find('span',class_='next')
link=con.link
print(link)
print (link.get('href'))
url=url+link.get('href')


"""bs=self.get_conent(start_url)
         #bs=BeautifulSoup(self.get_conent(),'html5lib')
         con = bs.find('span', class_='next')
         link = con.link
         href=link.get('href')
         a_url=start_url+href
         print(a_url)
         (self.list_url).append(a_url)
         return self.list_url"""