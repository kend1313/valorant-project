'''docstring -Ken Dong - agents database application'''
#imports
import sqlite3


#contant and variables
DATABASE = "val.db"


#functions
# 1st function:
def print_all_agents():
    '''print all agents'''
    try:
        # establish a connection to the database
        db = sqlite3.connect(DATABASE)
        # connect with database
        cursor = db.cursor()
        # create a cursor object to interact with the database
        sql = "SELECT * from agents;"
        # SQL quary to select all records from the ‘Agents' table
        cursor.execute(sql)
        # execute the SQL quary
        results = cursor.fetchall()
        #fetch all results from the execute query

        for agent in results:
            # unpack the agent data from the tuple
            agent_id, name, description, profession_id, origin_id, \
            pronouns, race , alses, real_name, relationships = agent
            # the SQL query copied
            print(f"Agent ID: {agent_id}")
            # print the agent id, displayed as agent id : {data input}
            print(f"Name: {name}")
            print(f"Description: {description.strip('\n')}")
            # print the agent description and got rid of any
            # extra line space between this and the next column in results terminal.
            print(f"Profession ID: {profession_id}")
            print(f"Origin ID: {origin_id}")
            print(f"Pronouns: {pronouns}")
            print(f"Species: {race}")
            print(f"Alses: {alses if alses else 'N/A'}")
            # print the alses of agents, automatically displays N/A if there isn't any
            print(f"Real Name: {real_name if real_name else 'N/A'}")
            print(f"Relationships: {relationships if relationships else 'N/A'}")
            print("-" * 40)
            # print a separator line

    except sqlite3.Error as e:
        # print an error message if there's an issue with the database
        print(f"An error occured: {e}")
    finally:
        db.close()
    # close the connection with the database


# 2nd function:
def print_all_agents_by_profession_id():
    '''print all agents in profession id order'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * from Agents ORDER BY professions;"
        # SQL quary to select all records from the 'Agents' table, ordered by 'profession'
        cursor.execute(sql)
        results = cursor.fetchall()

        for agent in results:
            # unpack the agent data from the tuple
            agent_id, name, description, profession_id, origin_id, \
            pronouns, race, alses, real_name, relationships = agent
            # the SQL query copied
            print(f"Agent ID: {agent_id}")
            print(f"Name: {name}")
            print(f"Description: {description.strip('\n')}")
            # print the agent description and got rid of any
            # extra line space between this and the next column in results terminal.
            print(f"Profession ID: {profession_id}")
            print(f"Origin ID: {origin_id}")
            print(f"Pronouns: {pronouns}")
            print(f"Species: {race}")
            print(f"Alses: {alses if alses else 'N/A'}")
            print(f"Real Name: {real_name if real_name else 'N/A'}")
            print(f"Relationships: {relationships if relationships else 'N/A'}")
            print("-" * 40)
            # print a separator line

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        db.close()
        # close the connection with the database

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
        print(val[0])
        # print only the name, no other brackets or quotation mark, displayed nicer.
    db.close()


# 4th function:
def print_professions_of_agents():
    '''print professions of the agents'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = 'SELECT Agents.name, Professions.name from Agents \
        Join Professions On Agents.professions = Professions.id;'
        # SQL quary to select the names from the 'Agents' table and the 'Professions' table
        # Joining the 'Agents' and 'Professions' tables on the 'professions' column in 'Agents'
        # and the 'id' column in 'Professions'
        cursor.execute(sql)
        results = cursor.fetchall()

        for agent_name, profession_name in results:
            # loop through all the results
            print(f"Agent Name: {agent_name}, Profession: {profession_name}")
            # print the agent name and profession nicely
            # using format Agent: {data input}, Profession: {data input}

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

# 5th function:
def print_names_and_race_of_agents():
    '''print the names and race of the agents'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT name, race FROM Agents;"
        # SQL quary to select 'name' and 'race' from the 'Agents' table
        cursor.execute(sql)
        results = cursor.fetchall()

        for name, race in results:
            print(f"Agent Name: {name}, Race: {race}")
            # print the agent name and race nicely
            # using format Agent: {data input}, Race: {data input}
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()


# 6th function:
def print_name_and_descriptions_of_agents():
    '''print the names and descriptions of the agents'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT name, description FROM Agents;"
        # SQL query to select the 'name' and 'description' columns from the 'Agents' table
        cursor.execute(sql)
        results = cursor.fetchall()

        for name, description in results:
            print(f"Agent Name: {name}")
            # print agent name
            print(f"Description: {description.strip()}")
            # print descriptiona and get rid of any extra empty line
            print("-" * 40)

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        db.close()

# 7th function:
def print_name_and_pronouns_of_agents():
    '''print the names and pronouns of the agents'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT name, pronouns FROM Agents;"
        # SQL quary to select names and pronouns of agents from the Agents table
        cursor.execute(sql)
        results = cursor.fetchall()

        for name, pronouns in results:
            print(f"Agent Name: {name}")
            print(f"Pronouns: {pronouns}")
            print("-" * 40)

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        db.close()


# 8th function:
def print_name_and_descriptions_of_abilities():
    '''print the names and descriptions of the abilities'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT name, description FROM Abilities;"
        # SQL query to select the 'name' and 'description' columns from the 'Abilities' table
        cursor.execute(sql)
        results = cursor.fetchall()

        for name, description in results:
            print(f"Ability Name: {name}")
            print(f"Description: {description}")
            # print description
            # don't need the strip method as there is no more variables to be prints after this
            print("-" * 40)

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        db.close()


