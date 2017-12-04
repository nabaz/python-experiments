import sys
import requests
import bs4
from bs4 import BeautifulSoup
from collections import Counter
from urlparse import urljoin

class WikiCrawler():
    WIKI_LINK = "https://en.wikipedia.org/wiki/"
    PHILOSOPHY = "Philosophy"

    def soup(self, content):
        '''
        here we get content and sanitize them to make sure we only get a tags with no parentheses
        '''
        soup = BeautifulSoup(content, "html.parser")
        all_p_tags = soup.find("div", {"id":"mw-content-text"}).find_all('p') # main text area only
        for p_tags in all_p_tags:
            context = ''
            for element in p_tags:
                if type(element) == bs4.element.NavigableString: # Only html string
                    context += element
                elif type(element) == bs4.element.Tag and element.name == 'a': # only a tags
                    if self.check_parentheses(context):
                        return element
                else:
                    context += element.get_text()
        return None

    def check_parentheses(self, context):
        counter = 0
        for c in context:
            if c == '(':
                counter += 1
            elif c == ')':
                counter -= 1
        return counter == 0

    def presentage_of_pages_lead_to_philosophy(self, urls):
        i = 0
        for url in urls:
            if self.leads_to_philosophy(url, 0) != -1:
                i += 1
        return float("{0:.2f}".format(i * 100 / len(urls)))

    def random_presentage_of_pages_lead_to_philosophy(self, m):
        links = []
        for i in range(m):
            p = self.WIKI_LINK + 'Special:Random'
            links.append(p)
        return self.presentage_of_pages_lead_to_philosophy(links)

    def distribution(self, urls):
        d = []
        for url in urls:
            re = self.leads_to_philosophy(url, 0)
            if re != -1:
                d.append(re)
        return d

    def random_distribution(self, m):
        urls = []
        for i in range(m):
            p = self.WIKI_LINK + "Special:Random"
            urls.append(p)
        return Counter(self.distribution(urls))

    def leads_to_philosophy(self, url, path_length=0):
        re = requests.get(url)
        visited_url=[]
        content = re.text
        philosophy_url = self.WIKI_LINK + 'Philosophy'
        if re.url == philosophy_url:
            return path_length
        elif re.url in visited_url:
            return -1
        else:
            link = self.soup(content)
            if link and link.attrs.has_key('href'):
                url = urljoin(re.url, link.attrs['href'])
                path_length += 1
                visited_url.append(re.url)
                return self.leads_to_philosophy(url, path_length)
            else:
                return -1

if __name__ == '__main__':
    c = WikiCrawler()
    urls = ['https://en.wikipedia.org/wiki/Art', 'https://en.wikipedia.org/wiki/Hawaii', 'https://en.wikipedia.org/wiki/Global']
    n = 5
    print "percentage of page lead to philosophy: {}%".format(c.presentage_of_pages_lead_to_philosophy(urls))
    print "random percentage of page lead to philosophy: {}%".format(c.random_presentage_of_pages_lead_to_philosophy(n))
    print c.random_distribution(n)
