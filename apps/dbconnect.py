import pandas as pd
import psycopg2


def getdblocation():
    db = psycopg2.connect(
        host="localhost",
        database="172casedb_230",
        user="postgres",
        post=5432,
        password="password",
    )

    return db


def modifydatabase(sql, values):
    db = getdblocation()
    cursor = db.cursor()
    cursor.execute(sql, values)
    db.commit()
    db.close()


def querydatafromdatabase(sql, values, dfcolumns):
    db = getdblocation()
    cur = db.cursor()
    cur.execute(sql, values)
    rows = pd.DataFrame(cur.fetchall(), columns=dfcolumns)
    db.close()
    return rows
