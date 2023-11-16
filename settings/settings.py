import os
from dotenv import load_dotenv

load_dotenv()

API_GIF = os.getenv('API_GIF')
NASA_API = os.getenv('NASA_API')
TOKEN_BOT = os.getenv('TOKEN_BOT')

#PostgresSQL
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db_name = os.getenv('db_name')