"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)
from gather_twits import gather_twits
from draw_graph import draw_graph


@app.route("/")
def homepage():
    """View function for Home Page."""
    twits = gather_twits(n=1, df=False)
    draw_graph(20)
    return render_template("home.html", twits = twits)





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)