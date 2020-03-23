import requests
import json

url='https://api.upcitemdb.com/prod/trial/lookup?'
paramaters={'upc':'012993441012'}
response=requests.get(url,paramaters)
#print(response.url)

content=response.content
data=json.loads(content)
#print(data)

book=data['items'][0]
book_title=book['title']
book_brand=book['brand']
print("Title :",book_title," ,Brand :" +book_brand)
