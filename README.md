# Alethea 

Python Project - Autumn, 2020

On Github: https://github.com/brunoponne123/Alethea

Alethea aims to aggregate data on fake news from fact checking Twitter accounts in one web application. The goal of the app is to automate the collection of information in one place helping the people to be informed in a fast and reliable way. 

The project is divided into 3 main modules documented accordingly:


## Module 1 - Web Scraping- Twitter API

This module scrapes twits via the Twitter API relying mostly on the Tweepy module. So far, it is composed by one function:

**gather_tweets**(*n, accounts = ["factcheckdotorg", "Politifact", "snopes"], df = True)*)

This function collects the last n tweets from the specified accounts. 

*n*: integer representing the number of tweets to be gathered per account;
*accounts*: list describing the names of the Twitter accounts from which the tweets will be retrieved. The default accounts are "factcheckdotorg", "Politifact", "snopes";
*df*: boolean specifying whether the data should be returned as a data frame or as a list of dictionaries. The default specification is True (data frame).

**sensing**(accounts)

This function analyses the sentiment for last 2000 tweets for a specific account. It returns a data frame with two columns: Column 1: the the measure of the sentiment in a positive/negative scale

*accounts*:  the name of the account (the strings that follow the "@" on twitter)  


## Module 2 - Data Analysis

This module consists of two functions that analyse data:

***draw_graph***(*words*)

draw_graph creates a bar graph representing the most frequent words employed in the last 200 tweets published by "factcheckdotorg", "Politifact", "snopes". The result is a .png file saved in the *static* folder.

*words*: integer specifying the number of words to be included in the plot.

***plot_frequency***(n)

plot_frequency creates a histogram of the number of tweets created week by week, colored according to the website that published it. The function includes the argument 'n' which allows the specification of the total number of tweets to be scraped and plotted. The result is the printed plot. 

*n*: integer specifying the number of tweets to be included in the plot.

***sentiment_graphs***(*accounts*)

This function plots the graphics of the sentiment of the last 2k tweets and return a png file with the graph

*accounts*:  the name of the account (the strings that follow the "@" on twitter)  

## Module 3 - The Web Application 

This is the module that aggregates all other modules to produce a web application, using the Flask library. This module uses the functions that get the information from the Web Scrapping Module and  the functions that
make the data analysis. It  renders html file with the information incorporated with Jinja2 commands. All the required files for the proper renderization are in the directories "static" and "templates".

## Running the application
Open the Module 3 named "Mod_3_MainApp". And then type in the web browser the IP address that appears in the console (e.g. http://0.0.0.0:3000 or http://127.0.0.1:5000/)
