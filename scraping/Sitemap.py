import requests
from bs4 import BeautifulSoup
import urllib.robotparser as robotparser
from urllib.parse import urljoin
import logging

ALLOW_REDIRECTS = True

# Utku Sağocak
class Sitemap():
  def __init__(self, domain, max_scope = 1000):
    self.MAX_SCOPE = max_scope
    self.domain = domain
    self.map = set()
    self.generateMap()

  def checkDomain(self):
    logging.debug("Check domain: {}".format(self.domain))
    try:
      response =  requests.get(self.domain)
      if (response.status_code != 200):
        logging.error("Request failed, status code: {}".format(response.status_code))
        return False
    except Exception as error:
      logging.error(error)
      return False
    return True

  def generateMap(self):
    if not self.checkDomain():
      return self.map
    else:
      self.map.add(self.domain)

    sitemapXMLs = self.getSitemapXml()
    if (sitemapXMLs):
      for sitemapUrl in sitemapXMLs:
          self.parseUrlsFromSitemap(sitemapUrl)

  def getSitemapXml(self):
    try:
        robots_url = urljoin(self.domain, 'robots.txt')
        parser = robotparser.RobotFileParser()
        parser.set_url(robots_url)
        parser.read()
        sitemaps = parser.site_maps()
        if sitemaps != None:
            return sitemaps
        else:
            return [urljoin(self.domain, 'sitemap.xml')]
    except Exception as e:
        return []

  def parseUrlsFromSitemap(self, sitemapUrl):
    if len(self.map) > self.MAX_SCOPE: 
      return False

    logging.debug("Request to: {}".format(sitemapUrl))
    try:
      response =  requests.get(sitemapUrl, allow_redirects=ALLOW_REDIRECTS)
      if (response.status_code != 200):
        logging.error("Request failed, status code: {}".format(response.status_code))
        return False

    except Exception as error:
      logging.error(error)
      return False

    soup = BeautifulSoup(response.content, "xml")

    for element in soup.findAll('url'):
      if len(self.map) > self.MAX_SCOPE: 
        return False

      self.map.add(element.find("loc").string)

    sitemapTags = soup.findAll('sitemap')
    if sitemapTags:
      for element in sitemapTags:
          sitemap_url = element.find('loc').string
          self.parseUrlsFromSitemap(sitemap_url)


if __name__ == "__main__":
  logging.basicConfig(filename='sitemapGen.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s', level=logging.DEBUG)
  site = Sitemap("https://getbootstrap.com") 
  print(len(site.map))