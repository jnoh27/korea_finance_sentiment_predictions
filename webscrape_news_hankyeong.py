import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Function to clean and extract text
def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()
    return text


'''
Scrape article from page
'''

# Function to scrape article links from a page
def scrape_article_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    article_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '/article/' in href:  # Filter for links that lead to articles
            article_links.append(href)

    return list(set(article_links))  # Remove duplicates


# Base URL (Korean Economics)
base_url = 'https://www.hankyung.com/all-news-economy'

# Scrape links from the first 5 pages
article_links = []
for page in range(1, 10):
    url = f"{base_url}?page={page}"
    links = scrape_article_links(url)
    article_links.extend(links)
    print(f"Scraped {len(links)} article links from page {page}")

# Print the collected article links
print(f"Total article links collected: {len(article_links)}")

'''
Scrape content from article
'''

# Function to scrape content from a single article page
def scrape_article_content(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('h1.headline').text.strip()  # Adjust based on the site structure
    content = soup.select_one('div.article-body').text.strip()
    date = soup.select_one('span.txt-date').text.strip()

    return {'title': title, 'content': content, 'date': date}


# Scrape content from each collected article link
articles = []
for link in article_links:
    try:
        article = scrape_article_content(link)
        articles.append(article)
        print(f"Scraped article: {article['title']}")
    except Exception as e:
        print(f"Failed to scrape {link}: {e}")

# Save the articles to a CSV file
df = pd.DataFrame(articles)
df.to_csv('korean_financial_news_full.csv', index=False)
print("Full articles scraped and data saved to 'korean_financial_news_full.csv'")