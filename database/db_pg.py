import psycopg2
from config import Config

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
    # insert one vendor
    # insert_user("Joey")
    # insert multiple vendors
    insert_user_list([
        ('Anna',),
        ('Marie',),
        ('Teddy',),
        ('Quincy',),
    ])

    

