
# CENG-3548 Blog or Non-blog Detection


## Abstract
We evaluate a model to classify whether a web page is a blog or not.
Firstly, to collect data, we was collect example blog and non-blog domains from the web. Then we got random URLs from these web pages sitemaps and we generated 14 different attributes per every URL by accessing and parsing HTML contents or paths.
As a result, we got 2 datasets one of them contains information about blogs and other non-blog web pages.

After the data collection step, we loaded our data to a Jupyter Notebook and normalize it. Then we developed machine learning models with **Naive Bayes**, **KNN**, **C-Support Vector** and **Decision Tree** algorithms. 
	Finally we train a KNN classifier that has ~98% accuracy.
	
List of technologies we used:
```bash
- Python with BeatifulSoup and requests libraries to collect data from web pages.
- Python with pandas, seaborn and sklearn libraries for data processing, visualization and model evaluation.
Jupyter Notebook 
```


## Project Structure
```bash
ProjectRoot
       └─── data
       |             |─── blog-dataset-2k.csv
       |             └─── nonblog-dataset-1k
       |─── scraping
       |	 |─── output
       |	 |                |─── blog_sitemaps.txt
       |	 |                |─── blog_urls.txt
       |	 |                |─── non_blog_ sitemaps.txt
       |	 |                └─── non_blog _urls.txt
       |	 |
       |	 |─── GenerateSitemaps.py
       |	 |─── GetUrls.py
       |	 |─── Main.py
       |	 |─── UrlAttributes.py
       |	 |─── Sitemap.py
       |	 └─── Website.py
       |─── model
       | 	  └─── Model.pynb
       └─── requirements.txt

```



## Authors

- [@rbozburun - Resul Bozburun](https://github.com/rbozburun)
- [@23sent - Utku Sağocak](https://github.com/23sent)



