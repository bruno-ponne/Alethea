#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:47:02 2020

@author: Bruno
"""

# To install tweepy: type "pip install tweepy"
# in the command line
import tweepy


# Authentication with your credentials:

auth = tweepy.OAuthHandler("your key", "your secret key")
api = tweepy.API(auth)

# Getting some tweets:
    
tweets = api.user_timeline(screen_name="factcheckdotorg",
                           count=200,
                           include_rts = False,
                           tweet_mode = 'extended'
                           )

for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")

