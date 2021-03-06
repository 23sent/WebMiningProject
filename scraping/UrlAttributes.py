#Resul Bozburun & Utku Sağocak

import os
from tokenize import String
from Website import Website
import logging  
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse

logging.basicConfig(filename='UrlAttributes.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s', level=logging.DEBUG)

class UrlAttributes():
    @staticmethod
    def setAttributes(website):
        try:
            page = requests.get(website.url)
            if page.status_code != 200:
                print("Request failed: ", website.url)
        except Exception as e:
            print(e)

        soup = BeautifulSoup(page.content, "html.parser")

        website.isWordpress = UrlAttributes.isWordpress(website)
        website.isBlogSpot = UrlAttributes.isBlogSpot(website)
        website.isUrlIncludeDomainPostTitle = UrlAttributes.isUrlIncludeDomainPostTitle(website, soup)
        website.numOfBlogKeywords = UrlAttributes.numOfBlogKeywords(website, soup)
        website.numOfKeywords = UrlAttributes.numOfKeywords(website, soup)
        website.domainLen = UrlAttributes.lenOfDomain(website)
        website.isUrlIncludeDate = UrlAttributes.isUrlIncludeDate(website)
        website.isUrlIncludeYearMonthPostTitle = UrlAttributes.isUrlIncludeYearMonthPostTitle(website)        
        website.pathNumberCount = UrlAttributes.pathNumberCount(website)
        website.urlLen = UrlAttributes.urlLen(website)
        website.isIncludeBlog = UrlAttributes.isIncludeBlog(website)
        website.isMetaTagIncludeBlogKeyword = UrlAttributes.isMetaTagIncludeBlogKeyword(soup)
        website.isUrlSuffixHTML = UrlAttributes.isUrlSuffixHTML(website)
        website.lenOfPath = UrlAttributes.lenOfPath(website)
        
        return website

    #Utku
    #netloc
    def lenOfDomain(website):
        parsedUrl = urlparse(website.url)
        domain = parsedUrl.netloc

        return len(domain)

    #Resul
    #Check the url include "wp-"
    def isWordpress(website):
        wp_pattern = ".*/wp-[a-zA-Z].*"
        return 1 if re.search(wp_pattern, website.url) else 0

    #Resul
    #Check the url include .blogspot
    def isBlogSpot(website):
        blogspot_pattern = ".*\.blogspot\.com/.*"
        return 1 if re.search(blogspot_pattern, website.url) else 0
        
    #Utku
    #Check the url include domain/year/month/day/
    def isUrlIncludeDate(website):
        date_time_pattern = "/(19|20)\d{2}(/(0?[1-9]|1[012]))?(/(\d|3[01]))?/"
        return 1 if re.search(date_time_pattern, website.url) else 0

    #Check the url include domain/post_title  => RESUL
    def isUrlIncludeDomainPostTitle(website, soup):
        domain = urlparse(website.url).netloc
        path = urlparse(website.url).path

        if "." in domain: 
            domain = domain.replace(".","\.")
        domain_post_title_pattern = ".*{}/([a-zA-Z]+(-[a-zA-Z0-9]+)+)$".format(domain)

        #Check certainity of post title into url if format is domain/text-values
        if re.search(domain_post_title_pattern, website.url):
            path = path.replace("/","")
            path_words = path.split("-")
            title = soup.title.text

            #Remove special chars in title
            title_special_removed = re.sub('[^a-zA-Z.\d\s]', '', title).lower()

            numOfOccurence = 0
            for word in path_words:
                if word.lower() in title_special_removed:
                    numOfOccurence += 1
            
            certainity = numOfOccurence / len(path_words)
            # print("Title: " + title_special_removed + "\n Certainity: " +str(certainity))
            return 1 if certainity > 0.5 else 0
        return 0


    #Utku
    #Check the url include /year/month/post_title -> /2022/05/post-title
    def isUrlIncludeYearMonthPostTitle(website):
        path = urlparse(website.url).path
        year_month_posttitle_pattern = "\/(19|20)\d{2}(\/(0?[1-9]|1[012]))?\/(\w|-|_)*(\.\w*\/*)?$"
        return 1 if re.search(year_month_posttitle_pattern, path) else 0


    #Utku 
    def pathNumberCount(website):
        path = urlparse(website.url).path
        return len(re.findall("\d", path))

    #Utku
    #Return the length of the URL
    def urlLen(website):
        return len(website.url)

    #Resul
    #Return number of "blog" keywords into page content
    def numOfBlogKeywords(website, soup):
        return str(soup).count("blog")

    #Resul
    #Return number of ald words into page content
    def numOfKeywords(website, soup):
        word_pattern = "\w+"
        return len(re.findall(word_pattern, str(soup)))

    #Utku
    #Check the domain includes "blog"
    def isIncludeBlog(website):
        parsedUrl = urlparse(website.url)
        return 1 if re.search("blog", parsedUrl.hostname) else 0


    #Utku
    #Check <meta property="og:description"> tag is include "blog" keyword
    def isMetaTagIncludeBlogKeyword(soup):
        description = soup.find("meta", attrs={'name':'description'})
        if description and description["content"] and  re.search("blog", description["content"]):
            return 1
        
        description = soup.find("meta", attrs={'property':'og:description'})
        if description and description["content"] and  re.search("blog", description["content"]):
            return 1
        return 0

    #Utku
    #Check the URL ends with "".html"
    def isUrlSuffixHTML(website):
        path = urlparse(website.url).path
        return 1 if re.search("\.html(\/*)$", path) else 0
    
    #Utku
    def lenOfPath(website):
        path = urlparse(website.url).path
        if not len(path):
            return 0
        return len(path.strip("/").split("/"))

if __name__ == "__main__":
    att = UrlAttributes.setAttributes(Website("http://ibj.com", 0))
