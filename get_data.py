from helpers.postgres_class import PostgresPipeline
from sql_queries import *


db = PostgresPipeline()
db.create_conn()
db.load_data(gold_price_l14d_query, 'data/staging_data.csv')
db.close_conn()
