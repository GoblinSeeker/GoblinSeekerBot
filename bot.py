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
    # Primary source for high-quality paranormal content
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

        # Massive phrase pool for organic variety
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
            # Simulate "thinking/typing" time
            time.sleep(random.randint(5, 15))
            client.create_tweet(text=tweet_text)
            print(f"News cycle completed: {title[:30]}...")
        except Exception as e:
            print(f"News Error: {e}")

def interact_with_world():
    # Diverse search queries to reach different sub-communities
    search_queries = [
        "goblin sighting", "paranormal investigation", "cryptid encounter", 
        "creature in the woods", "strange lights sky", "supernatural event",
        "skinwalker", "mothman", "forest anomaly"
    ]
    
    query = f"{random.choice(search_queries)} -is:retweet"
    
    try:
        search_results = client.search_recent_tweets(query=query, max_results=15)
        
        if search_results.data:
            # Pick a subset of tweets to interact with (max 3)
            interaction_batch = random.sample(search_results.data, min(len(search_results.data), 3))
            
            for target_tweet in interaction_batch:
                # Random delay between interactions to look human
                time.sleep(random.randint(20, 45))
                
                # Probability: Always like, but only reply 50% of the time
                try:
                    client.like(target_tweet.id)
                    print(f"Engagement: Liked {target_tweet.id}")
                except:
                    pass

                if random.random() > 0.5:
                    replies = [
                        "This fits the #GoblinSeeker pattern perfectly. 👺",
                        "The energy here is extremely high. Stay safe. 🚨",
                        "We've seen similar reports in the Seeker network. 🔍",
                        "Classic anomaly behavior. Thanks for documenting! 👣",
                        "Interesting. The veil seems thin in that area. 🌑",
                        "Don't ignore the signs. They are definitely active. 👁️",
                        "Exactly what we've been warning about! #Paranormal",
                        "Fascinating report. Adding this to the database. 📂"
                    ]
                    
                    try:
                        client.create_tweet(
                            text=random.choice(replies),
                            in_reply_to_tweet_id=target_tweet.id
                        )
                        print(f"Engagement: Replied to {target_tweet.id}")
                    except Exception as r_e:
                        print(f"Reply Error: {r_e}")
                
    except Exception as e:
        print(f"Interaction Cycle Error: {e}")

if __name__ == "__main__":
    print("--- [GOBLIN SEEKER PROTOCOL INITIALIZED] ---")
    
    # 80% chance to post news (makes it less predictable)
    if random.random() < 0.8:
        post_news()
    
    # 70% chance to interact with others
    if random.random() < 0.7:
        # Pause between posting and interacting
        time.sleep(random.randint(30, 60))
        interact_with_world()
    
    print("--- [CYCLE COMPLETED] ---")
