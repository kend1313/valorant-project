from flask import Flask, render_template # type: ignore

import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT name,professions,origin,real_name FROM Agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    # close the db.
    db.close()
    return render_template("home.html",agents=results)
# display the home page, connect with home.html

if __name__=='__main__':
    app.run(debug=True, port=4000)