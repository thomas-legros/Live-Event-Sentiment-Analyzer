import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import time
from collections import Counter

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Event-specific search query (e.g., "Super Bowl", "ConcertXYZ")
search_query = 'Super Bowl'

# Function to analyze sentiment of each tweet
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Main function to collect tweets and perform sentiment analysis
def collect_and_analyze():
    positive = 0
    negative = 0
    neutral = 0
    tweet_count = 0
    sentiments = []

    print("Starting real-time sentiment analysis for:", search_query)
    
    # Stream tweets
    for tweet in tweepy.Cursor(api.search_tweets, q=search_query, lang="en").items(100):
        sentiment = analyze_sentiment(tweet)
        sentiments.append(sentiment)
        tweet_count += 1
        if sentiment == 'positive':
            positive += 1
        elif sentiment == 'negative':
            negative += 1
        else:
            neutral += 1

        # Update stats every 10 tweets
        if tweet_count % 10 == 0:
            print(f"Processed {tweet_count} tweets...")
            plot_sentiment_analysis(positive, negative, neutral)

        time.sleep(2)

# Plot sentiment analysis results
def plot_sentiment_analysis(positive, negative, neutral):
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive, negative, neutral]
    colors = ['#66b3ff', '#ff6666', '#ffcc99']

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Live Event Sentiment Analysis')
    plt.show()

# Run the sentiment analysis
collect_and_analyze()
