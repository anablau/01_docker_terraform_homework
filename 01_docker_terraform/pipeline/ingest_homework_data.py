import click
import pandas as pd
from sqlalchemy import create_engine

@click.command()
@click.option('--pg-user', default='root')
@click.option('--pg-pass', default='root')
@click.option('--pg-host', default='localhost')
@click.option('--pg-port', default=5432)
@click.option('--pg-db', default='ny_taxi')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db):
    # 1. Create Connection
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # --- PART A: INSERT PARQUET (Green Taxi Data) ---
    print("Reading Green Taxi Parquet...")
    df_taxi = pd.read_parquet('green_tripdata_2025-11.parquet')
    
    # Green Taxi uses lpep_pickup_datetime, not tpep!
    df_taxi.lpep_pickup_datetime = pd.to_datetime(df_taxi.lpep_pickup_datetime)
    df_taxi.lpep_dropoff_datetime = pd.to_datetime(df_taxi.lpep_dropoff_datetime)

    print("Inserting Taxi Data to 'green_tripdata_nov'...")
    # 'replace' creates the table for you
    df_taxi.to_sql(name='green_tripdata_nov', con=engine, if_exists='replace', index=False)

    # --- PART B: INSERT CSV (Zones Data) ---
    print("Reading Zones CSV...")
    df_zones = pd.read_csv('taxi_zone_lookup.csv')

    print("Inserting Zones Data to 'zones'...")
    df_zones.to_sql(name='zones', con=engine, if_exists='replace', index=False)

    print("All data inserted successfully into the same schema!")

if __name__ == '__main__':
    run()