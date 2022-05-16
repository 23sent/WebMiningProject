#Resul Bozburun

from bs4 import BeautifulSoup
import requests
from time import sleep
import logging

class GetBlogUrls:
    logging.basicConfig(filename='getUrls.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s')
    BLOGLIST_URL = "https://en.wikipedia.org/wiki/List_of_blogs"

    def __init__(self):
        page = requests.get(self.BLOGLIST_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        
        table = soup.find("table", class_="wikitable")
        table_body = table.find("tbody")
        rows = table_body.find_all("tr")
        
        wiki_urls = []
        for row in rows[1:]:
            try:
                href = row.find_all("td")[0].find("a")["href"]
            except TypeError as e:
                logging.error("Element does not have a HREF attr: {}".format(row.find_all("td")[0].text))
                continue
            url = "https://en.wikipedia.org" + href
            wiki_urls.append(url)

        blog_urls = []
        for wiki_url in wiki_urls:
            wiki_url_page = requests.get(wiki_url)
            wiki_blog_soup = BeautifulSoup(wiki_url_page.content, "html.parser")
            infobox = wiki_blog_soup.find("table", class_="infobox vcard")

            try:
                infobox_url = infobox.find("td", class_="infobox-data url")
            except AttributeError as e:
                logging.error("Element does not have an infobox table : {}".format(wiki_url))
                continue

            try: 
                blog_a_tag =infobox_url.find("a", class_="external text")
            except AttributeError as e:
                logging.error("Element does not have an A tag: {}".format(wiki_url))
                continue

            try:
                blog_url = blog_a_tag["href"]
            except TypeError:
                logging.error("Element does not have a HREF tag: {}".format(wiki_url))
                continue

            if blog_url not in blog_urls:
                blog_urls.append(blog_url)
        
        blog_urls_file = open("blog_urls.txt","w")
        for url in blog_urls:
            blog_urls_file.write(url+'\n')
        blog_urls_file.close()


class GetUrlsFromBuiltWith:
    logging.basicConfig(filename='getUrls.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s')
    
    def __init__(self, builtwith_urls):
        self.builtwith_urls = builtwith_urls
        urls = []
        for url in self.builtwith_urls:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            rows = soup.find_all("tr")
            for row in rows:
                if row.has_attr("data-domain"):
                    urls.append("http://"+row["data-domain"])
            
        non_blog_urls_file = open("nonBlogUrls.txt","a+")
        for url in urls:
            non_blog_urls_file.write(url+"\n")
        non_blog_urls_file.close()

 
class GetBlogUrlsFromBuiltWith:
    logging.basicConfig(filename='getUrls.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s')
    BUILTWITH_URL = "https://builtwith.com/website-lists/Blog"

    def __init__(self):
        self.builtwith_urls = self.BUILTWITH_URL
        blog_urls = []
        for url in [self.builtwith_urls]:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            rows = soup.find_all("tr")
            for row in rows:
                if row.has_attr("data-domain"):
                    blog_urls.append("http://"+row["data-domain"])
            
        blog_urls_file = open("blog_urls.txt","a+")
        for url in blog_urls:
            blog_urls_file.write(url+'\n')
        blog_urls_file.close()

if __name__ == "__main__":
    #Get list of blog urls from wikipedia and builtwith
    #GetBlogUrls()
    #GetBlogUrlsFromBuiltWith()

    #Get list of nonblog urls from builtwith
    ECOMMERCELIST_URLS = ["https://trends.builtwith.com/websitelist/WooCommerce-Checkout", "https://trends.builtwith.com/websitelist/BigCommerce", "https://trends.builtwith.com/websitelist/Magento-Enterprise", "https://trends.builtwith.com/websitelist/Shopify-Plus", "https://trends.builtwith.com/websitelist/PrestaShop", "https://trends.builtwith.com/websitelist/Demandware"]
    PORTFOLIOLIST_URLS = ["https://trends.builtwith.com/websitelist/Nimble-Portfolio/Historical","https://trends.builtwith.com/websitelist/Grand-Portfolio/Historical", "https://trends.builtwith.com/websitelist/Gallery-Portfolio/Historical", ]
    #GetUrlsFromBuiltWith(PORTFOLIOLIST_URLS)

