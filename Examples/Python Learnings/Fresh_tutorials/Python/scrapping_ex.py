from bs4 import BeautifulSoup
import requests
import csv

url = 'https://coreyms.com/'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())


csv_file = open('test_scrap.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'youtube link'])

for article in soup.find_all('article'):
    # print(article.prettify())
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', {'class': 'entry-content'}).p.text
    print(summary)

    try:
        youtube_link = article.find('iframe', {'class': "youtube-player"}).get('src')
        video_id = youtube_link.split('/')[4]
        video_id = video_id.split('?')[0]
        final_youtube_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        final_youtube_link = None
    print(final_youtube_link)

    csv_writer.writerow([headline, summary, final_youtube_link])

csv_file.close()
