import sqlite3


def init_db():
    db_con = sqlite3.connect("lib.db")
    cur = db_con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS `subscriptions` (
          `subid` INTEGER PRIMARY KEY AUTOINCREMENT ,
          `user` VARCHAR(64) NOT NULL DEFAULT '0',
          `subscription` VARCHAR(12) DEFAULT '0',
          `is_del` TINYINT(4) DEFAULT '0'
        )""")

    db_con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS `user` (
          `uid` INTEGER PRIMARY KEY AUTOINCREMENT ,
          `user` VARCHAR(64) NOT NULL DEFAULT '0',
          `email` VARCHAR(128) NOT NULL DEFAULT '0'
        )""")

    db_con.commit()
    cur.close()
    return db_con
