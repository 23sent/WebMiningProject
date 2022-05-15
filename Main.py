from Website import Website
from UrlAttributes import UrlAttributes

class Main:
    def __init__(self):
        blog_urls_file = open("blog_urls.txt","r")
        blog_websites = []

        count = 0
        for url in blog_urls_file.read().split("\n"):
          if count > 10:
            break
          website = Website(url, 1)
          UrlAttributes.setAttributes(website)
          blog_websites.append(website)
          count += 1

        blog_urls_file.close()
        blog_website_obj_file = open("blogWebsiteObjects.csv","w")
        blog_website_obj_file.writelines(",".join(website.ATTRIBUTE_NAMES))
        blog_website_obj_file.write("\n")
        for website in blog_websites:
            blog_website_obj_file.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                website.url, website.isBlog, website.isWordpress, website.isBlogSpot, website.isUrlIncludeDate, website.isUrlIncludeDomainPostTitle,
                website.isUrlIncludeYearMonthPostTitle, website.isUrlIncludeDomainPostTitleNumbers, website.urlLen, website.numOfKeywords,
                website.isPrefixBlog, website.isMetaTagIncludeBlogKeyword, website.isUrlSuffixHTML, website.domainLen, website.pathNumberCount,
                website.lenOfPath
            ))
        blog_website_obj_file.close()

      

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