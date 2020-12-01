#for submission
# Top frequent words:
def draw_graph(words):
    import nltk as t
    import pandas
    import random
    from Mod_1_API import gather_tweets,sensing
    from stop_words import get_stop_words
    import string
    import matplotlib.pyplot as plt
    import seaborn as sns
    from wordcloud import WordCloud
    stop_words = get_stop_words('english')


    x = gather_tweets(200, df=False)
    list3 = ["“","”","’", "https","'s", "s", "''","``"]
    list1 = []
    for element in x:
        list1.append(t.word_tokenize(element["Content"]))

    list2 = []
    for sublist in list1:
        for item in sublist:
            list2.append(item)

    # add punctuation to stop words:
        for e in string.punctuation:
            stop_words.append(e)
    
    for i in list3:
        stop_words.append(i)

    wordsFiltered = []
    for w in list2:
        if w not in stop_words:
            wordsFiltered.append(w)

    dictionary = {}

    for element in wordsFiltered:
        dictionary.update({element: wordsFiltered.count(element)})
    
    dic_data_frame = pandas.DataFrame(list(dictionary.items()),columns = ['Word', 'Counts'])


    dic_data_frame = dic_data_frame.sort_values(by=['Counts'], 
                                                ascending = False)

    
    x = random.randint(1, 1000)
    name_fig = str(x)+"_"
    top_words = dic_data_frame.head(words)
    sns.set_style('whitegrid')
    # create plot
    sns.barplot(x = 'Counts', y="Word",  color = "blue", data = top_words)
    plt.title('The top '+ str(words) + ' words used by fact-check websites')
    plt.xlabel('Counts')
    plt.ylabel('Words')
    plt.savefig("static/"+name_fig+".png")
    return name_fig+".png"



# Histogram:
def plot_frequency(n = 200):
        
    from plotnine import ggplot, aes, geom_histogram,  scale_x_datetime, labs, theme_minimal, ggsave 
    from Mod_1_API import gather_tweets
    from mizani.breaks import date_breaks
    from mizani.formatters import date_format
    import pandas
    
     
    df = pandas.DataFrame(gather_tweets(n))
       
    plot1 = (ggplot(df, aes(x = 'Date', fill = 'Author')) +
           geom_histogram() +
           scale_x_datetime(breaks=date_breaks('1 week')) +
           labs(x = "Time in weeks", y = "Number of tweets by source") +
           theme_minimal()
           )
    ggsave(plot = plot1, filename = "test.png", path = "static/")


def delete_plots():
    import os
    folder_path = ("static/")
    all_files = os.listdir(folder_path)
    for images in all_files:
        if images.endswith("_.png"):
            os.remove(os.path.join(folder_path, images))
            
def compare_tweets():
    
    import nltk as t
    import pandas as pd
    from stop_words import get_stop_words
    import string
    import re
    from Mod_1_API import gather_many_tweets
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    stop_words = get_stop_words('english')

    data_snopes = gather_many_tweets("snopes", 3000)
    time.sleep(2)
    data_fact = gather_many_tweets("factcheckdotorg", 3000)
    time.sleep(2)
    data_poli = gather_many_tweets("Politifact", 3000)
    list0 = [data_snopes, data_fact, data_poli]

    #Trump-------------------------------------------------------------------------
    list1=[]
    for data in list0:
        for element in data:
            y = t.word_tokenize(element["Content"])
            if "Trump" in y:
                if "Biden" not in y:
                    list1.append(y)
    list2 = []
    for sublist in list1:
        for item in sublist:
            list2.append(item)
        
    list3 = ["“","”","’", "https","'s", "s", "''","``","Trump","Donald","President"]

    # add punctuation to stop words:
    for e in string.punctuation:
        stop_words.append(e)
    for i in list3:
        stop_words.append(i)

    wordsFiltered = []
    for w in list2:
        if w not in stop_words:
            wordsFiltered.append(w)
    wordsFiltered = [x.lower() for x in wordsFiltered]
        
    dictionary = {}
    for element in wordsFiltered:
        dictionary.update({element: wordsFiltered.count(element)})



    search_key = ["false","fake","misleading", "wrong", "fraud", "innacurate","incorrect", "^lie","fabricated","fictitious", "deceit", "erroneous","distorted","unfounded","mistaken","untrue"]
    res={}
    dic_trump = {}
    for i in search_key:
        res = {key:val for key, val in dictionary.items() if re.search(i, key)}
        dic_trump = {**res, **dic_trump}
    
    
    
