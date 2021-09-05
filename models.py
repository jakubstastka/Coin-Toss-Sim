import datetime

from peewee import *

db = SqliteDatabase("cointosses.db")


class BaseModel(Model):
    class Meta:
        database = db


class ResultSet(BaseModel):
    created = DateTimeField(default=datetime.datetime.now)


class CoinToss(BaseModel):
    heads = BooleanField()
    tails = BooleanField()
    result_set = ForeignKeyField(ResultSet, backref="tosses")
