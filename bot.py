import tweepy
import feedparser
import os
import random
import time

# --- AUTHENTIFIZIERUNG ---
# Wir nutzen exakt deine GitHub-Secret-Namen. 
# Hinweis: X_REFRESH_TOKEN enthält technisch gesehen dein Access Token Secret.
client = tweepy.Client(
    consumer_key=os.environ['X_CLIENT_ID'], 
    consumer_secret=os.environ['X_CLIENT_SECRET'],
    access_token=os.environ['X_ACCESS_TOKEN'],
    access_token_secret=os.environ['X_REFRESH_TOKEN']
)

def post_news():
    """Zieht einen Artikel aus den Feeds und postet ihn garantiert."""
    sources = [
        "https://www.unexplained-mysteries.com/headlines.xml",
        "https://www.phantomsandmonsters.com/feeds/posts/default?alt=rss"
    ]
    
    feed = feedparser.parse(random.choice(sources))

    if feed.entries:
        entry = random.choice(feed.entries[:15]) # Nimmt einen der 15 neuesten Artikel
        title = entry.title
        link = entry.link

        intros = [
            "🚨 ALERT:", "👺 GOBLIN LOG:", "🔍 INVESTIGATION:", "⚠️ UNKNOWN:", 
            "👣 TRACKS DETECTED:", "🌑 MIDNIGHT REPORT:", "👁️ WITNESS:", 
            "🎥 ANALYZING FOOTAGE:", "🏚️ ANOMALY DETECTED:", "📡 FREQUENCY SHIFT:"
        ]
        
        connectors = [
            "You need to see this.", "Something is happening.", "The signs are clear.",
            "Analyzing the data now.", "The Seeker network is buzzing.", 
            "Captured near the tree line.", "Can anyone explain this?"
        ]
        
        tags_pool = ["#GoblinSeeker", "#Paranormal", "#Cryptid", "#UFO", "#Anomaly", "#Supernatural"]
        selected_tags = " ".join(random.sample(tags_pool, random.randint(2, 4)))

        tweet_text = f"{random.choice(intros)} {title}\n\n{random.choice(connectors)}\n{link}\n\n{selected_tags}"
        
        try:
            client.create_tweet(text=tweet_text)
            print(f"✅ Guaranteed news post published: {title[:40]}...")
        except Exception as e:
            print(f"❌ News Post Error: {e}")

def interact_with_world():
    """Sucht nach passenden Tweets und interagiert zufällig (Likes/Replies)."""
    search_queries = [
        "goblin sighting", "paranormal investigation", "cryptid encounter", 
        "creature in the woods", "strange lights sky"
    ]
    
    query = f"{random.choice(search_queries)} -is:retweet"
    
    try:
        search_results = client.search_recent_tweets(query=query, max_results=10)
        
        if search_results.data:
            # Schnappt sich max. 2 Tweets, um nicht spammig zu wirken
            interaction_batch = random.sample(search_results.data, min(len(search_results.data), 2))
            
            for target_tweet in interaction_batch:
                # Organische Pause vor der Interaktion (20 bis 45 Sekunden)
                delay = random.randint(20, 45)
                print(f"⏳ Reading tweet... waiting {delay}s before reacting.")
                time.sleep(delay)
                
                # 1. Like (wird immer ausgeführt, wenn dieser Block läuft)
                try:
                    client.like(target_tweet.id)
                    print(f"❤️ Liked tweet {target_tweet.id}")
                except Exception as e:
                    print(f"⚠️ Like Error: {e}")

                # 2. Reply (50% Chance, um nicht unter jeden Tweet zu schreiben)
                if random.random() > 0.5:
                    # Kurze zusätzliche Pause vor dem Tippen
                    time.sleep(random.randint(10, 25))
                    replies = [
                        "This fits the #GoblinSeeker pattern perfectly. 👺",
                        "The energy here is extremely high. Stay safe. 🚨",
                        "We've seen similar reports in the Seeker network. 🔍",
                        "Classic anomaly behavior. Thanks for documenting! 👣",
                        "Interesting. The veil seems thin in that area. 🌑"
                    ]
                    
                    try:
                        client.create_tweet(
                            text=random.choice(replies),
                            in_reply_to_tweet_id=target_tweet.id
                        )
                        print(f"💬 Replied to tweet {target_tweet.id}")
                    except Exception as e:
                        print(f"⚠️ Reply Error: {e}")
                
    except Exception as e:
        print(f"❌ Interaction Cycle Error: {e}")

if __name__ == "__main__":
    print("--- [GOBLIN SEEKER PROTOCOL STARTING] ---")
    
    # 1. TARNUNGS-PHASE (Human Delay)
    # Wartet zufällig zwischen 2 und 12 Minuten. 
    # Wenn GitHub um 20:00 Uhr triggert, startet die Aktion z.B. erst um 20:07 Uhr.
    start_delay = random.randint(120, 720)
    print(f"🕵️ Organic stealth mode active. Waiting {start_delay} seconds...")
    time.sleep(start_delay)

    # 2. GARANTIERTER POST
    post_news()
    
    # 3. ZUFÄLLIGE INTERAKTION (75% Chance)
    # Der Bot interagiert nicht jede Stunde, sondern lässt auch mal Pausen.
    if random.random() < 0.75:
        # Pause zwischen dem eigenen Post und der Suche nach anderen
        time.sleep(random.randint(40, 90))
        print("🔍 Searching for anomalies to interact with...")
        interact_with_world()
    else:
        print("💤 Skipping interactions this cycle to stay under the radar.")
    
    print("--- [CYCLE COMPLETED] ---")
