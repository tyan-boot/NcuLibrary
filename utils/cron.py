import utils.lib_db as lib_db


def run():
    db = lib_db.init_db()
    cur = db.cursor()

    data = cur.execute("""SELECT * FROM user LEFT JOIN subscriptions ON user.uid=subscriptions.userid;""")

    return data
