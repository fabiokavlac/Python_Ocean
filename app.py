from flask import Flask, render_template
import moment
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clock")
def clock():
    tz = pytz.timezone("America/Sao_Paulo")
    time = datetime.now(tz).strftime("%H:%M:%S")
    return time

if __name__ == "__main__":
    app.run(debug=True)
