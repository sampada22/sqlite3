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

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    try:
        sql = ''' INSERT INTO projects(name,begin_date)
                  VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, project)
        return cur.lastrowid
    except Error as e:
        print(e)
    return None

def create_task(conn,task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    try:
        sql = '''INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                 VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql,task)
        return cur.lastrowid
    except Error as e:
        print(e)
    return None

def main():
    database = "C:\\sqlite\db\pythonsqlite.db"
    #create a database connection
    conn = create_connection(database)
    with conn:
        #create a new project
        project = ('Cool App with SQLite and Python','2015-01-01')
        project_id = create_project(conn,project)

        #tasks
        task_1 = ('Analyze the requirements of the app',1,1,project_id,'2015-01-01','2015-01-02')
        task_2 = ('Confirm with user about the top requirements',1,1,project_id,'2015-01-02','2015-01-07')

        #create tasks
        create_task(conn,task_1)
        create_task(conn,task_2)

if __name__ =='__main__':
    main()
