import pymysql.cursors
import pygame

db = pymysql.connect(host='178.62.226.124',
                             user='infprj2',
                             password='banaan',
                             db='groep6')

def init():
    pass

def execute_query(sql):
    cur = db.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    db.commit()
    return cur.fetchall()


def quit():
    db.close()




def update(name, score):

    scores = execute_query("SELECT * from scores WHERE name='{}'".format(name))
    updateScore = True

    if not len(scores):
        execute_query("INSERT INTO scores (name,score,wins,loses) VALUES ('{}','0','0','0')".format(name, 0, 0, 0))

   
    for x in scores:
        if x["score"] > score:
            updateScore = False

    if updateScore:
        execute_query("UPDATE scores SET score='{}' WHERE name='{}'".format(score, name))


def get_value(col, name):
    scores = execute_query("SELECT * FROM scores WHERE name='{}'".format(name))

    for x in scores:
        return int(x[col])

    return 0


def increment_wins(name):
    wins = get_value("wins", name) + 1
    execute_query("UPDATE scores SET wins='{}' WHERE name='{}'".format(wins, name))


def increment_loses(name):
    loses = get_value("loses", name) + 1
    execute_query("UPDATE scores SET loses='{}' WHERE name='{}'".format(loses, name))