# 9th function:
def print_all_abilities():
    '''print all the abilities'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM Abilities;"
        # SQL query to select all columns from the 'Abilities' table
        cursor.execute(sql)
        results = cursor.fetchall()

        for ability in results:
            ability_id, name, description, maximum_carry, duration, damage, buff, \
            debuff, cost, points_required, windup = ability
            # SQL query copied
            print(f"Ability ID: {ability_id}")
            print(f"Name: {name}")
            print(f"Description: {description.strip('\n')}")
            # print descriptiona and get rid of any extra empty line
            print(f"Maximum carry: {maximum_carry}")
            print(f"Duration: {duration}")
            print(f"Damage {damage}")
            print(f"Buff: {buff}")
            print(f"Debuff: {debuff}")
            print(f"Cost: {cost}")
            print(f"Points_required: {points_required}")
            print(f"Windup: {windup}")
            # print all the variables in the table serpartely
            # displayed for the user to identify easy
            print("-" * 40)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

# 10th function:
def print_abilities_by_cost():
    '''print all the abiliites alng with the cost'''
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM Abilities ORDER BY cost;"
        # SQL query to select all columns from the 'Abilities' table, ordered by the 'cost' column
        cursor.execute(sql)
        results = cursor.fetchall()

        for ability in results:
            ability_id, name, description, maximum_carry, duration, damage, buff, \
            debuff, cost, points_required, windup = ability
            print(f"Ability ID: {ability_id}")
            print(f"Name: {name}")
            print(f"Description: {description.strip('\n')}")
            # get rid of any extra line space between the next line.
            print(f"Maximum carry: {maximum_carry}")
            print(f"Duration: {duration}")
            print(f"Damage {damage}")
            print(f"Buff: {buff}")
            print(f"Debuff: {debuff}")
            print(f"Cost: {cost}")
            print(f"Points_required: {points_required}")
            print(f"Windup: {windup}")
            print("-" * 40)
            # print a serparator line for better readibility.

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

# 11th function:
def display_options(options):
    '''Display options for the user to select from'''
    for idx, option in enumerate(options, start=1):
        # Iterate over the list of options with an index starting from 1
        print(f"{idx}. {option}")
    while True:
        choice = input("Please select an option by number: ")
        # Prompt the user to select an option by number
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            # check if the input is a digit and within the valid range
            return options[int(choice) - 1]
        # return the selected option
        else:
            print("Invalid choice. Please select a valid number.")
            # print an error message for invalid choices

def insert_a_new_agent():
    '''Insert a new agent'''
    try:
        db = sqlite3.connect(DATABASE)
        # connect to the SQLite database
        cursor = db.cursor()
        # SQL query to insert values into the ‘Agents' table
        sql = "INSERT INTO Agents (name, description, professions, origin, \
        pronouns, race, alses, real_name, relationships) \
        VALUES (?,?,?,?,?,?,?,?,?);"

        while True:
            # Loop to ensure valide agent name input
            name = input("What is the new agent's name? ")
            if name.strip():
                # check if the name is not just whitespace
                break
            else:
                print("Invalid name. Please enter a valid name.")
                # print an error message for invalde name

        description = input("What is the new agent's description? ")
        # Prompt the user to enter the agent's description

        print("Select profession ID:")
        # Display the profession options for the user to choose from
        profession_options = ['controller', 'sentinel', 'initiator', 'duelist']
        profession_choice = display_options(profession_options)
        professions = profession_options.index(profession_choice) + 1
        # Get the index of the selected profession (1-based index)

        print("Select origin ID:")
        # Display the origin options for the user to choose from
        origin_options = ['earth', 'unknown', 'alternative timeline earth']
        origin_choice = display_options(origin_options)
        origin = origin_options.index(origin_choice) + 1
        # Get the index of the selected origin (1-based index)

        print("Select pronouns:")
        # Display the pronouns options for the user to choose from
        pronouns_options = ['He/Him', 'She/Her', 'They/Them']
        pronouns = display_options(pronouns_options)

        race = input("What is the new agent's race? ")
        # Prompt the user to enter the agent's race

        alses = input("What are the new agent's alses? (Enter 'X' if none) ")
        # Prompt the user to enter the agent's alses, with a provision for no alses.
        if alses.upper() == 'X':
            # Set alses to None if the user entered 'X'
            alses = None

        real_name = input("What is the new agent's real name? (Enter 'X' if none) ")
        # Prompt the user to enter the agent's real name, with a provision for no real name.
        if real_name.upper() == 'X':
            # Set real name to None if the user entered 'X'
            real_name = None

        relationships = input("What are the new agent's relationships? (Enter 'X' if none) ")
        # Prompt the user to enter the agent's relationships, with a provision for no relationships.
        if relationships.upper() == 'X':
            # Set relationship to None if the user entered 'X'
            relationships = None

        val = (name, description, professions, origin, pronouns, \
            # Tuple containing all the values to be inserted into the database
               race, alses, real_name, relationships)
        cursor.execute(sql, val)
        # Execute the SQL query with the provided values


        db.commit()
        # Commit the transaction to save the changes into the database.
        print("New agent inserted successfully.")

    except sqlite3.Error as e:
        # Print an error message if any database error occurs
        print(f"An error occurred: {e}")
    finally:
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
# Print a message to users indicating their input wasn't a valid option (if not in the range 1-12)
# This is used for input validation to handle cases where the uer enteres something
# Defined options are 1 - 12.
