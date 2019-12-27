import pandas as pd
import logging
from database.manage import *

logging.basicConfig(level=logging.INFO)


tables_csv = {
    Circuit: r'csv\circuits.csv',
    Result: r'csv\results.csv',
    Race: r'csv\races.csv',
    Driver: r'csv\drivers.csv',
    DriverStanding: r'csv\driver_standings.csv',
    Qualifying: r'csv\qualifying.csv',
    # 'results': r'C:\Users\naked\Downloads\f1db_csv\constructor_results.csv',
    # 'driver_standings': r'C:\Users\naked\Downloads\f1db_csv\results.csv',
    # 'lap_times': r'C:\Users\naked\Downloads\f1db_csv\results.csv',
    # 'qualifying': r'C:\Users\naked\Downloads\f1db_csv\results.csv',
    # 'bobobob': r'C:\Users\naked\Downloads\f1db_csv\circuits.csv',
}

for table, csv in tables_csv.items():
    # try:
    logging.debug('Removing data from table {}'.format(table.__table__.name))
    table.query.delete()
    db.session.commit()

    logging.debug('Uploading data to table {}'.format(table.__table__.name))
    df = pd.read_csv(csv, header=0, index_col=None, na_values=r'\N')
    df.columns = table.__table__.columns.keys()
    df.to_sql(table.__table__.name, db.engine, if_exists='replace', index=False, chunksize=50)

    logging.info('Completed upload for table {}'.format(table.__table__.name))
    # except Exception:
    #     print(1)
