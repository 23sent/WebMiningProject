from Sitemap import Sitemap
import logging  
logging.basicConfig(filename='sitemapGen.log', filemode='w', format='%(asctime)s - %(levelname)s:  %(message)s', level=logging.DEBUG)


urls = open('blog_urls_v2.txt', 'r')
urls = urls.read().split('\n')

blogSitemaps = open('blog_sitemaps_v3.txt', 'w')
blogUrlCounts = open('blog_url_counts_v3.txt', 'w')

totalUrlCount = 0
index = 1
for url in urls:
  site = Sitemap(url)
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