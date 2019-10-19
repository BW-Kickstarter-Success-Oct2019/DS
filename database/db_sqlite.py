import pandas as pd 
import sqlite3

# Connect to sqlite file and create cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Make a table
curs.execute('DROP TABLE IF EXISTS demo;')
curs.execute('CREATE TABLE demo (s TEXT, x INTEGER, y INTEGER);').fetchall()

curs.execute("""INSERT INTO demo VALUES ('g', 3, 9);""")
curs.execute("""INSERT INTO demo VALUES ('v', 5, 7);""")
curs.execute("""INSERT INTO demo VALUES ('f', 8, 7);""")

# Commit the table / save it
conn.commit()
conn.close()

# Query: find number of rows
query1 = """SELECT COUNT(*) FROM demo;"""
# Query: find number of rows where x and y >= 5
query2 = """SELECT COUNT(*) AS Num_rows FROM demo
WHERE x >= 5 AND y >= 5;"""
# Query: find number of unique y-values
query3 = """SELECT COUNT(DISTINCT y) AS Unique_y_values FROM demo;"""

# Define a function to loop through all queries and return their outputs
queries = [query1, query2, query3]

def executer(list_queries):
    for i in list_queries:
        
        conn = sqlite3.connect('demo_data.sqlite3')
        
        # make a cursor
        curs = conn.cursor()

        # print results of each query
        print(curs.execute(i).fetchall())

# Call the function with specified list of queries
executer(queries)