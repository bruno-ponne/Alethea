
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
           
plot_frequency()
