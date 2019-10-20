# run these before entering python
#pip install psycopg2-binary 
#pip install wget

#To connect csv data file to ElephantSQL, run the following in python
import psycopg2

#Set from a .csv file to Postgress (# titanic.csv example..)

# convert .csv to .sqlite
# import sqlite
import sqlite3

# call the dataframe
import pandas as pd
dset = pd.read_csv('Kickstarter.csv')

#Populate the database (sqlite)
# make the engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://',echo=False)

# establish a connection with the desired database
conn = sqlite3.connect('kckstr.sqlite3') 
# connects the file to the database so queries can be run

# make the sqlite file; note you need to specify the connection defined above
dset.to_sql('kckstr', conn)

# then cursor -> used for queries
curs = conn.cursor()

# translate pandas dataframe to sql; run in command line
query = 'SELECT COUNT(*) FROM kckstr;'
engine.execute(query).fetchall() 

# commit each query
conn.commit()

# close up each query
curs.close()    


# from sqlite to Postgress(ElephantSQL)
# connect to Elephant via python 
dbname = 'gnlosqdo'
user = 'gnlosqdo'
password = 'E29cMSaZaEsQp2kWecFiMkOGWqm4sgpD'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()


# connect to sqlite
sl_conn = sqlite3.connect('kckstr.sqlite3')
sl_curs = sl_conn.cursor()

# test output
sl_curs.execute('SELECT COUNT(*) FROM kckstr').fetchall() 
#"You must fetch all rows for the current query before executing 
# new statements using the same connection." https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html 

# get a list of entries
entries = sl_curs.execute('SELECT * FROM kckstr').fetchall()

# check the schema
sl_curs.execute('PRAGMA table_info(kckstr);').fetchall()

# make a datatable 
o_table = """CREATE TABLE kckstr(
    index SERIAL PRIMARY KEY, 
    goal NUMERIC,
    pledged NUMERIC,
    backers_count NUMERIC
    );
    """

pg_curs.execute(o_table)

show_tables = """
SELECT * 
FROM pg_catalog.pg_tables 
WHERE schemaname != 'pg_catalog' 
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

# populate the data to the ElephantSQL instance
for entry in entries:
    insert_entry = """INSERT INTO titanic(
        index, goal, pledged, backers_count
        ) VALUES""" + str(entry[1:]) + ';'
    pg_curs.execute(insert_entry)

# check output
pg_curs.fetchall()

# save changes
pg_curs.close()
pg_conn.commit()


# check process
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic')
pg_entries = pg_curs.fetchall()

for entry, pg_entry in zip(entries, pg_entries):
    assert entry == pg_entry

# need to commit created plot to get showing up on ElephantSQL.