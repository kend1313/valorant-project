#docstring - Ken Dong - Agents database application
#imports

from flask import Flask, render_template # type: ignore

import sqlite3

#contants and variables



#functions



#main code

app = Flask(__name__)

@app.route("/")
def home():
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT Agents.name, Professions.name, Origin.name, real_name from Agents join Professions On Agents.professions = Professions.id join Origin on Agents.origin = origin.id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print them nicely.
    for val in results:
        print(val)

    # close the db.
    db.close()
    return render_template("home.html",agents=results)
# display the home page, connect with home.html

if __name__=='__main__':
    app.run(debug=True, port=4000)