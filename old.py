import re
from bs4 import BeautifulSoup
import requests
import argparse

# miner sınıfı -> miner(mining_query)
# arparse

class Miner():
    URL_GOOGLE = "https://www.google.com/search?q=siber"

    def __init__(self, query):
        print("Searcing for: {}".format(query))
        self.URL_GOOGLE = self.URL_GOOGLE + query
        
        
        
    def googleQueryParser(self, query):
        page = requests.get(self.URL_GOOGLE)
        soup_google_query = BeautifulSoup(page.content, "html.parser")
        links = []
        for link in soup_google_query.find_all('a'):

def main():
    parser = argparse.ArgumentParser(description="Crawl web pages and do mining process to findin 'email address, name, address' triples.")
    parser.add_argument('-q', '--query', help="Search query")
    args = parser.parse_args()
    query = args.query

    miner = Miner(query)

if __name__ == "__main__":
    run = main()