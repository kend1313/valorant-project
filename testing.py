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
    # connect with database
    cursor = db.cursor()
    # create a cursor object to interact with the database
    sql = "SELECT * from agents;"
    # SQL quary to select all records from the ‘Agents' table
    cursor.execute(sql)
    # execute the SQL quary stored in the variable (sql)
    results = cursor.fetchall()
    #loop through all the results
    for val in results:
        print(val)
    # Iterate through the results and print each value
    db.close()
    # close the connection with the database


# 2nd function:
def print_all_agents_by_profession_id():
    '''print all agents in profession id order'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Agents ORDER BY professions;"
    # SQL quary to select all records from the 'Agents' table, ordered by the 'profession' column
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
    # SQL quary to select 'name' column from the 'Agents' table
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
    sql = 'SELECT Agents.name, Professions.name from Agents \
    join Professions On Agents.professions = Professions.id;'
    # SQL quary to select the names from the 'Agents' table and the 'Professions' table
    # Joining the 'Agents' and 'Professions' tables on the 'professions' column in 'Agents'
    # and the 'id' column in 'Professions'
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
    # SQL quary to select 'name' and 'race' from the 'Agents' table
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
    # SQL query to select the 'name' and 'description' columns from the 'Agents' table
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
    # SQL quary to select names and pronouns of agents from the Agents table
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
    # SQL query to select the 'name' and 'description' columns from the 'Abilities' table
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
    # SQL query to select all columns from the 'Abilities' table
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
    # SQL query to select all columns from the 'Abilities' table, ordered by the 'cost' column
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
    sql = "INSERT INTO Agents (name, pronouns) \
    VALUES (?,?);"
    # SQL query to insert values into the 'Agents' table for the 'name' and 'pronouns' columns
    name = input("What name is the new agent? ")
    # asking the user to input a agent name
    pronouns = input("What pronouns does the new agent have? ")
    # asking the user to input the new agent's pronouns
    val = (name, pronouns)
    cursor.execute(sql, val)
    # Execute the SQL query with the provided values for name and pronouns
    db.commit()
    # To Commit and save the changes into the database
    db.close()
    # Close the connection with the database


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
11. Insert a new agent
12. Exit
""")
# These are the outputs in the terminal when user runs the program
# for the user to see what are the choices
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
        insert_a_new_agent()
    elif user_input == "12":
        break
    else:
        print("That was not an option\n")