#--------------------------------------------------------------------------
# Biden:
    list1=[]
    for data in list0:
        for element in data:
            y = t.word_tokenize(element["Content"])
            if "Biden" in y:
                if "Trump" not in y:
                    list1.append(y)
    list2 = []
    for sublist in list1:
        for item in sublist:
            list2.append(item)
        
    list3 = ["“","”","’", "https","'s", "s", "''","``","Trump","Donald","President"]

    # add punctuation to stop words:
    for e in string.punctuation:
        stop_words.append(e)
    for i in list3:
        stop_words.append(i)

    wordsFiltered = []
    for w in list2:
        if w not in stop_words:
            wordsFiltered.append(w)
    wordsFiltered = [x.lower() for x in wordsFiltered]
        
    dictionary = {}
    for element in wordsFiltered:
        dictionary.update({element: wordsFiltered.count(element)})

    search_key = ["false","fake","misleading", "wrong", "fraud", "innacurate","incorrect", "^lie","fabricated","fictitious", "deceit", "erroneous","distorted","unfounded","mistaken","untrue"]
    res={}
    dic_biden = {}
    for i in search_key:
        res = {key:val for key, val in dictionary.items() if re.search(i, key)}
        dic_biden = {**dic_biden,**res }


    df_trump = pd.DataFrame(list(dic_trump.items()),columns = ['word', 'counts'])
    df_trump = df_trump.sort_values(by="counts", ascending=False)
    df_trump = df_trump[:10]
    df_biden = pd.DataFrame(list(dic_biden.items()),columns = ['word', 'counts'])
    df_biden = df_biden.sort_values(by="counts", ascending=False)
    df_biden = df_biden[:10]
    df_biden["Candidate"] = "Biden"
    df_trump["Candidate"] = "Trump"
    merged_df = df_trump.append(df_biden)


    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    # create plot
    sns.barplot(x = 'counts', y= "word", data = merged_df, hue="Candidate", palette=("red", "mediumblue"))
    plt.title('Fake news related words in tweets that mention or Trump or Biden')
    plt.xlabel('Counts')
    plt.ylabel('Words')
    plt.savefig("static/compare.png")
    
def word_cloud():
    import nltk as t
    import pandas
    import random
    from Mod_1_API import gather_tweets
    from stop_words import get_stop_words
    import string
    import matplotlib.pyplot as plt
    import seaborn as sns
    from wordcloud import WordCloud
    stop_words = get_stop_words('english')


    x = gather_tweets(200, df=False)
    list3 = ["“","”","’", "https","'s", "s", "''","``"]
    list1 = []
    for element in x:
        list1.append(t.word_tokenize(element["Content"]))

    list2 = []
    for sublist in list1:
        for item in sublist:
            list2.append(item)

    # add punctuation to stop words:
        for e in string.punctuation:
            stop_words.append(e)
    
    for i in list3:
        stop_words.append(i)

    wordsFiltered = []
    for w in list2:
        if w not in stop_words:
            wordsFiltered.append(w)

    dictionary = {}

    for element in wordsFiltered:
        dictionary.update({element: wordsFiltered.count(element)})
        
    x = random.randint(1, 10000)
    name_fig = str(x)+"_"
    wordcloud = WordCloud(color_func=lambda *args, **kwargs: (0,0,0),background_color='#e4faf4', height = 150, width=600)
    wordcloud.generate_from_frequencies(frequencies=dictionary)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    wordcloud.to_file("static/"+name_fig+".png")
    return name_fig+".png"



def sentiment_graphs(accounts):
    from Mod_1_API import sensing
    import matplotlib.pyplot as plt
    import seaborn as sns
    import random
    from pylab import rcParams
    rcParams['figure.figsize'] = 12, 8
    import warnings
    warnings.filterwarnings("ignore")
    sns.set(font_scale=1.5)
    sns.set_style("whitegrid")
    
    
    sent = sensing(accounts)
    
        #%%Plotting the values
    fig, ax = plt.subplots(figsize=(8, 6))
     
     # Plot histogram of the polarity values
    sent.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
                  ax=ax,
                  color="purple")   
    y = random.randint(1, 1000)
    name_fig = str(y)+"_"
    sns.set_style('whitegrid')
    plt.title("Sentiments from Tweets of Factcheckers- "+ str(accounts))
    plt.savefig("static/"+name_fig+".png")
    return name_fig+".png"
