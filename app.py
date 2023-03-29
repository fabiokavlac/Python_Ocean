from flask import Flask, render_template
import moment

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clock")
def clock():
    time = moment.now().strftime("%H:%M:%S")
    return time

if __name__ == "__main__":
    app.run(debug=True)
