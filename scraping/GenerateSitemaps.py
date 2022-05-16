from Sitemap import Sitemap
import logging  
logging.basicConfig(filename='sitemapGen.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s', level=logging.DEBUG)


# Utku Sağocak
class GenerateSitemap():
    def __init__(self, urlsFilename, blogSitemapsFilename, blogUrlCountsname, max_scope = 1000 ):
        urls = open(urlsFilename, 'r')
        urls = urls.read().split('\n')

        blogSitemaps = open(blogSitemapsFilename, 'w')
        blogUrlCounts = open(blogUrlCountsname, 'w')

        totalUrlCount = 0
        index = 1
        for url in urls:
            site = Sitemap(url, max_scope)
            totalUrlCount += len(site.map)

            if len(site.map) > 0:
                blogSitemaps.write("\n".join(site.map) + "\n")

            countMsg = "{}) Domain: {}, Url Count: {}\n".format(index, url, len(site.map))
            print(countMsg, end="")
            blogUrlCounts.write(countMsg)

            index += 1


        blogSitemaps.close()
        blogUrlCounts.close()

        print("Total:", totalUrlCount)

    
if __name__ == "__main__":
    GenerateSitemap("output/non_blog_url.txt", "output/non_blog_sitemaps.txt", "output/non_blog_url_count.txt", 300)