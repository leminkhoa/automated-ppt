import psycopg2
import pandas as pd
import os

class PostgresPipeline:
    def __init__(self):
        self.db_user        = os.environ.get('RDS_USER' ,'') 
        self.db_password    = os.environ.get('RDS_PASSWORD', '')
        self.db_host        = os.environ.get('RDS_HOSTNAME', '')
        self.db_name        = 'postgres'
        self.db_schema      = 'dev'
        self.db_table       = 'get_gold_2022'
        self.port           = 5432

    def create_conn(self):
        self.client = psycopg2.connect(
                            user=self.db_user,
                            password = self.db_password,
                            host = self.db_host,
                            database = self.db_name,
                            port = self.port)
        self.curr = self.client.cursor()  
        print("Successfully connected to database!")
        
    
    def close_conn(self):
        self.client.close()
        print("Successfully closed connection to database!")
        
    
    def load_data(self, query, path):
        fmt_query = query.format(db_schema=self.db_schema, db_table=self.db_table)  
        df = pd.read_sql(fmt_query, self.client)
        df.to_csv(path, index=False)
        