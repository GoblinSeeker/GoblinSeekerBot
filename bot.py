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

def interact_with_users():
    try:
        # Searching specifically for Goblin related tweets
        search_query = "goblin folklore OR goblin sightings -is:retweet"
        tweets = client.search_recent_tweets(query=search_query, max_results=10)
        
        if tweets.data:
            target_tweet = random.choice(tweets.data)
            client.like(target_tweet.id)
            client.follow_user(target_tweet.author_id)
            print(f"Interacted with Goblin tweet ID: {target_tweet.id}")

        my_user = client.get_me()
        mentions = client.get_users_mentions(id=my_user.data.id)
        
        if mentions.data:
            for mention in mentions.data:
                reply_text = "The Goblin Archive acknowledges your presence. The truth is hidden in the shadows. #GoblinSeeker"
                client.create_tweet(text=reply_text, in_reply_to_tweet_id=mention.id)
                print(f"Replied to goblin mention: {mention.id}")

    except Exception as e:
        print(f"Interaction Error: {e}")

def search_and_post():
    # Strictly Goblin-focused queries
    queries = [
        "goblin sightings history",
        "historical goblin reports",
        "goblin folklore archives",
        "ancient goblin legends",
        "documented goblin encounters"
    ]
    
    selected_query = random.choice(queries)
    formatted_query = selected_query.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={formatted_query}&hl=en-US&gl=US&ceid=US:en"
    
    feed = feedparser.parse(rss_url)
    
    if feed.entries:
        entry = random.choice(feed.entries)
        description = entry.summary if 'summary' in entry else "A fascinating report from the goblin archives."
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
            print(f"Post successful: {selected_query}")
        except Exception as e:
            print(f"Posting Error: {e}")
    else:
        print(f"No goblin results found for: {selected_query}")

if __name__ == "__main__":
    search_and_post()
    interact_with_users()
