from config import Config
from flask import Flask, render_template, request
import json
from .model import model
import psycopg2
import requests

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
        """DROP TABLE IF EXISTS users CASCADE;""",
        """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(200) NOT NULL,
            other1 BOOL
        )
        """,
        """INSERT INTO users (user_name) VALUES ('joe');""",
        """DROP TABLE IF EXISTS campaigns CASCADE;""",
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
        """DROP TABLE IF EXISTS user_campaigns CASCADE;""",
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


    def tuple_transformer(tuples):
    """a function for tuple-list preprocessing practice"""
        values = []
        for i in tuples:
            value = values.append(i[1])
        return values
    # data_list = [('happy', 3), ('sad',5), ('mad',4), ('crazy',7)]
    # test = tuple_transformer(data_list)
    # output -> [3, 5, 4, 7]
    return tuple_transformer(data_list)


    # pass through a machine-learning model (MLM)
    def predict(parameters):
    """ make a prediction using the MLM"""
        
        # for inter-flask functionality use request module
        # Eg. parameter_a, parameter_b = [request.values['parameter_a'],
        #                            request.values['parameter_b']]

        if parameters[0] == 1106 and parameters[2] == 'Luc':
            prediction = 'Happy Birthday!!!'
        else:
            prediction = model(parameters)
            all_values = parameters.append(prediction)
        
        return all_values


    def new(params_list):
    """ recipe for passing list of tuples through a function """
        for params in params_list:
            a = params[0]
            b = params[1]
            c = params[2]
            out = b + c
        print(out)
        #return out

    # return in json format
    json_str = json.dumps(data_list)
    
    return "" # json_str 


# sample postgres entry insert function
def insert_user_list(user_list):
    """ insert multiple users into the users table  """
    sql = """INSERT INTO users (user_name) VALUES(%s)"""
    conn = None

    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(dbname=DBNAME, user=USER,
            password=PASSWORD,host=HOST)
        cur = conn.cursor()

        # execute the INSERT statement
        cur.executemany(sql, user_list)

        conn.commit()
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
