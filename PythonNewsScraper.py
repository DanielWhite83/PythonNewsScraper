#import what we need
from requests_html import HTMLSession
session = HTMLSession()


#use session to get the page
google_session = session.get('https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
google_session.html.render(sleep=1, scrolldown=10)

#find all the articles by using inspect element and create blank list
articles = google_session.html.find('article')
newslist = []

#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        title = newsitem.text
        link = newsitem.absolute_links
        newsarticle = {
            'title': title,
            'link': link 
        }
        newslist.append(newsarticle)
    except:
       pass

# target titles with key words
keywords = ['science', 'telescope', 'scientists', 'space', 'study', 'studies', 'research', 'black hole']
for i in newslist:
    for j in keywords:
        cf_title = i['title'].casefold()
        if j.casefold() in cf_title:
            print(i['title'])