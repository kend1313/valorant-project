'''docstring -Ken Dong - agents database application'''
#imports
import sqlite3

#contant and variables
DATABASE = "val.db"


#functions
# 1st function:
def print_all_agents():
    '''print all agents'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    for val in results:
        print(val)
    db.close()


# 2nd function:
def print_all_agents_by_profession_id():
    '''print all agents in profession id order'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from agents ORDER BY professions;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 3rd function:
def print_names_of_agents():
    '''print names of the agents'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name FROM Agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 4th function:
def print_professions_of_agents():
    '''print professions of the agents'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Agents.name, Professions.name from Agents join Professions On Agents.professions = Professions.id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 5th function:
def print_names_and_race_of_agents():
    '''print the names and race of the agents'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name, race FROM Agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 6th function:
def print_name_and_descriptions_of_agents():
    '''print the names and descriptions of the agents'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name, description FROM Agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 7th function:
def print_name_and_pronouns_of_agents():
    '''print the names and pronouns of the agents'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name, pronouns FROM Agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 8th function:
def print_name_and_descriptions_of_abilities():
    '''print the names and descriptions of the abilities'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name, description FROM Abilities;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 9th function:
def print_all_abilities():
    '''print all the abilities'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Abilities;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 10th function:
def print_abilities_by_cost():
    '''print all the abiliites alng with the cost'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Abilities ORDER BY cost;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()


# 11th function:
def insert_a_new_agent():
    '''inser a new agent'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "INSERT INTO Agents (name, pronouns) VALUES (?,?);"
    cursor.execute(sql)
    results = cursor.fetchall()
    for val in results:
        print(val)
    db.close()



#main code
while True:
    user_input = input(
"""
What would you like to do.
1. Print all agents
2. Print all agents by professions id
3. Print all agents names
4. Print all agents names and professions
5. Print all agents names and races
6. Print all agents names and descriptions
7. Print all agents names and pronouns
8. Print all abilities names and descriptions
9. Print all abilities
10. Print all abilities sorted by costs
11. Exit
""")
    if user_input == "1":
        print_all_agents()
    elif user_input == "2":
        print_all_agents_by_profession_id()
    elif user_input == "3":
        print_names_of_agents()
    elif user_input == "4":
        print_professions_of_agents()
    elif user_input == "5":
        print_names_and_race_of_agents()
    elif user_input == "6":
        print_name_and_descriptions_of_agents()
    elif user_input == "7":
        print_name_and_pronouns_of_agents()
    elif user_input == "8":
        print_name_and_descriptions_of_abilities()
    elif user_input == "9":
        print_all_abilities()
    elif user_input == "10":
        print_abilities_by_cost()
    elif user_input == "11":
        break
    else:
        print("That was not an option\n")