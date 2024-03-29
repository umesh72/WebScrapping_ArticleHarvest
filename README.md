# ArticleHarvest_Scrapping the MeaningFull Information

ArticleHarvest is a Python script that fetches articles from a given website's sitemap, extracts various information from each article using the `newspaper` library, and then stores this information along with the article URL into a MongoDB database.

## Prerequisites

Before running the script, ensure you have installed the following libraries:

- `newspaper3k`
- `trafilatura`
- `pymongo`

You can install them using pip:

pip install newspaper3k trafilatura pymongo



Configuration

    Modify the MongoDB connection URI (mongodb://localhost:27017/) in the script to your MongoDB URI.
    Replace "article_database" with your desired database name in the script.

Usage

    Run the script scrape_and_store_articles.py.
    Monitor the console for execution updates.
    The extracted article information will be stored in your MongoDB database.

File Descriptions

   main.py: Main Python script for scraping and storing articles.
