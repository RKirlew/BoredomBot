import tweepy
import requests
from random import randrange
randNum=randrange(40)

def main():
    response=requests.get("https://www.boredapi.com/api/activity")
    joke=requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    photoUrl=requests.get("https://api.unsplash.com/search/photos?page=1&query=relaxation&client_id=X0sVRMLjgtZbkyQ9Qn_wgnXgHzZrzI_clYHze0zD-kU")
    
    auth = tweepy.OAuthHandler('Aw172HN6wwRKVs13qK1om6D3B', 'sa8l0bMeq9Am48d5eE7IsY5a5rtqJWFOtMH71moVohcK9kLYHB')
    auth.set_access_token('1415553024450129921-JzrMp902nGyrjDfVIFDFAtnAHZAwOX', '5Kh8Xk3mZL2ma19Dh2p0WVGhi9XsTFBwW1fuj7l5KhTra')
   
    thePhotoformat="https://api.unsplash.com/search/photos?page={0}&query={1}&client_id=X0sVRMLjgtZbkyQ9Qn_wgnXgHzZrzI_clYHze0zD-kU".format(randNum,response.json()['type'])
    print(thePhotoformat)
    photoUrl=requests.get(thePhotoformat)
    tweet=" Bored? Here's What You Can Do Today:\n"+response.json()['activity']+" \nActivity Type: #"+response.json()['type'] +" #boredombotsuggestions #pythonprogramming #python #fun #quarantinecoding #bored "
    api = tweepy.API(auth)
    api.update_status(status = (tweet))
    for tweet in tweepy.Cursor(api.search, q='#python', rpp=5).items():
        
        try:
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            api.create_friendship(tweet.author.name)
        except:
                continue

    for tweet in tweepy.Cursor(api.search, q='#pythonprojects', rpp=3).items(10):
        try:
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
        except:
                continue
    for tweet in tweepy.Cursor(api.search, q='#programming', rpp=25).items(10):
        user = api.get_user(screen_name = tweet.user.screen_name)
        ID = user.id
        print(ID)
        test=joke.json()[0]['setup']+'\n'+joke.json()[0]['punchline']

        try:
            
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
            api.send_direct_message(ID, "Hi, BoredomBot has followed you because your post caused deiviations in the base temperature of my cold, digital, life unit, beep boop! "+test)

        except:
                continue
    for tweet in tweepy.Cursor(api.search, q='#coding', rpp=25).items():
        try:
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
            api.retweet(tweet.id)

        except:
                continue
    for tweet in tweepy.Cursor(api.search, q='#softwareengineering').items(50):
        try:
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
        except:
                continue


    for tweet in tweepy.Cursor(api.search, q='#100DaysOfCode', rpp=2).items():
        try:
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
        except:
                continue
    for tweet in tweepy.Cursor(api.search, q='#IoT', rpp=10).items():
         try:
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
         except:
                continue
    for tweet in tweepy.Cursor(api.search, q='#javascript').items(100):
        try:
            api.create_favorite(tweet.id)
            api.create_friendship(tweet.author.name)
        except:
                continue

def follow_followers(api):
    
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            greet="Hello @"+follower.name +"!! Thank you so much for following! I've gone ahead and followed you back <3"
            logger.info(f"Following {follower.name}")
            follower.follow()
            api.update_status(status = (greet))

if __name__=="__main__":
    auth = tweepy.OAuthHandler('Aw172HN6wwRKVs13qK1om6D3B', 'sa8l0bMeq9Am48d5eE7IsY5a5rtqJWFOtMH71moVohcK9kLYHB')
    auth.set_access_token('1415553024450129921-JzrMp902nGyrjDfVIFDFAtnAHZAwOX', '5Kh8Xk3mZL2ma19Dh2p0WVGhi9XsTFBwW1fuj7l5KhTra')
   
  
    api = tweepy.API(auth)
    main()
    follow_followers(api)
