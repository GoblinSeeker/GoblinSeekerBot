import tweepy
import os
import feedparser
import random

client_id = os.environ['X_CLIENT_ID']
client_secret = os.environ['X_CLIENT_SECRET']
access_token = os.environ['X_ACCESS_TOKEN']
refresh_token = os.environ['X_REFRESH_TOKEN']

client = tweepy.Client(
    bearer_token=None,
    consumer_key=client_id,
    consumer_secret=client_secret,
    access_token=access_token,
    access_token_secret=refresh_token
)

def search_and_post():
    queries = [
        "goblin sightings history",
        "documented angel encounters",
        "cryptid archives",
        "historical goblin reports",
        "mystical creature sightings"
    ]
    
    selected_query = random.choice(queries)
    formatted_query = selected_query.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={formatted_query}&hl=en-US&gl=US&ceid=US:en"
    
    feed = feedparser.parse(rss_url)
    
    if feed.entries:
        entry = random.choice(feed.entries)
        
        description = entry.summary if 'summary' in entry else "A fascinating report from the archives."
        if len(description) > 130:
            description = description[:127] + "..."

        tweet_text = (
            f"🚨 GOBLIN SEEKER ARCHIVE 🚨\n\n"
            f"Topic: {entry.title}\n"
            f"Details: {description}\n\n"
            f"Source: {entry.link}\n\n"
            f"#GoblinSeeker $GOBLIN"
        )
        
        try:
            if len(tweet_text) > 280:
                tweet_text = f"🚨 GOBLIN SEEKER ARCHIVE 🚨\n\n{entry.title}\n\n{entry.link}\n\n$GOBLIN"

            client.create_tweet(text=tweet_text)
            print(f"Post successful for: {selected_query}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"No results found for: {selected_query}")

if __name__ == "__main__":
    search_and_post()
    
