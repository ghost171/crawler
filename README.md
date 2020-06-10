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

## What do this program?
This program contains two lines of purpouses:
1) Find the current site from the start site and print the biggest site on the path, and count of sites that we have visited.
2) Crawling all the sites to the three-depth length and print the biggest site on the path, and count of sites that we have visited.
### Info for line 1):
In this function the start site and finish site you need indicate as arguments to function crawl(url, url2).
### Info for line 2):
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
