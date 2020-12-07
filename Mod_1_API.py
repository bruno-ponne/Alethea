# =============================================================================
# Module 1 - Gathering Data and Sentiment Analysis
# =============================================================================

def gather_tweets(n, 
                 accounts = ["factcheckdotorg", "Politifact", "snopes"], 
                 df = True):
    
    """
    Collects the last n tweets from the specified accounts.
    
    Parameters
    ----------
    n: int
    An integer specifying how many tweets of each account should be gathered
    
    accounts: list
    A list specifying the names of the accounts from which tweets will be gathered.
    
    df: boolean
    If True returns a data frame with the tweets.
    If False returns a list of dictionaries with the tweets.
    
    Returns
    -------
    A data frame or list of dictionaries with the tweets requested
    
    """
    
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

def sensing(accounts):
    """
    Analyses the sentiment for last 2000 tweets for a specific account 
    
    Parameters
    ----------
    accounts:  the name of the account (the strings that follow the "@" on twitter)  


    Returns
    -------
    A data frame with two columns: Column 1: the the measure of the sentiment in a positive/negative scale
    
     Column 2: The cleaned text of the tweet. All symbols like hashtags and  links removed.
    
    """
    
    # Libraries
    import pandas as pd  
    import tweepy as tw
    import re
    from textblob import TextBlob

                
    # Autentication
    consumer_key= "NF8JKlckrqEpmU1GGvkXJTJh3"
    consumer_secret= 'sBuazfcxTFM9PSEIpa2a64WBeODhofnHgOTx9ZBXYcTXLdO1VW'
    access_token= "1309820560659148802-XR8dXI7lnNHX0D7ZXurqlAYDbJOt0X"
    access_token_secret= "GRvHLEEOg83HfpwSsaZp1fRfz5Et2GF3atciIC7NNVRst"
    
    auth = tw.OAuthHandler(consumer_key, 
                                   consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    userID= accounts    
    
    # Function to clean the text
    def clean_up(txt):
        """Replace URLs found in a text string with nothing 
        (i.e. it will remove the URL, hashtags, @ from the string).
    
        Parameters
        ----------
        txt : string
            A text string that you want to parse and remove urls.
    
        Returns
        -------
        The same txt string with url's removed.
        # """
        #txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)
        txt = re.sub(r'@', '', txt)
        # Remove hashtags
        txt = re.sub(r'#', '', txt)
        # Remove retweets:
        txt = re.sub(r'RT', '', txt)
        # Remove urls
        txt = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', txt)
        txt = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
        
        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
    
    # Routine that gathers the last 2k tweets
   
    tweets = tw.Cursor(api.user_timeline, 
                            screen_name=userID, 
                            count=None,
                            since_id=None,
                            max_id=None,
                            trim_user=True,
                            exclude_replies=True,
                            contributor_details=False,
                            include_entities=False,
                            tweet_mode = 'extended'
                            ).items(2000);
    
    df = pd.DataFrame(data=[clean_up(str(tweet.full_text)) for tweet in tweets],columns=[userID])
                         
    # Create textblob objects of the tweets
        
    sentiment_objects = [TextBlob(tweet) for tweet in df[userID]]
    
    sentiment_objects[0].polarity, sentiment_objects[0]
        
    # Create list of polarity valuesx and tweet text
    sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]  
    sentiment_values[0]
    
    sentiment_df = pd.DataFrame(sentiment_values,columns = ["Polarity",str(userID)])
               
    # Sentiment dataframe
    return sentiment_df




    
