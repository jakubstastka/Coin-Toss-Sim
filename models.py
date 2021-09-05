import datetime

from peewee import *

db = SqliteDatabase("cointosses.db")


class TossSet(Model):
    tossed = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Toss(Model):
    set = ForeignKeyField(TossSet, backref="tosses")
    heads = BooleanField()
    tails = BooleanField()

    class Meta:
        database = db
