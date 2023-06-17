#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.name, states.name \
                 FROM cities, states \
                 WHERE states.name = %s AND \
                 states.id = cities.state_id;",
                (argv[4],))

    states_cities = cur.fetchall()

    print(", ".join([i[0] for i in states_cities]))

    # for i in states_cities:
    #   j = "".join(i[0])
    #   print("{:s}, ".format(j), end="")
    # print()

    cur.close()
    db.close()
