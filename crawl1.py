from bs4 import BeautifulSoup
from collections import deque
import sys
from urllib.parse import urljoin, unquote
import requests
from urllib.request import urlopen
import re
import multiprocessing as mp
import requests
import re
import urllib.request, urllib.error, urllib.parse

urlTemplate = r"/wiki/%[a-zA-Z_\.0-9/%]+"
baseURL = "https://kk.wikipedia.org"


def getFilename_fromCd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def get_urls(url):
    print("crawling " + unquote(url))
    answer = requests.get(url=url)
    urls = re.findall(urlTemplate, answer.text)
    for url in urls:
        yield baseURL + url

def print_report(crawled, lvl, max_url):
    print("URL WAS FINDED!")
    print("Crowled sites:", crawled)
    print("Site with biggest quantity of symbols:")
    answer = requests.get(max_url)
    print(unquote(max_url) + str(" : ") + str(len(answer.text)))
    print("Your site is on level", lvl) 


def visit(url, marked, queue, crawled, url2, lvl, max_url):
    for url in get_urls(url):
        crawled += 1
        if url in marked:
            continue
        if url == url2:
            print_report(crawled, lvl, max_url)
            exit()
        marked.add(url)
        queue.append(url)
    return marked, queue, crawled

def crawl(url, url2):
    queue = deque([])
    marked = set()
    crawled = 0
    queue.append(url)
    marked.add(url)
    lvl = 1
    len_queue_old = 1
    max_url = url
    while queue:
        url = queue.popleft()
        len_queue_old -= 1
        marked, queue, crawled = visit(url, marked, queue, crawled, url2, lvl, max_url)
        answer = requests.get(url, allow_redirects=True)
        answer1 = urllib.request.urlopen(url)
        webContent = answer1.read()
        f = open('wikikz.html' + str(lvl), 'wb')
        f.write(webContent)
        f.close()
        filename = getFilename_fromCd(r.headers.get('content-disposition'))
        open(filename, 'wb').write(r.content)

        answer_max_url = requests.get(max_url)
        if (len(answer.text) > len(answer_max_url.text)):
            max_url = url
        if (len_queue_old == 0):
            len_queue_old = len(queue)
            lvl += 1


def print_report_for_lvl(crawled, max_url):
    print("DEPTH IS REACHED!")
    print("Crowled sites:", crawled)
    print("Site with biggest quantity of symbols:")
    answer = requests.get(max_url)
    print(unquote(max_url) + str(" : ") + str(len(answer.text)))

def visit_for_url(url, marked, queue, crawled, lvl, max_url):
    for url in get_urls(url):
        crawled += 1
        if url in marked:
            continue
        marked.add(url)
        queue.append(url)
    return marked, queue, crawled

def crawl_for_lvl(url, given_lvl):  
    queue = deque([])
    marked = set()
    crawled = 0
    queue.append(url)
    marked.add(url)
    lvl = 1
    len_queue_old = 1
    max_url = url
    while queue:
        url = queue.popleft()
        len_queue_old -= 1
        marked, queue, crawled = visit_for_url(url, marked, queue, crawled, lvl, max_url)
        answer = requests.get(url, allow_redirects=True)
        answer1 = urllib.request.urlopen(url)
        webContent = answer1.read()
        f = open('wikikz.html' + str(lvl), 'wb')
        f.write(webContent)
        f.close()
        answer_max_url = requests.get(max_url)
        if (len(answer.text) > len(answer_max_url.text)):
            max_url = url
        if (len_queue_old == 0):
            len_queue_old = len(queue)
            lvl += 1
        if (lvl == given_lvl):
            print_report_for_lvl(crawled, max_url)
            exit()
        


crawl_for_lvl("https://kk.wikipedia.org/wiki/%D2%9A%D0%B0%D0%B7%D0%B0%D2%9B%D1%81%D1%82%D0%B0%D0%BD", 3)

