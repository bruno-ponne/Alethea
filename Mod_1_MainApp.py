#for submission
from flask import Flask, render_template
app = Flask(__name__)
from Mod_2_API import gather_twits



@app.route("/")
def homepage():
    """View function for Home Page."""
    twits = gather_twits(n=3, df=True)
    return render_template("home.html", twits = twits)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
    
    