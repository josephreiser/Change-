# UNFINISHED PROJECT - TWEET GAME
# Author: Joe Reiser | 09/25/20
import json
import requests
import sys
import random
from datetime import datetime

random.seed(datetime.now())
resMusk = requests.GET('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=3200')
muskTweets = json.loads(resMusk.text)
muskData = json.dumps(muskTweets)
resKanye = requests.GET('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=kanyewest&count=3200')
kanyeTweets = json.loads(resKanye.text)
kanyeData = json.dumps(kanyeTweets)


for tweet in kanyeData:
    if "@" in tweet:
        kanyeData.pop(tweet)
    if "https" in tweet:
        kanyeData.pop(tweet)


for tweet in muskData:
    if "@" in tweet:
        muskData.pop(tweet)
    if "https" in tweet:
        muskData.pop(tweet)

games = 0
wins = 0

ongoing = True

while (ongoing):
    games += 1
    if (games == 0):
        print("Welcome to Tweet Guesser. Guess who tweeted the following tweet: \n")
    else:
        print("Here is your next tweet: \n")

    random.seed(datetime.now())
    if (random.randint(0,1)):
        print(random.choice(list(muskData)))
        tweeter = "MUSK"
        notTweeter = "KANYE"
    else:
        print(random.choice(list(kanyeData)))
        tweeter = "KANYE"
        notTweeter = "MUSK"

    answer = input("What do you think?\n")
    if (tweeter == answer.upper()):
        wins += 1
        print("Congratulations! You are correct, the tweet came from " + tweeter + ".\n")
    else:
        print("Wrong! The tweet came from " + notTweeter + ", not " + tweeter + ".\n")

    print("Current Statistics:\n")
    print("Games played: " + str(games) + "\n")
    print("Games won: " + str(wins) + "\n")
    
    invalid = True
    while (invalid):
        again = input('Would you like to play again? Type YES or NO\n')
        if (again.upper() == "YES"):
            invalid = False
        elif (again.upper() == "NO"):
            invalid = False
            ongoing = False
            print("Thanks for playing!\n")
        else:
            print("Answer not understood. You must type YES or NO\n")
        


    
