''' docstring - Ken Dong - Agents database application '''
# imports

import sqlite3

from flask import Flask, render_template, abort, request

app = Flask(__name__)


# Home Route
@app.route("/")
def home():
    '''
    renders the home page
    '''
    return render_template("home.html")


# search bar
@app.route('/search')
def search():
    '''
    renders the search bar in home page
    '''
    query = request.args.get('query', '').strip()

    if not query:
        # check if the query is empty
        return render_template('404.html'), 404

    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Agents WHERE name LIKE ?"
    cursor.execute(sql, ('%' + query + '%',))
    results = cursor.fetchall()
    db.close()

    return render_template('search_bar.html', query=query, results=results)


# Purpose Route
@app.route("/purpose")
def purpose():
    '''
    renders the purpose page
    '''
    return render_template("purpose.html")


# Agents Table Route
@app.route("/agentstable")
def agentstable():
    '''
    renders the agentstable page
    '''
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT Agents.id, Agents.name, Professions.name, \
    Origin.name, real_name, Agents.image, \
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
    return render_template("agentstable.html", agents=results)
# display the agents page, connect with agents.html


# Professionstable Route
@app.route("/professionstable")
def professionstable():
    '''
    renders the professionstable page
    '''
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT name, description, image FROM Professions;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print them nicely
    for val in results:
        print(val[0].encode("utf-8"))
    db.close()
    return render_template("professionstable.html", professions=results)


# Professions Route
@app.route("/professions")
def professions():
    '''
    renders the professions page
    '''
    db = sqlite3.connect('val.db')
    cursor = db.cursor()
    sql = "SELECT name, description, image FROM Professions;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("professions.html", professions=results)


# Agents Detail Route
@app.route("/agent/<int:agent_id>")
def all_agents(agent_id):
    '''
    renders the agents detailed page
    '''
    if agent_id < 1 or agent_id > 25:
        # If the ID is out of the valid range, trigger a 404 error
        abort(404)

    db = sqlite3.connect('val.db')
    cursor = db.cursor()

    # Query to fetch the agent's details
    sql = """
    SELECT Agents.name, Agents.description, Professions.name, Origin.name,
           Agents.pronouns, Agents.race, Agents.alses, Agents.real_name,
           Agents.relationships, Agents.image
    FROM Agents
    JOIN Professions ON Agents.professions = Professions.id
    JOIN Origin ON Agents.origin = Origin.id
    WHERE Agents.id = ?;
    """
    cursor.execute(sql, (agent_id,))
    agent = cursor.fetchone()

    if not agent:
        # If no agent was found, trigger a 404 error
        db.close()
        abort(404)

    # Query to fetch the agent's abilities
    abilities_sql = """
    SELECT Abilities.name, Abilities.description, Abilities.MaximumCarry,
           Abilities.duration, Abilities.damage, Abilities.buff,
           Abilities.debuff, Abilities.cost, Abilities.PointsRequired,
           Abilities.windup
    FROM Abilities
    JOIN Agent_Ability ON Abilities.id = Agent_Ability.ability_id
    WHERE Agent_Ability.agent_id = ?;
    """
    cursor.execute(abilities_sql, (agent_id,))
    abilities = cursor.fetchall()

    db.close()

    return render_template('all_agents.html', agent=agent, abilities=abilities)


# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(_e):
    '''
    renders the 404 page
    '''
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=4000)
