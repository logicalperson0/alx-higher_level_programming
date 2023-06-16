Object-relational mapping
==========================

Project done during Full Stack Software Engineering studies at ALX.

It aims to learn about how to connect to a MySQL database from a Python script, what ORM means and how to map a Python Class to a MySQL table.

Technologies
============


    MySQL
    MySQLdb,
    sqlalchemy,
    Python Scripts are written with Python3
    Tested on Ubuntu 22
    
Files
=====

All the following files are scripts of MySQL:

Filename 	Description
========================

0-select_states.py 	Lists all states from the database hbtn_0e_0_usa

1-filter_states.py 	Lists all states with a name starting with N from the database hbtn_0e_0_usa

2-my_filter_states.py 	Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument

3-my_safe_filter_states.py 	Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument without injection

4-cities_by_state.py 	Lists all cities from the database hbtn_0e_4_usa

5-filter_cities.py 	Takes in the name of a state as an argument and lists all cities of that state

model_state.py 	Contains the class definition of a State and an instance Base = declarative_base()

7-model_state_fetch_all.py 	Lists all State objects from the database hbtn_0e_6_usa

