#for submission
from flask import Flask, render_template
app = Flask(__name__)
from Mod_1_API import gather_tweets
from Mod_2_DataAnalysis import draw_graph
from Mod_2_DataAnalysis import delete_plots
from Mod_2_DataAnalysis import compare_tweets
from Mod_2_DataAnalysis import word_cloud
from Mod_2_DataAnalysis import sentiment_graphs


@app.route("/")
def homepage():
    """View function for Home Page."""
    delete_plots()
    name_plot = draw_graph(10)
    name_word_cloud = word_cloud()
    sentiment_analysis1 = sentiment_graphs("Politifact")
    sentiment_analysis2 = sentiment_graphs("factcheckdotorg")
    sentiment_analysis3 = sentiment_graphs("snopes")
        
    tweets = gather_tweets(n=10, df=False)
    return render_template("home.html", 
                           tweets = tweets, 
                           name_plot = name_plot,
                           name_word_cloud = name_word_cloud, 
                           sentiment_analysis1 = sentiment_analysis1,
                           sentiment_analysis2 = sentiment_analysis2,
                           sentiment_analysis3 = sentiment_analysis3)


if __name__ == "__main__":
    app.run()
