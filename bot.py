import tweepy
import feedparser
import os
import random
import time

# Authentifizierung
client = tweepy.Client(
    consumer_key=os.environ['X_CLIENT_ID'], 
    consumer_secret=os.environ['X_CLIENT_SECRET'],
    access_token=os.environ['X_ACCESS_TOKEN'],
    access_token_secret=os.environ['X_REFRESH_TOKEN']
)

def post_news():
    sources = [
        "https://www.unexplained-mysteries.com/headlines.xml",
        "https://www.phantomsandmonsters.com/feeds/posts/default?alt=rss"
    ]
    feed = feedparser.parse(random.choice(sources))

    if feed.entries:
        entry = random.choice(feed.entries[:20])
        tweet_text = f"🚨 ANOMALY REPORT: {entry.title}\n\n#GoblinSeeker #Paranormal #Cryptid\n{entry.link}"
        
        try:
            client.create_tweet(text=tweet_text)
            print(f"✅ Success: News post published!")
        except Exception as e:
            print(f"❌ Post Error: {e}")

if __name__ == "__main__":
    print("--- [GOBLIN SEEKER PROTOCOL STARTING] ---")
    
    # Kürzere Verzögerung für diesen Test (2-5 Minuten)
    wait_time = random.randint(120, 300)
    print(f"🕵️ Stealth mode: Waiting {wait_time} seconds...")
    time.sleep(wait_time)

    # NUR POSTEN - Das ist im Free Tier erlaubt
    post_news()
    
    print("--- [CYCLE COMPLETED] ---")
