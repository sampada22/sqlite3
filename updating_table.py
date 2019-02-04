import sqlite3
from sqlite3 import Error

def update_task(conn,task):
    """
    update priority, begin_date,end_date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = '''UPDATE tasks
             SET priority = ?,
                 begin_date = ?,
                 end_date = ?
             WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql,task)

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

def main():
    database = "C:\\sqlite\db\pythonsqlite.db"

    #create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn,(2,'2015-01-04','2015-01-06',2))

if __name__ == '__main__':
    main()
