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

def generate_dynamic_report():
    # Der Text-Baukasten für unendliche Variationen
    intros = [
        "Anomaly detected:", 
        "Sensors picking up unusual readings:", 
        "New field report:", 
        "Monitoring local frequencies:", 
        "Just intercepted a strange broadcast:"
    ]
    phenomena = [
        "unidentified humanoid figures", 
        "strange luminescent orbs", 
        "erratic electromagnetic shifts", 
        "unexplained acoustic anomalies", 
        "sudden temperature drops"
    ]
    locations = [
        "near the old logging road", 
        "deep in the dense forest", 
        "along the river banks", 
        "at the edge of the abandoned sector", 
        "in the remote northern ridge"
    ]
    actions = [
        "Investigating further.", 
        "Data logged for analysis.", 
        "Proceeding with caution.", 
        "Equipment is malfunctioning.", 
        "Staying hidden to observe."
    ]
    tags = [
        "#GoblinSeeker #Paranormal", 
        "#Cryptid #Mystery", 
        "#Anomaly #Seeker", 
        "#Unexplained #Files"
    ]

    # Baut den Satz aus den zufälligen Bausteinen zusammen
    tweet = f"{random.choice(intros)} {random.choice(phenomena)} {random.choice(locations)}. {random.choice(actions)}\n\n{random.choice(tags)}"
    return tweet

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
        print("⚠️ No news found. Generating dynamic report...")
        # Hier rufen wir jetzt den neuen Baukasten auf
        tweet_text = generate_dynamic_report()

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
