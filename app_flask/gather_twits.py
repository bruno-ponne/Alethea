#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:19:30 2020

@author: Bruno
"""

# The function gather_twits() collects the last n twits from the specified accounts
# n: an integer ranging from 1 to 200.
# accounts: a list with the name of the accounts
# df: True - a data frame is returned; False - a list of dictionaries is returned
def gather_twits(n, accounts = ["factcheckdotorg", "Politifact", "snopes"], df = True):
    import tweepy
    import pandas
    from datetime import datetime

    # Authentication:

    auth = tweepy.OAuthHandler("SNXprfNdEjmTiQG4MjMI8ANoQ", "oFpNh8EuhGt1m06SJwLxl7tp3uumGAEt5SK7m5AW3IUxCls2MC")
    api = tweepy.API(auth)

    #Variables needed:
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
  

    # creates a data frame:   
    zipped_list = list(zip(date, author, content))
    final = pandas.DataFrame(zipped_list, 
                                columns=("Date", "Author", "Content"))

        
    # transforms the data frame to a list of dictionaries, according to data_frame argument:
    if df == False:
        final= final.to_dict("records")
            
    return final



    