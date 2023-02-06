import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    '''
    Loads the data from the S3 bukect of udacity to the created staging tables at the Redshift cluster.

            Parameters:
                    cur (object): A cursor for the connection of the database
                    conn (object): The connection for the database

            Returns:
                    Void
    
    '''
    for query in copy_table_queries:
    
        cur.execute(query)
        conn.commit()
        
        

def insert_tables(cur, conn):
    '''
    Inserts the data from the staging tables to the dimension and fact tables at
    the Redshift cluster.

            Parameters:
                    cur (object): A cursor for the connection of the database
                    conn (object): The connection for the database

            Returns:
                    Void
    
    '''
    for query in insert_table_queries:
        
        cur.execute(query)
        conn.commit()
        


def main():
    '''
    Main function:
        connects to the database at the Redshift cluster, loads the data to the staging tables then insert the
        data to the dimension and fact tables.
            Parameters:
                    None

            Returns:
                    Void
    
    '''
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    print('Connecting to the database')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('Successfuly connected to the database')
    print('Loading staging_tables')
    load_staging_tables(cur, conn)
    print('Inserting to tables')
    insert_tables(cur, conn)
    print('Completed the loading and insertion of the data')

    conn.close()


if __name__ == "__main__":
    main()