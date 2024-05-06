from flask import Flask, render_template # type: ignore
import sqlite3
db = sqlite3.connect('val.db')
cur


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
# display the home page, connect with home.html

if __name__=='__main__':
    app.run(debug=True, port=4000)