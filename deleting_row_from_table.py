import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def delete_task(conn,id):
    """
    Delete a task by task id
    :param conn: Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE  id = ?'
    cur = conn.cursor()
    cur.execute(sql,(id,))

def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)

def main():
    database = "C:\\swlite\db\pythonsqlite.db"

    #create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn,2);

if __name__ == '__main__':
    main()
