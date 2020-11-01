#for submission
def gather_twits(n, 
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
        twits = api.user_timeline(screen_name = str(element),
                                  count= n,
                                  include_rts = False,
                                  tweet_mode = 'extended')
        for info in twits:
            "ID: {}".format(info.id)
            date.append(str(info.created_at))
            content.append(str(info.full_text))
            author.append(str(element))
  

    # Creates a data frame:   
    zipped_list = list(zip(date, author, content))
    gathered_twits = pandas.DataFrame(zipped_list, 
                                columns=("Date", "Author", "Content"))

        
    # Transforms the data frame to a list of dictionaries, 
    # according to data_frame argument:
    if df == False:
        gathered_twits= gathered_twits.to_dict("records")
            
    return gathered_twits



    