import tweepy
import feedparser
import os
import random
import time

# Authentication via GitHub Secrets
client = tweepy.Client(
    consumer_key=os.environ['X_CLIENT_ID'], 
    consumer_secret=os.environ['X_CLIENT_SECRET'],
    access_token=os.environ['X_ACCESS_TOKEN'],
    access_token_secret=os.environ['X_REFRESH_TOKEN']
)

def post_news():
    # Primary sources for high-quality paranormal content
    sources = [
        "https://www.unexplained-mysteries.com/headlines.xml",
        "https://www.phantomsandmonsters.com/feeds/posts/default?alt=rss"
    ]
    
    feed = feedparser.parse(random.choice(sources))

    if feed.entries:
        # Select from the most recent articles
        entry = random.choice(feed.entries[:20])
        title = entry.title
        link = entry.link

        intros = [
            "🚨 ALERT:", "👺 GOBLIN LOG:", "🔍 INVESTIGATION:", "⚠️ UNKNOWN:", 
            "👣 TRACKS DETECTED:", "🌑 MIDNIGHT REPORT:", "👁️ WITNESS:", 
            "🎥 ANALYZING FOOTAGE:", "🏚️ ANOMALY DETECTED:", "📡 FREQUENCY SHIFT:",
            "📜 OLD RECORDS:", "🌑 SHADOW WORK:", "🔋 ENERGY SPIKE:", "🔦 WOODS SCAN:"
        ]
        
        connectors = [
            "You need to see this.", "Something is happening.", "The signs are clear.",
            "Analyzing the data now.", "The Seeker network is buzzing.", 
            "Captured near the tree line.", "Verified report coming in.",
            "Can anyone explain this?", "The evidence is mounting."
        ]
        
        # Dynamic Hashtag Generator
        tags_pool = ["#GoblinSeeker", "#Paranormal", "#Cryptid", "#UFO", "#Anomaly", "#Supernatural", "#Seeker", "#GhostHunter"]
        selected_tags = " ".join(random.sample(tags_pool, random.randint(2, 4)))

        tweet_text = f"{random.choice(intros)} {title}\n\n{random.choice(connectors)}\n{link}\n\n{selected_tags}"
        
        try:
            client.create_tweet(text=tweet_text)
            print(f"Guaranteed news post published: {title[:30]}...")
        except Exception as e:
            print(f"News Error: {e}")

def interact_with_world():
    search_queries = [
        "goblin sighting", "paranormal investigation", "cryptid encounter", 
        "creature in the woods", "strange lights sky", "supernatural event"
    ]
    
    query = f"{random.choice(search_queries)} -is:retweet"
    
    try:
        search_results = client.search_recent_tweets(query=query, max_results=10)
        
        if search_results.data:
            interaction_batch = random.sample(search_results.data, min(len(search_results.data), 2))
            
            for target_tweet in interaction_batch:
                # Small delay between interactions
                time.sleep(random.randint(10, 30))
                
                # Like is 100% if interaction triggers
                try:
                    client.like(target_tweet.id)
                    print(f"Engagement: Liked {target_tweet.id}")
                except:
                    pass

                # Reply is 50/50
                if random.random() > 0.5:
                    replies = [
                        "This fits the #GoblinSeeker pattern perfectly. 👺",
                        "The energy here is extremely high. Stay safe. 🚨",
                        "We've seen similar reports in the Seeker network. 🔍",
                        "Classic anomaly behavior. Thanks for documenting! 👣",
                        "Interesting. The veil seems thin in that area. 🌑",
                        "Don't ignore the signs. They are definitely active. 👁️"
                    ]
                    
                    try:
                        client.create_tweet(
                            text=random.choice(replies),
                            in_reply_to_tweet_id=target_tweet.id
                        )
                        print(f"Engagement: Replied to {target_tweet.id}")
                    except:
                        pass
                
    except Exception as e:
        print(f"Interaction Cycle Error: {e}")

if __name__ == "__main__":
    print("--- [GOBLIN SEEKER PROTOCOL STARTING] ---")
    
    # 1. RANDOM DELAY AT THE START (Avoids posting exactly at :00)
    # Delays the execution by 2 to 12 minutes
    start_delay = random.randint(120, 720)
    print(f"Waiting {start_delay} seconds to look organic...")
    time.sleep(start_delay)

    # 2. GUARANTEED POST
    post_news()
    
    # 3. RANDOM INTERACTION (75% chance)
    if random.random() < 0.75:
        time.sleep(random.randint(30, 90))
        interact_with_world()
    
    print("--- [CYCLE COMPLETED] ---")
