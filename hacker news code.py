import requests
from bs4 import BeautifulSoup
import pprint

# create html requests and parser
def create_soup(url, titlelink, subtext):
    res = requests.get(url)
    print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select(titlelink)
    subtext = soup.select(subtext)

    return links, subtext

url = 'https://news.ycombinator.com/'
url2 = 'https://news.ycombinator.com/news?p=2'

links, subtext = create_soup(url, '.titlelink', '.subtext')
links2, subtext2 = create_soup(url2, '.titlelink', '.subtext')

mega_links = links+links2
mega_subtext = subtext+subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda x: x['votes'], reverse = True)

# extract desired html elements
def create_custom_hn(links, subtext):
    hn = []
    for count, value in enumerate(links):
        title = value.getText()
        href = value.get('href', None)
        vote = subtext[count].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points>99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# pretty print 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
