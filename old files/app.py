# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:29:48 2020

@author: diego
"""
#%%
import tweepy

auth = tweepy.OAuthHandler("NF8JKlckrqEpmU1GGvkXJTJh3", 
                           "sBuazfcxTFM9PSEIpa2a64WBeODhofnHgOTx9ZBXYcTXLdO1VW")

auth.set_access_token("1309820560659148802-XR8dXI7lnNHX0D7ZXurqlAYDbJOt0X", 
                     "GRvHLEEOg83HfpwSsaZp1fRfz5Et2GF3atciIC7NNVRst")
api = tweepy.API(auth)
userID = "PolitiFact"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                          )

#%%
from flask import Flask, render_template
app = Flask(__name__)

#%%
@app.route("/") 
def hello1():
    content = []
    for info in tweets[:3]:
        content.append(info.full_text)
    return "<center><b>Politifact</b><br><br></center>"+content[2]+"<br><br>"+content[1]+"<br><br>"+content[0]
  

   
#%%
@app.route('/square/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of "+ str(number) +" is: "+ str(number * number) 



if __name__=='__main__':
    app.run()
