import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return None
    



def create_table(conn,create_table_sql):
    #create a table from the create_table_sql statement
    #:param conn: Connection object
    #:param create_table_sql: a CREATE TABLE statement
    #:return:
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "C:\\sqlite\db\pythonsqlite.db"

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects(
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end date text
    ); """

    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks(
        id integer PRIMARY KEY,
        name text OT NULL,
        priority integer,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text NOT NULL,
        end_date text NOT NULL
    ); """

    #create a database connection
    conn = create_connection(database)
    if conn is not None:
        #create projects table
        create_table(conn,sql_create_projects_table)
        #create tasks table
        create_table(conn,sql_create_tasks_table)
    else:
        print("Error! Cannot create the database connection")

if __name__ =='__main__':
    main()
