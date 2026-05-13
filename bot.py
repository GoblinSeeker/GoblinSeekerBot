import tweepy
import os
import feedparser
import random

# Wir laden die 1.0a Keys aus deinen Secrets
api_key = os.environ['X_CLIENT_ID']
api_secret = os.environ['X_CLIENT_SECRET']
access_token = os.environ['X_ACCESS_TOKEN']
access_secret = os.environ['X_REFRESH_TOKEN']

# Authentifizierung strikt nach OAuth 1.0a
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Client für v2 Befehle (wie create_tweet) mit 1.0a Daten füttern
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

def search_and_post():
    query = "goblin sightings"
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    if feed.entries:
        entry = random.choice(feed.entries)
        tweet_text = f"🚨 GOBLIN NEWS 🚨\n\n{entry.title}\n\n{entry.link}\n\n#GoblinSeeker"
        
        try:
            client.create_tweet(text=tweet_text)
            print("Erfolg! Der Post ist raus.")
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    search_and_post()
