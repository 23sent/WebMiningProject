from Website import Website
import logging  
from bs4 import BeautifulSoup
import requests
from time import sleep
import re

logging.basicConfig(filename='UrlAttributes.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s', level=logging.DEBUG)

#TODO
# Custom user-agent eklenecek.
#
class UrlAttributes():
    def __init__(self, url):
        self.url = url

        # create website obj with self.url
        # crawl website url to get attrs

        website = Website(url=self.url)
        website.isWordpress = self.isWordpress(website)
        print(website.isWordpress)

    #Check the url include "wp-"
    def isWordpress(self, website):
        wp_pattern = ".*/wp-[a-zA-Z].*"
        return 1 if re.search(wp_pattern, website.url) else 0

    #Check the url include .blogspot
    def isBlogSpot(self):
        pass

    #Check the url include domain/year/month/day/random_numbers/
    def isUrlIncludeDateTime(self):
        pass

    #Check the url include domain/post_title -> /2022/5/13/23070197/
    def isUrlIncludeDomainPostTitle(self):
        pass

    #Check the url include /year/month/post_title -> /2022/05/post-title
    def isUrlIncludeYearMonthPostTitlifehacker(self):
        pass

    #Check the url domain/post_title-numbers
    def isUrlIncludeDomainPostTitleNumbers(self):
        pass

    #Return the length of the URL
    def urlLen(self):
        pass

    #Return number of "blog" keywords into page content
    def numOfBlogKeyword(self):
        pass

    #Return number of ald words into page content
    def numOfKeywords(self):
        pass

    #Check the url starts with "blog."
    def isPrefixBlog(self):
        pass

    #Check <meta property="og:description"> tag is include "blog" keyword
    def isMetaTagIncludeBlogKeyword(self):
        pass

    #Check the URL ends with "".html"
    def isUrlSuffixHTML(self):
        pass
        
        

        

if __name__ == "__main__":
  att = UrlAttributes("https://www.airlinereporter.com/2009/11/oops-pilots-on-qantas-airlines-forget-to-lower-landing-gear/")