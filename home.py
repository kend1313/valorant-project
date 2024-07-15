#docstring - Ken Dong - Agents database application
#imports

import sqlite3

from flask import Flask, render_template # type: ignore

app = Flask(__name__)

# Home Route
@app.route("/")


@app.route("/agents")
def agents():
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT Agents.name, Professions.name, Origin.name, real_name, Agents.image, \
    Professions.image, Origin.image from Agents \
    join Professions \
    On Agents.professions = Professions.id \
    join Origin on Agents.origin = origin.id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print them nicely.
    for val in results:
        print(val[0].encode("utf-8"))
    db.close()
    # close the database.
    return render_template("agents.html",agents=results)
# display the agents page, connect with agents.html


if __name__=='__main__':
    app.run(debug=True, port=4000)
