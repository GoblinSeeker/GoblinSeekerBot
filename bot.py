import tweepy
import os
import feedparser
import random

# Load credentials from GitHub Secrets
client_id = os.environ['X_CLIENT_ID']
client_secret = os.environ['X_CLIENT_SECRET']
access_token = os.environ['X_ACCESS_TOKEN']
refresh_token = os.environ['X_REFRESH_TOKEN']

# Initialize Client
client = tweepy.Client(access_token=access_token)

def search_and_post():
    # We removed the "when:7d" constraint to find older entries as well
    # Added terms like "archive" and "history" for more variety
    queries = [
        "goblin sightings history",
        "documented angel encounters",
        "cryptid archives",
        "historical goblin reports",
        "mystical creature sightings"
    ]
    
    selected_query = random.choice(queries)
    rss_url = f"https://news.google.com/rss/search?q={selected_query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    if feed.entries:
        # Pick a random entry from the results to avoid posting the same thing every time
        entry = random.choice(feed.entries)
        
        # Clean up the description (remove HTML tags if present)
        description = entry.summary if 'summary' in entry else "A fascinating report from the archives."
        if len(description) > 150:
            description = description[:147] + "..."

        # Construct the tweet
        tweet_text = (
            f"🚨 GOBLIN SEEKER ARCHIVE 🚨\n\n"
            f"Topic: {entry.title}\n"
            f"Details: {description}\n\n"
            f"Source: {entry.link}\n\n"
            f"#GoblinSeeker $GOBLIN"
        )
        
        try:
            # Check length for X (280 chars)
            if len(tweet_text) > 280:
                tweet_text = f"🚨 GOBLIN SEEKER ARCHIVE 🚨\n\n{entry.title}\n\n{entry.link}\n\n$GOBLIN"

            client.create_tweet(text=tweet_text)
            print("Post successful!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    search_and_post()
    
