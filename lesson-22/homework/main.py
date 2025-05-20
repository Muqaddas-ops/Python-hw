import pandas as pd
from sqlalchemy import create_engine
import requests
import logging
import json
import pyodbc

with open('json//secret.json','r') as f:
    data = json.load(f)

 conn_str = f'mssql+pyodbc://{data['USERNAME']}:{data['PASSWORD']}@{data['SERVER']}/{data['DATABASE']}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(conn_atr)
print('Connected Successfully')

# print(data)