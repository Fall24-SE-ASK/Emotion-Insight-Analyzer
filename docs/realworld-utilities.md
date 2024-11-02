# Utitity Codes

## twitter_scrap.py:
- Uses the `matplotlib` library for plotting graphs and `nltk` for natural language processing.

### twitter_sentiment_score():
- Reads tweets from the `twitt.txt` file.
- Tokenizes the text using `nltk.word_tokenize()`.
- Calculates sentiment scores.
- Plots the sentiment scores and returns the scores.

## fb_scrap.py:
- Similar to `twitter_scrap.py`, it reads Facebook posts, builds, trains, evaluates, and validates models, and returns the sentiment scores.

### Main function:
- `fb_sentiment_score()`

## newsScraper.py:
### scrapNews() function:
- Sets API key and search engine ID (CSE).
- Uses Google Custom Search API, retrieves articles, processes search results, and saves summaries to `news.json` file.

## amazon_test.py:
- The `AmazonReviewsSpider` class inherits from `scrapy.Spider`.
- The spider scrapes data from predefined URLs, and a parser extracts the data from the scraped result.
- The scraping result, including key metrics like star ratings, comments, and product reviews, is returned as a dictionary.
