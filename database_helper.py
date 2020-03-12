import sqlite3

conn = sqlite3.connect('database.db')
#c = conn.cursor()

def connect_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    return conn

def closeConnection():
    if(conn is not None):
        conn.close()

def query_db(query, args=()): # används vid insert
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

def updatelager(incityID, product, city, inamount):
    currentamount = getAmountInCityByCityAndProduct(city, product)
    data1 = ""
    if( currentamount == None ):
        if(checkProductInProducts(product)):
        #skapa produkt i lager
            query_db('insert into lagersaldo values (?, ?, ?, ?)', (incityID, product, city, inamount))
            data1 = "produkten lades till"
        else: #produkterna måste finnas inlagt i produktlagret
            data1 = "produkten kunde inte läggas till, är du säker på att den finns i databasen?"
    else:
        newamount = int(inamount) + int(currentamount[0])
        query_db('Update lagersaldo set amount = ? where cityID = ? and product = ?', (newamount, incityID, product))
        data1 = "produkterna lades till"
    return data1

def getAmountInCityByCity(city):
    return query_db_all('select amount from lagersaldo where city = ?', (city, ))

def getAmountInCityByCityAndProduct(city, product):
    return query_db_one('select amount from lagersaldo where city = ? and product = ?', (city, product ))

def getProductInCityByCity(city):
    return query_db_all('select product from lagersaldo where city = ?', (city, ))

def getIDbyCity(city):
    return query_db_one('select cityID from lagersaldo where city = ?', (city, ))

def getCityByID(cityID):
    return query_db_one('select city from lagersaldo where cityID = ?', (cityID, ))

def deleteCity(city):
    return query_db('delete from lagersaldo where city = ?', (city, ))

def createLager(city, cityID): #en liten fuling här
    return query_db('insert into lagersaldo values (?, ?, ?, ?)', (cityID, 'jPlatta', city, 0))

def createProduct(product, productID, price):
    return query_db('insert into products values (?, ?, ?)', (productID, product, price) )
    #return query_db('insert into lagersaldo values (?, ?, ?, ?)', (cityID, product, city, 0))

def checkProductInProducts(product):
    return query_db_one('select product from products where product = ?', (product, ))

def getDataInInOut(product):
    return query_db_all('select datePosted, product, cityTo, cityFrom, amount from inout where product = ?', (product, ))

def inoutlager(product, cityTo, cityOut, amount): #kolla mer på denna
    query_db('insert into inout (product, cityTo, cityFrom, amount) values (?, ?, ?, ?)', (product, cityTo, cityOut, amount))
    # skapa "kvitto" i inout, uppdatera vardera lagerstatus efter detta
    # om produkten finns i lagret den skickas till --> update lager
    cityIDto = getIDbyCity(cityTo)
    cityIDfrom = getIDbyCity(cityOut)
    amountout = -int(amount)
    updatelager(cityIDto[0], product, cityTo, amount)
    updatelager(cityIDfrom[0], product, cityOut, amountout)
    return True
    #return query_db_all('update lagersaldo values (?, ?, ?) where city = ?', (product, cityTo, cityOut, amount))
