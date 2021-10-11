from peewee import *

db = SqliteDatabase("cointosses.db")


def prep_db():

    raw_models = []
    models = []

    with open("models.py", "r") as f:
        for line in f:
            if line.startswith("class"):
                raw_models.append(line)

    for item in raw_models:
        fitem = item.replace("class ", " ").replace("(Model):", "").replace("(BaseModel):", "").strip()
        models.append(fitem)

    models.remove("BaseModel")

    with db:
        #models = ["ResultSet", "CoinToss"]
        tables = db.get_tables()

        for model in models:
            if not model.lower() in tables:
                db.create_tables(model)
            else:
                print(f"Model {model} exists in database already.")

        # db.create_tables([ResultSet, CoinToss])


if __name__ == "__main__":
    prep_db()