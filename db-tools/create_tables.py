from peewee import *

db = SqliteDatabase("cointosses.db")


def create_tables():
    with db:
        models = ["ResultSet", "CoinToss"]
        tables = db.get_tables()

        for model in models:
            if not model.lower() in tables:
                db.create_tables(model)
            else:
                print(f"Model {model} exists in database already.")

        # db.create_tables([ResultSet, CoinToss])


if __name__ == "__main__":
    create_tables()