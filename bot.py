import tweepy
import feedparser
import os
import random
import time

# Authentifizierung
try:
    client = tweepy.Client(
        consumer_key=os.environ['X_CLIENT_ID'], 
        consumer_secret=os.environ['X_CLIENT_SECRET'],
        access_token=os.environ['X_ACCESS_TOKEN'],
        access_token_secret=os.environ['X_REFRESH_TOKEN']
    )
    print("✅ Auth-Client initialized.")
except Exception as e:
    print(f"❌ Auth-Client Setup Error: {e}")

def post_news():
    print("📡 Fetching news from RSS feeds...")
    sources = [
        "https://www.unexplained-mysteries.com/headlines.xml",
        "https://www.phantoms-and-monsters.com/feeds/posts/default?alt=rss"
    ]
    
    url = random.choice(sources)
    feed = feedparser.parse(url)

    if not feed.entries:
        print(f"⚠️ No entries found in feed: {url}")
        # Falls der erste Feed leer war, probieren wir den anderen
        url = sources[0] if url != sources[0] else sources[1]
        feed = feedparser.parse(url)

    if feed.entries:
        entry = random.choice(feed.entries[:20])
        # Wir kürzen den Titel, falls er zu lang ist
        title = (entry.title[:200] + '...') if len(entry.title) > 200 else entry.title
        tweet_text = f"🚨 ANOMALY REPORT: {title}\n\n#GoblinSeeker #Paranormal\n{entry.link}"
        
        print(f"✍️ Attempting to post: {title[:50]}...")
        try:
            client.create_tweet(text=tweet_text)
            print(f"✅ Success: News post published!")
        except Exception as e:
            print(f"❌ Post Error: {e}")
    else:
        print("❌ Failed to retrieve any news from all sources.")

if __name__ == "__main__":
    print("--- [GOBLIN SEEKER PROTOCOL STARTING] ---")
    
    # Kürzeste Verzögerung für diesen finalen Test (30-60 Sekunden)
    # Wir wollen ja nicht ewig warten, um zu sehen ob es geht
    wait_time = random.randint(30, 60)
    print(f"🕵️ Stealth mode: Waiting {wait_time} seconds...")
    time.sleep(wait_time)

    post_news()
    
    print("--- [CYCLE COMPLETED] ---")
