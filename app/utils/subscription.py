from . import lib_db


def add(user, book_id):
    lib_db.execute("INSERT INTO subscriptions (user, subscription) VALUES (?, ?)", (user, book_id))


def del_subs(user, book_id):
    lib_db.execute("UPDATE subscriptions SET is_del = 1 WHERE subscription =? AND user=?", (book_id, user))
