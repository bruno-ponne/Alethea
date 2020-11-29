#for submission
from flask import Flask, render_template
app = Flask(__name__)
from Mod_1_API import gather_tweets
from Mod_2_DataAnalysis import draw_graph
from Mod_2_DataAnalysis import delete_plots
from Mod_2_DataAnalysis import compare_tweets
from Mod_2_DataAnalysis import word_cloud

@app.route("/")
def homepage():
    """View function for Home Page."""
    delete_plots()
    name_plot = draw_graph(10)
    name_word_cloud = word_cloud()
    tweets = gather_tweets(n=10, df=False)
    return render_template("home.html", 
                           tweets = tweets, 
                           name_plot = name_plot,
                           name_word_cloud = name_word_cloud)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

