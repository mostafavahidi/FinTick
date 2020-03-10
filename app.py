from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def analyze():
    if request.method == "POST":
        tickerName = request.form["tickerName"]
        return redirect(url_for("tickerCalc", ticker=tickerName))
    else:
	    return render_template("analyze.html")

@app.route("/<ticker>")
def tickerCalc(ticker):
    return f"<h1>{ticker}</h1>"



if __name__ == "__main__":
    app.run(debug=True)