#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:19:30 2020

@author: Bruno
"""

# The function gather_twits(n=10) collects the last 10 twits from the following users:
# "factcheckdotorg", "Politifact", "snopes"
# By default, 10 twits will be gathered, but n can be changed between 1 and 200.

def gather_twits(n=10):
    import tweepy
    import pandas
    import datetime




    # Authentication with your credentials:

    auth = tweepy.OAuthHandler("SNXprfNdEjmTiQG4MjMI8ANoQ", "oFpNh8EuhGt1m06SJwLxl7tp3uumGAEt5SK7m5AW3IUxCls2MC")
    api = tweepy.API(auth)

    # Getting the last 10 twits for the three accounts

    # The name of the accounts we are interested:   
    accounts =["factcheckdotorg", "Politifact", "snopes"]

    zipped_list = []
    date = []
    content = []
    author = []

    for element in accounts:
        twits = api.user_timeline(screen_name = str(element),
                                  count= n,
                                  include_rts = False,
                                  tweet_mode = 'extended')
        for info in twits:
            "ID: {}".format(info.id)
            date.append(str(info.created_at))
            content.append(str(info.full_text))
            author.append(str(element))
  
    # separates date and time:
        split_date = []
        x = []
        for element in date:
            x = element.split(" ")
            x = x[0]
            split_date.append(x)

    # creates a data frame:   
        zipped_list = list(zip(split_date, author, content))
        final = pandas.DataFrame(zipped_list, 
                                 columns=("Date", "Author", "Content"))

    # transforms date from string to date type:
        final["Date"]  = pandas.to_datetime(final["Date"])
    return final


    
    