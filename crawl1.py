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
        answer = requests.get(url)
        try:
            answer1 = urllib.request.urlopen(url)
            webContent = answer1.read()
            url_for_download = ""
            iterator = len(unquote(url)) - 1
            while(url[iterator] != "/"):
                url_for_download += (unquote(url)[iterator])
                iterator -= 1
            url_for_download = url_for_download[::-1]
            f = open('WikiKz' + str(url_for_download) + str(lvl) + '.html', "w+")
            f.write(str(webContent))
            f.close()
        except:
            pass
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
        answer = requests.get(url)
        try:
            answer1 = urllib.request.urlopen(url)
            webContent = answer1.read()
            url_for_download = ""
            iterator = len(unquote(url)) - 1
            while(url[iterator] != "/"):
                url_for_download += (unquote(url)[iterator])
                iterator -= 1
            url_for_download = url_for_download[::-1]
            f = open('WikiKz' + str(url_for_download) + str(lvl) + '.html', "w+")
            f.write(str(webContent))
            f.close()
        except:
            pass
        
        answer_max_url = requests.get(max_url)
        if (len(answer.text) > len(answer_max_url.text)):
            max_url = url
        if (len_queue_old == 0):
            len_queue_old = len(queue)
            lvl += 1
        if (lvl == given_lvl):
            print_report_for_lvl(crawled, max_url)
            exit()
        
print("To use the program choose your service:")
print("1. Find page from another page and statistics about path pages. Pick 1")
print("2. Analyse all pages on 3 depth. Pick 2")
service = input()
if( service == 1):
    print("Enter the start and final page ")
    print("Start page:")
    start_page = input()
    print("Final page")
    final_page = input()
    crawl(start_page, final_page)
elif (service == 2):
    print("Enter the depth of search and the final page")
    print("DEpth:")
    depth = input()
    print("Start page")
    start_page = input()
    crawl_for_lvl(start_page, depth)
else:
    print("Error! Receive 1 or 2.")
    exit()

