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

    bus_route = params['bus_route']
    bus_stop = params['bus_stop'].lower()
    response = {}

    query_df = bus_df[(bus_df.BUS_ROUTE == bus_route) & (bus_df.BUS_STOP == bus_stop)]

    if query_df.shape[0] <= 0:
        response = {"Error" : "There are no records available with this data"}
    else:
        bus_route = query_df.BUS_ROUTE.item()
        bus_stop = query_df.BUS_STOP.item()
        bus_time = query_df.SCHEDULED_ARRIVAL_TIME.item()
        return_string = "Bus " + str(bus_route) + " is scheduled to arrive at " + bus_stop + " at " + str(bus_time)
        response = {"bus_message": return_string}
    return response
