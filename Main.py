import logging
from Website import Website
from UrlAttributes import UrlAttributes
from concurrent.futures import ProcessPoolExecutor
import time
class Main:
    ATTRIBUTE_NAMES = [
        "url",
        "isBlog",
        "isWordpress",
        "isBlogSpot",
        "isUrlIncludeDate",
        "isUrlIncludeDomainPostTitle",
        "isUrlIncludeYearMonthPostTitle",
        "isUrlIncludeDomainPostTitleNumbers",
        "urlLen",
        "numOfKeywords",
        "isPrefixBlog",
        "isMetaTagIncludeBlogKeyword",
        "isUrlSuffixHTML",
        "domainLen",
        "pathNumberCount",
        "lenOfPath",
    ]
    executor = ProcessPoolExecutor(59)
    blog_website_objs = []

    def __init__(self):
        blog_urls_file = open("random-10k-blog-urls.txt","r")      
        starttime = time.time()
        try:
            for r in self.executor.map(self.createWebsiteObj, blog_urls_file.read().split("\n")):
                self.blog_website_objs.append(r)
        except Exception as e:
            print(e)

        self.executor.shutdown(wait=True)        
        endtime = time.time()
        print((endtime - starttime) / 60, "minutes")
        print("Total", len(self.blog_website_objs))
        blog_urls_file.close()

        blog_website_obj_file = open("blog-dataset-10k.csv","w")
        # blog_website_obj_file.writelines(",".join(self.ATTRIBUTE_NAMES))
        blog_website_obj_file.write("\n")
        
        for website in self.blog_website_objs:
            blog_website_obj_file.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                website.url, website.isBlog, website.isWordpress, website.isBlogSpot, website.isUrlIncludeDate, website.isUrlIncludeDomainPostTitle,
                website.isUrlIncludeYearMonthPostTitle, website.isUrlIncludeDomainPostTitleNumbers, website.urlLen, website.numOfKeywords,
                website.isPrefixBlog, website.isMetaTagIncludeBlogKeyword, website.isUrlSuffixHTML, website.domainLen, website.pathNumberCount,
                website.lenOfPath
            ))
        blog_website_obj_file.close()

    def createWebsiteObj(self, url, isblog=1):
        website = Website(url, isblog)
        UrlAttributes.setAttributes(website)
        # self.blog_website_objs.append(website)
        print("Website object created for URL: " + url)
        return website

    #non_blog_urls_file = open("nonBlogUrls.txt","r")
    #nonblog_websites = []

    #for url in non_blog_urls_file.read().split("\n"):
    #  website = Website(url, 1)
    #  UrlAttributes.setAttributes(website)
    #  nonblog_websites.append(website)
    
    #non_blog_urls_file.close()

    #non_blog_website_obj_file = open("nonBlogWebsiteObjects.csv","w")
    #

 
if __name__ == "__main__":
    Main()