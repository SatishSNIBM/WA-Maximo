import sys
import json
import os, ibm_db, ibm_db_dbi as dbi, pandas as pd
import requests

def main(params):
    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        'bludb',
        'mas-masgsi-masgsi-manage-db2u.masgsilabs-240f75f72cdf82f997ffe11d34c5adcb-0000.us-east.containers.appdomain.cloud',
        '32686',
        uid='db2inst1',
        pwd='P2J56xZ8OUXXdXM'
    )

    db2_connection = dbi.connect(db2_dsn)
    query = 'SELECT * FROM "Maximo"."WORKORDER"'
    bus_df = pd.read_sql_query(query, con=db2_connection)

    response = {"result": "Success"}
    return response
