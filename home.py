#docstring - Ken Dong - Agents database application
#imports

import sqlite3

from flask import Flask, render_template # type: ignore

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Purpose Route
@app.route("/purpose")
def purpose():
    return render_template("purpose.html")

# Agents Table Route
@app.route("/agentstable")
def agentstable():
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT Agents.id, Agents.name, Professions.name, Origin.name, real_name, Agents.image, \
    Professions.image, Origin.image from Agents \
    join Professions \
    On Agents.professions = Professions.id \
    join Origin on Agents.origin = origin.id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print them nicely.
    for val in results:
        print(val[1].encode("utf-8"))
    db.close()
    # close the database.
    return render_template("agentstable.html",agents=results)
# display the agents page, connect with agents.html

# Professionstable Route
@app.route("/professions")
def professionstable():
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT name, description, image FROM Professions;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print them nicely
    for val in results:
        print(val[0].encode("utf-8"))
    db.close()
    return render_template("professionstable.html",professions=results)

# Agents Detail Route
@app.route("/agent/<int:id>")
def all_agents(id):
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT Agents.name, Agents.description, Professions.name, Origin.name, \
    Agents.pronouns, Agents.race, Agents.alses, Agents.real_name, \
    Agents.relationships, Agents.image \
    FROM Agents \
    JOIN Professions ON Agents.professions = Professions.id \
    JOIN Origin ON Agents.origin = Origin.id \
    WHERE Agents.id = ?;"
    cursor.execute(sql, (id,))
    agent = cursor.fetchone()
    
    abilities_sql = "SELECT * FROM agent_ability WHERE agent_id =?;"
    cursor.execute(abilities_sql,(id,))
    abilities = cursor.fetchall()
    
    db.close()
    return render_template('all_agents.html', agent=agent,abilities=abilities)



if __name__=='__main__':
    app.run(debug=True, port=4000)
    app.run(debug=True)
