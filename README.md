
# Build A Cloud Data Warehouse using AWS Redshift

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


## How to run the project
1 - Fill in the information for the *dwh.cfg* configuration folder and save it in the project root folder.
```
[CLUSTER]
HOST= 
DB_NAME= dwh
DB_USER= dwhuser
DB_PASSWORD=
DB_PORT=5439
DB_ZONE = 'us-west-2'

[IAM_ROLE]
ARN= 

[S3]
LOG_DATA= 's3://udacity-dend/log_data'
LOG_JSONPATH= 's3://udacity-dend/log_json_path.json'
SONG_DATA= 's3://udacity-dend/song_data'

[AWS]
KEY= 
SECRET= 
REGION_NAME= us-west-2

[DWH] 
DWH_CLUSTER_TYPE=multi-node
DWH_NUM_NODES=2
DWH_NODE_TYPE=dc2.large
DWH_IAM_ROLE_NAME=dwhRole
DWH_CLUSTER_IDENTIFIER=dwhCluster
DWH_DB=dwh
DWH_DB_USER=dwhuser
DWH_DB_PASSWORD= 
DWH_PORT=5439
DWH_ENDPOINT= 
```
2 - Install the following libraries
```
pip install pandas
pip install psycopg2
pip install boto3
pip install json
pip install configparser
pip install ipython-sql
```
3- Create your own cluster manually from AWS Redshift UI or run step 2 in create_test_cluster.ipynb notebook.

4- Delete the cluster if needed manually or from step 5 in create_test_cluster.ipynb notebook.

### Project structure 
- sql_queries.py  
    - Contains all the sql queries, and is imported to all the other files.

- create_tables.py
    - Connects to the cluster then drops all existing tables, and creates new tables then close the connection.
- etl.py
    -  Connects to the cluster then load the data from the S3 bucket to the staging tables then insert the data from the staging tables to the database tables.
- dwh.cfg
    - Contains the configurations and credentials needed for connecting and creating the Redshift cluster.

- create_test_cluster.ipynb
    - Programmaticaly creates an AWS Redshift cluster then runs create_tables.py, runs etl.py, tests the tables of the schema, then deletes the cluster.




### Database Schema 
Staging tables:
```
staging_events
    - artist VARCHAR,
    - auth VARCHAR,
    - firstName VARCHAR,
    - gender CHAR(1),
    - itemInSession INT,
    - lastName VARCHAR,
    - length FLOAT,
    - level VARCHAR,
    - location TEXT,
    - method VARCHAR,
    - page VARCHAR,
    - registration VARCHAR,
    - sessionId INT,
    - song VARCHAR,
    - status INT,
    - ts BIGINT,
    - userAgent TEXT,
    - userId INT

staging_songs
    - artist_id VARCHAR,
    - artist_latitude FLOAT,
    - artist_location TEXT,
    - artist_longitude FLOAT,
    - artist_name VARCHAR,
    - duration FLOAT,
    - num_songs INT,
    - song_id VARCHAR,
    - title VARCHAR,
    - year INT
```

Dimension tables:
```
users
    - user_id int SORTKEY PRIMARY KEY,
    - first_name varchar,
    - last_name varchar,
    - gender varchar,
    - level varchar
```
```
songs                       
    - song_id varchar SORTKEY PRIMARY KEY,
    - title varchar,
    - artist_id varchar ,
    - year int,
    - duration numeric
```
```
artists                       
    - artist_id varchar SORTKEY PRIMARY KEY,
    - name varchar,
    - location varchar,
    - latitude float,
    - longitude float
```
```
time                       
    - start_time TIMESTAMP  DISTKEY SORTKEY PRIMARY KEY
    - hour int,
    - day int,
    - week int,
    - month int,
    - year int,
    - weekday varchar
```
Fact table

```
songplays                       
    - songplay_id IDENTITY(0,1) PRIMARY KEY,
    - start_time TIMESTAMP SORTKEY DISTKEY,
    - user_id int,
    - level varchar,
    - song_id varchar ,
    - artist_id varchar,
    - session_id int,
    - location varchar,
    - user_agent varchar
```
