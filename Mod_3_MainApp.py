#for submission
from flask import Flask, render_template
app = Flask(__name__)
from Mod_1_API import gather_twits
from Mod_2_DataAnalysis import draw_graph
from Mod_2_DataAnalysis import delete_plots
from Mod_2_DataAnalysis import plot_frequency


@app.route("/")
def homepage():
    """View function for Home Page."""
    delete_plots()
    plot_frequency()
    name_plot = draw_graph(10)
    twits = gather_twits(n=5, df=False)
    return render_template("home.html", twits = twits, name_plot = name_plot)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

