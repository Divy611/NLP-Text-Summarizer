import nltk
import streamlit as st
from newsapi import NewsApiClient
from transformers import pipeline

nltk.download('punkt', download_dir='./__pycache__/model_cache')

newsapi = NewsApiClient(api_key='3b09f8a8c5934cc48b1b5c39b76cc630')
summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')


def summarize_article(article_text):
    try:
        summary = summarizer(article_text, max_length=75,
                             min_length=35, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return "Error summarizing article: " + str(e)


def fetch_latest_news():
    top_headlines = newsapi.get_top_headlines(
        language='en', country='us', page_size=10)  # Fetch up to 10 articles
    return top_headlines['articles']

# Display news and summaries


def display_news_and_summaries():
    st.subheader("Latest News Summarized")

    # Fetch news articles
    news_articles = fetch_latest_news()

    # Summarize and display each article
    for idx, article in enumerate(news_articles):
        title = article['title']
        description = article['description']
        url = article['url']

        st.write(f"### {idx+1}. {title}")
        # st.write(
        #    f"**Original Description**: {description if description else 'No description available'}")
        if description:
            summary = summarize_article(description)
            st.write(f"**Summary**: {summary}")
        else:
            st.write("**Summary**: No description available to summarize.")

        st.write(f"[Read more]({url})")
        st.write("---")


display_news_and_summaries()
