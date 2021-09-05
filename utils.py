from peewee import *

from models import ResultSet, CoinToss

db = SqliteDatabase("cointosses.db")


def create_tables():
    with db:
        db.create_tables([ResultSet, CoinToss])
