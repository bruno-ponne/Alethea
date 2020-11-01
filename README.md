# Alethea

Python Project - Autumn, 2020

Alethea aims to aggregate data on fake news from fack checking Twitter accounts in one web application. The goal of the app is to automatize the collection of information in one place helping the people to be informed in a fast and reliable way. 

The project is divided into 3 main modules documented accordingly:


## Module 1 - The Web Application 

## Module 2 - Twitter API

This module relies mostly on the Tweepy module to gather twits via the Twitter API. So far, it is composed by one function:

**gather_twits**(*n, accounts = ["factcheckdotorg", "Politifact", "snopes"], df = True)*)

This function collects the last n twits from the specified accounts. 

*n*: integer representing the number of twits to be gathered per account;
*accounts*: list describing the names of the Twitter accounts from which the twits will be retrieved. The default accounts are "factcheckdotorg", "Politifact", "snopes";
*df*: boolean specifying whether the data should be returned as a data frame or as a list of dictionaries. The default specification is True (data frame).


## Module 3 - Data Analysis

This module consists of two functions that analyse data:

***draw_graph***(*words*)

draw_graph creates a bar graph representing the most frequent words employed in the last 200 twits published by "factcheckdotorg", "Politifact", "snopes". The result is a .png file saved in the *static* folder.

*words*: integer specifying the number of words to be included in the plot.
