#for submission
def gather_tweets(n, 
                 accounts = ["factcheckdotorg", "Politifact", "snopes"], 
                 df = True):
    # Libraries:
    import tweepy
    import pandas
    from datetime import datetime

    # Authentication:
    auth = tweepy.OAuthHandler("SNXprfNdEjmTiQG4MjMI8ANoQ", 
                               "oFpNh8EuhGt1m06SJwLxl7tp3uumGAEt5SK7m5AW3IUxCls2MC")
    api = tweepy.API(auth)

    # Variables needed:
    zipped_list = []
    date = []
    content = []
    author = []

    
    for element in accounts:
        tweets = api.user_timeline(screen_name = str(element),
                                  count= n,
                                  include_rts = False,
                                  tweet_mode = 'extended')
        for info in tweets:
            "ID: {}".format(info.id)
            date.append(str(info.created_at))
            content.append(str(info.full_text))
            author.append(str(element))
  

    # Creates a data frame:   
    zipped_list = list(zip(date, author, content))
    gathered_tweets = pandas.DataFrame(zipped_list, 
                                columns=("Date", "Author", "Content"))

        
    # Transforms the data frame to a list of dictionaries, 
    # according to data_frame argument:
    if df == False:
        gathered_tweets= gathered_tweets.to_dict("records")
            
    return gathered_tweets

def gather_many_tweets(account, t):
    # Libraries:
    import tweepy
    import pandas
    from datetime import datetime
    import time

    # Authentication:
    auth = tweepy.OAuthHandler("SNXprfNdEjmTiQG4MjMI8ANoQ", 
                               "oFpNh8EuhGt1m06SJwLxl7tp3uumGAEt5SK7m5AW3IUxCls2MC")
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name = account,
                                  count= 1,
                                  include_rts = False,
                                  tweet_mode = 'extended')
    for i in tweets:
        x= i.id
    n=0
    date = []
    content = []
    id_ = []
    author = []

    while n<t:
        tweets = api.user_timeline(screen_name = account,
                                  count= 200,
                                  max_id = x,
                                  include_rts = False,
                                  tweet_mode = 'extended')


        for i in tweets:
            date.append(str(i.created_at))
            content.append(str(i.full_text))
            id_.append(str(i.id))
            author.append(account)
        x = min(id_)
        n = len(content)
        time.sleep(1)
    
    zipped_list = list(zip(date, author, content, id_))
    gathered_tweets = pandas.DataFrame(zipped_list, 
                                columns=("Date", "Author", "Content", "Id"))
    gathered_tweets = gathered_tweets[:t]
    gathered_tweets = gathered_tweets.to_dict("records")
    return gathered_tweets




    
