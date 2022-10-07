from configparser import ConfigParser
import psycopg2
import psycopg2.extras
from os.path import join, dirname

def config(filename=join(dirname(__file__), 'database.ini'), section='prod-postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

        print(f'Trying to connect to {section}')
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db



# Use this file for testing the python functions defined elsewhere

"""Test db connection"""


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_db_conn(section:str = 'prod-postgresql'):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config(section=section)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        print('Connected successfully...')
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def close_db_conn(conn):
    if conn is not None:
        conn.close()
        print('Database connection closed.')
    else:
        print('Database connection not closed because it doesn\'t exist.')


# # Connect to an existing database
# conn = get_db_conn()

# # Open a cursor to perform database operations
# cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
