import tweepy
import time
import datetime
import config

#Initialize the client
client= tweepy.Client(bearer_token=config.Bearer_Token,
consumer_key=config.API_Key, 
consumer_secret=config.API_Secret,
access_token=config.Access_Token,
access_token_secret=config.Access_Secret)

query= 'Great Molasses Flood'#'from:briancox03 (@Stupid_TweetBot OR -is:reply) -is:retweet' 

#Get Last Tweet
lastTweet=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")#datetime.datetime.utcnow().replace(microsecond=1).isoformat()
print(lastTweet)

#Start Loop
while True:
    print("Waiting 15 minutes")
    time.sleep(900)
    #Get every tweet since last tweet
    response=client.search_recent_tweets(query=query,max_results=100, start_time=lastTweet)
    if response.data:
        for resp in response.data:
            print("tweeted")
            client.retweet(resp.id)
            time.sleep(60)
    lastTweet=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")#datetime.datetime.utcnow().replace(microsecond=1).isoformat()
