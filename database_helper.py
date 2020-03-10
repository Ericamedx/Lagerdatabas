import sqlite3

#conn = sqlite3.connect('database.db')
#c = conn.cursor()

def connect_db():
    return conn

def closeConnection():
    if(conn is not None):
        conn.close()

def query_db(query, args=()):
    #cursor = databaseConnection.cursor()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(query, args)
    conn.commit()
    c.close()
    return True

def query_db_one(query, args=()):
    databaseConnection = sqlite3.connect('database.db')
    cursor = databaseConnection.cursor()
    cursor.execute(query, args)
    result = cursor.fetchone()
    cursor.close()
    return result

def query_db_all(query, args=()):
    databaseConnection = sqlite3.connect('database.db')
    cursor = databaseConnection.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    return result

def inoutlager(product, cityTo, cityOut, amount): #kolla mer på denna
    return query_db_all('update lagersaldo values (?, ?, ?) where city = ?', (product, cityTo, cityFrom, amount))

def updatelager(product, city, amount):
    return query_db('insert into lagersaldo values (?, ?, ?)', (product, city, amount))

def getAmountInCityByCity(city):
    return query_db_all('select product, amount from lagersaldo where city = ?', (city, ))

def deleteCity(city):
    return query_db('delete from lagersaldo where city = ?', (city, ))

def createLager(city, cityID):
    return query_db_all('insert into cities values (?, ?)', (city, cityID))
