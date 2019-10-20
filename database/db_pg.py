import psycopg2
from config import Config
import requests
import json

# make a PostgreSQL database

DBNAME = 'gnlosqdo'
USER = 'gnlosqdo'
PASSWORD = 'E29cMSaZaEsQp2kWecFiMkOGWqm4sgpD'
HOST = 'salt.db.elephantsql.com'

# connect to PostgreSQL with a cursor
conn = psycopg2.connect(dbname=DBNAME, user=USER,
            password=PASSWORD,host=HOST)
cur = conn.cursor()
cur.execute('END;',
    'CREATE DATABASE kckstr'
    )
cur.close()

# make some tables
def create_tables():
    """make tables in PostgreSQL database"""
    commands = (
        """DROP TABLE IF EXISTS users;""",
        """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(200) NOT NULL,
            other1 BOOL
        )
        """,
        """INSERT INTO users (user_name) VALUES ('joe');""",
        """DROP TABLE IF EXISTS campaigns;""",
        """
        CREATE TABLE campaigns (
            campaign_id SERIAL PRIMARY KEY,
            other1 BOOL,
            other2 FLOAT(2),
            other3 INTEGER,
            other4 DATE,
            other5 INTERVAL
        )
        """,
        """DROP TABLE IF EXISTS user_campaigns;""",
        """
        CREATE TABLE user_campaigns (
            campaign_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            PRIMARY KEY (campaign_id, 
            user_id), FOREIGN KEY (
                user_id
            ) REFERENCES users (user_id) 
            MATCH SIMPLE ON UPDATE NO 
            ACTION ON DELETE NO ACTION
        )
        """)
    conn = None 

    try:
        DBNAME = 'gnlosqdo'
        USER = 'gnlosqdo'
        PASSWORD = 'E29cMSaZaEsQp2kWecFiMkOGWqm4sgpD'
        HOST = 'salt.db.elephantsql.com'

        # connect to PostgreSQL with a cursor
        conn = psycopg2.connect(dbname=DBNAME, user=USER,
            password=PASSWORD,host=HOST)
        cur = conn.cursor()

        # execute/create the tables 
        for command in commands:
            cur.execute(command)
            conn.commit()

        # close the cursor
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()


# take in API data
def get_results(API):
    """for picking apart the contents of an API"""
    request = r.get(API).json()
    list1 = []
    list2 = [] 
    for i in request['data']: 
        # 'data' is the output of request.keys()
        list1.append(i['dict_a'])
        list2.append(i['dict_b']['sub_a'])
        # json strings are dicts within dicts

    # combine chosen lists 
    data_list = list(tuple(zip(list1, list2)))

    # may use json_normalize (from pandas.io.join)
    #  to convert to pandas dataframe

    # pre-model practice 
    def tuple_transformer(tuples):
    """a function for tuple-list preprocessing practice"""
        values = []
        for i in tuples:
            value = values.append(i[1])
        return values
    # data_list = [('happy', 3), ('sad',5), ('mad',4), ('crazy',7)]
    # test = tuple_transformer(data_list)
    # output: [3, 5, 4, 7]

    # pass through preprocessing function(s)

    # pass through a model 
    def model():
        return "output_prediction_value"

    # consolidate the input and output values
    def aggregator(inputs, outputs):
        pass

    # return in json format
    json_str = json.dumps(data_list)
    
    return "" # json_str 


def insert_user_list(user_list):
    """ insert multiple users into the users table  """
    sql = """INSERT INTO users (user_name) VALUES(%s)"""
    conn = None

    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(dbname=DBNAME, user=USER,
            password=PASSWORD,host=HOST)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, user_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_user_list([
        ('Anna', 1),
     ])

# Want to have this be input(-able)
