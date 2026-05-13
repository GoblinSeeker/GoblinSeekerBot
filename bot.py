import tweepy
import feedparser
import os
import random
import time

# Authenticate to X API
try:
    client = tweepy.Client(
        consumer_key=os.environ.get('X_CLIENT_ID'), 
        consumer_secret=os.environ.get('X_CLIENT_SECRET'),
        access_token=os.environ.get('X_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('X_REFRESH_TOKEN')
    )
    print("✅ Auth-Client initialized.")
except Exception as e:
    print(f"❌ Auth-Client Setup Error: {e}")

def post_news():
    print("📡 Fetching news from RSS feeds...")
    
    sources = [
        "https://www.unexplained-mysteries.com/headlines.xml",
        "https://www.phantomsandmonsters.com/feeds/posts/default",
        "https://www.cryptozoologynews.com/feed/",
        "https://www.singularfortean.com/news?format=rss"
    ]
    
    selected_entry = None
    random.shuffle(sources)

    for url in sources:
        try:
            feed = feedparser.parse(url)
            if feed.entries:
                selected_entry = random.choice(feed.entries[:10])
                print(f"✅ Found news in: {url}")
                break
            else:
                print(f"⚠️ Feed empty: {url}")
        except Exception as e:
            print(f"⚠️ Error reading {url}: {e}")

    if selected_entry:
        title = selected_entry.title
        link = selected_entry.link
        tweet_text = f"🚨 ANOMALY REPORT: {title}\n\n#GoblinSeeker #Paranormal #Mystery\n{link}"
    else:
        print("⚠️ No news found. Switching to manual report mode...")
        backup_reports = [
            "Increased electromagnetic activity detected in the woods tonight. Stay vigilant. #GoblinSeeker #Paranormal",
            "Analyzing old eyewitness accounts of forest anomalies. The patterns are shifting. #Cryptid #Seeker",
            "The veil is thin tonight. No new sightings reported yet, but the energy is high. #Paranormal #Goblins"
        ]
        tweet_text = random.choice(backup_reports)

    print(f"✍️ Attempting to post...")
    try:
        client.create_tweet(text=tweet_text)
        print(f"✅ Success: Post published!")
    except Exception as e:
        print(f"❌ Post Error: {e}")

if __name__ == "__main__":
    print("--- [GOBLIN SEEKER PROTOCOL STARTING] ---")
    
    wait_time = random.randint(120, 720)
    print(f"🕵️ Stealth mode: Waiting {wait_time} seconds...")
    time.sleep(wait_time)

    post_news()
    
    print("--- [CYCLE COMPLETED] ---")
