from newspaper import Article
# pip install newspaper3k  # Before running, install it

from trafilatura import sitemaps
import pymongo
import time

def get_sitemap_urls(url):
    # extract sitemap URLs for given Homepage URL
    try:
        url_list = sitemaps.sitemap_search(url)
        return url_list[:25]  # Limit to first 25 URLs
    except Exception as err:
        print("Exception occurred:", err)

def extract_article_info(url):
    # Create an Article object
    article = Article(url, language="en")  # Language set to English

    # Download the article
    article.download()

    # Parse the article
    article.parse()

    # Perform natural language processing (NLP)
    article.nlp()

    # Extract information

    raw_html=article.html
    title = article.title
    text = article.text
    summary = article.summary
    keywords = article.keywords
    tags = list(article.tags)  # Convert set to list


    # Return extracted information along with URL
    return {

        "url": url,
        "raw_html":raw_html,
        "title": title,
        "text": text,
        "summary": summary,
        "keywords": keywords,
        "tags": tags,

    }

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["article_database"]  # Replace 'article_database' with your desired database name
collection = db["articles"]

# Get start time
start_time = time.time()

# Get sitemap URLs
sitemap_urls = get_sitemap_urls("https://www.example.com/")

# Loop through sitemap URLs
for url in sitemap_urls:
    article_info = extract_article_info(url)

    # Insert article information into MongoDB collection
    collection.insert_one(article_info)

# Get end time
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")

# Close MongoDB connection
client.close()
