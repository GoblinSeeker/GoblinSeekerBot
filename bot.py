import tweepy
import os
import feedparser
import random

client_id = os.environ['X_CLIENT_ID']
client_secret = os.environ['X_CLIENT_SECRET']
access_token = os.environ['X_ACCESS_TOKEN']
refresh_token = os.environ['X_REFRESH_TOKEN']

client = tweepy.Client(
    consumer_key=client_id,
    consumer_secret=client_secret,
    access_token=access_token,
    access_token_secret=refresh_token
)

def search_and_post():
    query = "goblin sightings"
    rss_url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    if feed.entries:
        entry = random.choice(feed.entries)
        tweet_text = f"🚨 GOBLIN NEWS 🚨\n\n{entry.title}\n\n{entry.link}\n\n#GoblinSeeker"
        
        try:
            client.create_tweet(text=tweet_text)
            print("Success")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    search_and_post()
