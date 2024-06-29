import shelve

def put(key, value):
    with shelve.open('db') as db:
        db[key] = value

def get(key):
    with shelve.open('db') as db:
        return db[key]