import tweepy
import os
import feedparser

# Load credentials from GitHub Secrets
client_id = os.environ['X_CLIENT_ID']
client_secret = os.environ['X_CLIENT_SECRET']
access_token = os.environ['X_ACCESS_TOKEN']
refresh_token = os.environ['X_REFRESH_TOKEN']

# Prepare OAuth 2.0 Authentication
oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=client_id,
    redirect_uri="https://google.com",
    scope=["tweet.read", "tweet.write", "users.read", "offline.access"],
    client_secret=client_secret
)

# Initialize Client with Access Token
client = tweepy.Client(access_token=access_token)

def search_and_post():
    # Search for goblin and theological entities
    query = "goblin sighting OR cryptid OR angel encounter"
    rss_url = f"https://news.google.com/rss/search?q={query}+when:7d&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    if feed.entries:
        entry = feed.entries[0]
        # Optimized text for Goblin Seeker update
        tweet_text = f"🚨 GOBLIN SEEKER UPDATE 🚨\n\n{entry.title}\n\nAnalyzing mystical significance... 🔍\n{entry.link}\n\n#GoblinSeeker $GOBLIN"
        
        try:
            client.create_tweet(text=tweet_text)
            print("Post successful!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    search_and_post()
  
