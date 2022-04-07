import sys
sys.path.append(".")
from pprint import pprint
from database.connection import Connection

heroes_select = """
    SELECT * from heroes
"""

def select(query):
    conn = Connection()
    heroes = conn.db_interact(heroes_select)
    typeof = type(heroes)
    for hero in heroes:
        print(hero.get('name'))

select(conn)
