
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

def create_data_Log(conn, data_Log):
    """
    Create a new project into the projects table
    :param conn:
    :param:data_Log
    :return: project id
    """
    try:
        sql = ''' INSERT INTO DHT_Data(humidity,temp_in_C,temp_in_F,heatIndex_in_C,heatIndex_in_F)
                  VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql,data_Log)
        
    except Error as e:
        print(e)
    return None



def main():
    database = "forecast.db"
    #create a database connection
    conn = create_connection(database)
    with conn:
        #create a new data log
        data_Log = ('58','20','30','75','66')

if __name__ =='__main__':
    main()
