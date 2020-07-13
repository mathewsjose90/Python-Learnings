import requests 
from bs4 import BeautifulSoup

url='https://scrapingclub.com/exercise/list_basic/?page=2'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
dress_items=soup.find_all('div',class_='col-lg-4 col-md-6 mb-4')

for pos,dress in enumerate(dress_items,start=1):
    dress_name=dress.find('h4',class_="card-title")
    dress_price=dress.find('h5')
    print(str(pos)+"==>Dress Name:"+dress_name.text.strip()+'==> Dress Price:'+dress_price.text)

#check multiple pages

pages=soup.find('ul',class_='pagination') 
links=pages.find_all('a',class_='page-link')  
urls=[]
for link in links:
    pagenum=int(link.text) if link.text.isdigit() else None
    if pagenum:
        x=link.get('href')
        urls.append(x)
print(urls)
base_url='https://scrapingclub.com/exercise/list_basic/'
for link in urls:
    new_url=base_url+link
    response=requests.get(new_url)
    soup=BeautifulSoup(response.text,'lxml')
    dress_items=soup.find_all('div',class_='col-lg-4 col-md-6 mb-4')
    print("Details for "+new_url)

    for pos,dress in enumerate(dress_items,start=1):
        dress_name=dress.find('h4',class_="card-title")
        dress_price=dress.find('h5')
        print(str(pos)+"==>Dress Name:"+dress_name.text.strip()+'==> Dress Price:'+dress_price.text)   