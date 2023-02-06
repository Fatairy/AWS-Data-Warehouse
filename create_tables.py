import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    '''
    Drops all existing tables at the Redshift cluster

            Parameters:
                    cur (object): A cursor for the connection of the database
                    conn (object): The connection for the database

            Returns:
                    Void
    
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
        


def create_tables(cur, conn):
    '''
    Creates all the tables at the Redshift cluster if the tables do not exists

            Parameters:
                    cur (object): A cursor for the connection of the database
                    conn (object): The connection for the database

            Returns:
                    Void
    
    '''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
        


def main():
    '''
    Main function:
        connects to the database at the Redshift cluster, Drops all existing tables then creates the staging, dimension, 
        and fact tables.
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
    print('Dropping tables if exists')
    drop_tables(cur, conn)
    print('Creating tables if not exists')
    create_tables(cur, conn)
    print('Completed the dropping and creation of the schema')

    conn.close()


if __name__ == "__main__":
    main()