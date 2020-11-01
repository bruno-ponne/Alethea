
# Top frequent words:
def draw_graph(words):
    import nltk as t
    import pandas
    from gather_twits import gather_twits
    from stop_words import get_stop_words
    import string
    import matplotlib.pyplot as plt
    stop_words = get_stop_words('english')


    x = gather_twits(200, df=False)
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

    dic_data_frame = pandas.DataFrame.from_dict(dictionary, 
                                            orient = "index",
                                            columns = ["Counts"])

    dic_data_frame = dic_data_frame.sort_values(by=['Counts'], 
                                                ascending = False)

    top_words = dic_data_frame.head(words)
    top_words.plot.bar()
    plt.savefig('static/plot.png', bbox_inches = "tight")

# Histogram:
def plot_frequency(n = 600):
        
    from plotnine import ggplot, aes, geom_histogram,  scale_x_datetime, labs, theme_minimal 
    from gather_twits import gather_twits
    from mizani.breaks import date_breaks
    from mizani.formatters import date_format
    import pandas
     
    df = pandas.DataFrame(gather_twits(n))
       
    plot1 = (ggplot(df, aes(x = 'Date', fill = 'Author')) +
           geom_histogram() +
           scale_x_datetime(breaks=date_breaks('1 week')) +
           labs(x = "Time in weeks", y = "Number of tweets by source") +
           theme_minimal()
           )
    return print(plot1)
           
