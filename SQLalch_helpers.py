import math
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Integer, String, insert, select, Subquery
engine = create_engine("sqlite+pysqlite:///GPSdata1.db", echo=False)

metadata_obj = MetaData()

players_table = Table("players", metadata_obj, autoload_with=engine)
sessions_data_table = Table("sessions_data", metadata_obj, autoload_with=engine)


def withEngine(func):
    def inner(*args, **kwargs):
        with engine.connect() as conn:
            to_execute = func(*args, **kwargs)
            result = conn.execute(to_execute)
            return result.mappings().all()
        
    return inner
    

def selectPlayerIDsSubQ(position: str, table: Table[players_table]):
    player_sbq = (
            select(table)
            .where(table.c.position == position)    
            .subquery()    
        )

    return player_sbq

@withEngine
def selectSessionsDataScatter(position_subQ: Subquery , 
                              columns: list, 
                              
                              table: Table[sessions_data_table]):
    
    session_data_for_scatter = (
        select(columns)
        .where(table.c.player_id == position_subQ.c.id)
    )
     
    return session_data_for_scatter

    
@withEngine
def selectSessionsDataScatter(position_subQ: Subquery , 
                              column, 
                              
                              table: Table[sessions_data_table]):
    
    session_data_for_scatter = (
        select(column)
        .where(table.c.player_id == position_subQ.c.id)
    )
     
    return session_data_for_scatter


