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

def interact_with_users():
    try:
        search_query = "goblin folklore OR goblin sightings -is:retweet"
        tweets = client.search_recent_tweets(query=search_query, max_results=5)
        if tweets.data:
            target_tweet = random.choice(tweets.data)
            client.like(target_tweet.id)
            client.follow_user(target_tweet.author_id)
            print(f"Interacted with ID: {target_tweet.id}")
    except Exception as e:
        print(f"Interaction Error: {e}")

def search_and_post():
    queries = [
        "goblin sightings history",
        "historical goblin reports",
        "goblin folklore archives",
        "ancient goblin legends",
        "documented goblin encounters"
    ]
    selected_query = random.choice(queries)
    rss_url = f"https://news.google.com/rss/search?q={selected_query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    if feed.entries:
        entry = random.choice(feed.entries)
        tweet_text = f"🚨 GOBLIN SEEKER ARCHIVE 🚨\n\nTopic: {entry.title}\n\nSource: {entry.link}\n\n#GoblinSeeker $GOBLIN"
        try:
            client.create_tweet(text=tweet_text)
            print(f"Post successful: {selected_query}")
        except Exception as e:
            print(f"Posting Error: {e}")
    else:
        print(f"No results for: {selected_query}")

if __name__ == "__main__":
    search_and_post()
    interact_with_users()
