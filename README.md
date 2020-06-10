# Сrawler
A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing (web spidering).

Web search engines and some other sites use Web crawling or spidering software to update their web content or indices of others sites' web content. Web crawlers copy pages for processing by a search engine which indexes the downloaded pages so users can search more efficiently.

Crawlers consume resources on visited systems and often visit sites without approval. Issues of schedule, load, and "politeness" come into play when large collections of pages are accessed. Mechanisms exist for public sites not wishing to be crawled to make this known to the crawling agent. For example, including a robots.txt file can request bots to index only parts of a website, or nothing at all.

The number of Internet pages is extremely large; even the largest crawlers fall short of making a complete index. For this reason, search engines struggled to give relevant search results in the early years of the World Wide Web, before 2000. Today, relevant results are given almost instantly.

Crawlers can validate hyperlinks and HTML code. They can also be used for web scraping (see also data-driven programming). 

## How to download this program:

    git clone https://github.com/ghost171/crawler

## How to execute this program:

    python3 crawl1.py
## How to use the program?
In the start you have to choose what kind of service you want to exploit:
1. If you want to searching final page from start and page-on-the-depth-analytics. You must pick 1.
2. If tou want to anlytics all pages by some depth. You must pick 2.
### Service 1
If you choose service 1. You must enter start and final page.
Example:
https://kk.wikipedia.org/wiki/%D2%9A%D0%B0%D0%B7%D0%B0%D2%9B%D1%81%D1%82%D0%B0%D0%BD
https://kk.wikipedia.org/wiki/%D0%A3%D0%B8%D0%BA%D0%B8
### Service 1
If you choose service 2. You must enter start page anbd depth for analytics.
Example: 
https://kk.wikipedia.org/wiki/%D2%9A%D0%B0%D0%B7%D0%B0%D2%9B%D1%81%D1%82%D0%B0%D0%BD 
3
## What do this program?
This program contains two lines of purpouses:
1. Find the current site from the start site and print the biggest site on the path, and count of sites that we have visited.
2. Crawling all the sites to the three-depth length and print the biggest site on the path, and count of sites that we have visited.
### Regular expression:
We find the sites url with this regular expression:

    r"/wiki/%[a-zA-Z_\.0-9/%]+"
### Info for line 1:
In this function the start site and finish site you need indicate as arguments to function crawl(url, url2).
### Info for line 2
In this function the start site and crawl-level  you need indicate as arguments to function crawl_for_lvl(url, given_lvl).
### Downloading pages:
Also, we can download pages that met on our way with a bit of code:

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
## Functions:

    def get_urls(url):
    def print_report(crawled, lvl, max_url):
    def visit(url, marked, queue, crawled, url2, lvl, max_url):
    def crawl(url, url2):
    def print_report_for_lvl(crawled, max_url):
    def visit_for_url(url, marked, queue, crawled, lvl, max_url):
    def crawl_for_lvl(url, given_lvl):  
