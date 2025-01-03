import math
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Integer, String, insert, select
engine = create_engine("sqlite+pysqlite:///GPSdata1.db", echo=False)
metadata_obj = MetaData()

players_table = Table("players", metadata_obj, autoload_with=engine)
sessions_data_table = Table("sessions_data", metadata_obj, autoload_with=engine)

# simply returns an int representing y:m:d
def dateHash(date: str):
    day = date.day
    month = date.month
    year = date.year

    hash_value = year * 10e3 + month * 10e1 + day

    return int(hash_value)

def stringHash(string: str):
    p = 31
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for char in string:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m

    return int(hash_value)

# returns a hash of a session using the player_id, session_title and session_date
def dateStringHash(date: str, title:str, player_id: int):
    hashed_date = dateHash(date)
    hashed_title = stringHash(title)

    title_mag = int(math.floor(math.log(hashed_title, 10)))
    date_mag = int(math.floor(math.log(hashed_date, 10)))

    return (player_id * 10 ** (date_mag + date_mag + 3)) + (hashed_date * 10 ** (title_mag + 1)) + hashed_title

def getMatchID(date: str, title:str, sessions:list):
    
    for session in sessions:
        session_date = session["session_date"]
        session_title = session["session_title"]

        if session_date == date and session_title == title:
            return session["match_id"]


def getPlayerIds(lookup: str, table: str, database: str):

    with engine.connect() as conn:

        ids = (
            select(players_table.c.id)
            .where(players_table.c.position == {position})
            .subquery()
        )

    return ids