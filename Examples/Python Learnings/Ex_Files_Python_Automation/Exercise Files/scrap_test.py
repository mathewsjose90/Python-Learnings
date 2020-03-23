import requests
from bs4 import BeautifulSoup
url='http://quotes.toscrape.com/'

response=requests.get(url)
data=response.text
#print(data)
soup=BeautifulSoup(data,'lxml')
quotes=soup.find_all('div',class_='quote')
for quote in quotes:
    #find text
    data=quote.find('span',class_='text')
    print('Quote:'+data.text)
    #find author
    author_info=quote.find('small',class_="author")
    print('Author:'+author_info.text)
    #find tags
    tags_info=quote.find_all('a', class_="tag")
    tags=[]
    for tag_name in tags_info:
        tags.append(tag_name.text)
    print('Tags:'+str(tags))

