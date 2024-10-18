import nltk
import streamlit as st
from newsapi import NewsApiClient
from transformers import pipeline

# Download NLTK data
nltk.download('punkt', download_dir='./__pycache__/model_cache')

# Initialize News API Client
newsapi = NewsApiClient(api_key='3b09f8a8c5934cc48b1b5c39b76cc630')

# Summarization pipeline (using a smaller model and local cache)
summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6',
                      cache_dir='./__pycache__/model_cache')

# Function to summarize the article


def summarize_article(article_text):
    summary = summarizer(article_text, max_length=100,
                         min_length=30, do_sample=False)
    return summary[0]['summary_text']


# Streamlit app interface
st.title('Latest News Summarizer')


def fetch_latest_news():
    top_headlines = newsapi.get_top_headlines(language='en', country='us')
    return top_headlines['articles']

# Display news and summaries


def display_news_and_summaries():
    st.subheader("Latest News")
    news_articles = fetch_latest_news()

    for article in news_articles:
        title = article['title']
        description = article['description']
        url = article['url']

        st.write(f"### {title}")
        st.write(description)
        st.write(f"[Read more]({url})")

        # Summarize the article content
        if description:
            summary = summarize_article(description)
            st.write(f"**Summary**: {summary}")


# Fetch and display news when button is clicked
if st.button('Fetch Latest News'):
    display_news_and_summaries()
