#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:47:02 2020

@author: Bruno
"""

# Modules 
import pandas 
import tweepy


# Authentication with your credentials:

auth = tweepy.OAuthHandler("dUccFFYUBCdImYFvQeLVNV3ij", 
                           "RPLTQRvGix0sK6QKkNS0ZJq6y1lsc5nR5OGDahV77mydUYTplq")
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


# Getting tweets from our three sources and saving them in a df (Adelaida)

factcheckers = ["factcheckdotorg", "Politifact", "snopes"]

tweets = [] 

for i in factcheckers:
   

    tweets += tweepy.Cursor(api.user_timeline,id= i).items(200)
    
    tweets_list = [[tweet.user.screen_name, tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
    
    tweets_df = pandas.DataFrame(tweets_list,columns=['User', 'Datetime', 'Tweet Id', 'Text'])
    
    

# Visualizing example (See plots pane)

from plotnine import * # for visualization 
from mizani.breaks import date_breaks
from mizani.formatters import date_format

theme_set(theme_minimal()) # default theme


plot1 = (ggplot(tweets_df, aes(x = 'Datetime', fill = 'User')) +
       geom_histogram() +
       scale_x_datetime(breaks=date_breaks('1 week')) +
       labs(x = "Time in weeks", y = "Number of tweets by source")
       )
       
print(plot1)





    