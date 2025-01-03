from database_dicts import sessions, sessions_data, players # data to be loaded into db
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Integer, String, insert

engine = create_engine("sqlite+pysqlite:///GPSdata1.db", echo=True)

metadata_obj = MetaData()

players_table = Table("players", metadata_obj, autoload_with=engine)


