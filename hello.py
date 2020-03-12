from flask import Flask, render_template, request
import database_helper
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/update_inout', methods = ['POST', 'GET'])
def update():
    addProduct = ""
    addCityTo = ""
    addCityFrom = ""
    addAmount = ""
    tempdata1 = ""
    tempdata2 = ""
    if(request.method == "POST"):
        addProduct = request.form['product']
        addCityTo = request.form['cityTo']
        addCityFrom = request.form['cityFrom']
        addAmount = request.form['amountout']
        currentamount2 = database_helper.getAmountInCityByCityAndProduct(addCityFrom, addProduct)
        # Får felmeddelande när stad inte finns!

        if(database_helper.getProductInCityByCity(addCityFrom) and currentamount2):
            currentamount = int(currentamount2[0])
            if(currentamount >= int(addAmount)):
                print(currentamount)
                database_helper.inoutlager(addProduct, addCityTo, addCityFrom, addAmount)
                tempdata1 = "Lyckades att skicka " + addProduct + " från " + addCityFrom + " till " + addCityTo
            else:
                tempdata1 = "Finns inte tillräckligt med varor i utlagret"
        else:
            tempdata1 = "Finns ingen vara med det namnet i utlagret"


    tempdata2 = database_helper.getDataInInOut(addProduct)

    return render_template('update_inout.html', data=tempdata1, data1 = tempdata2)

@app.route('/update_lager', methods = ['POST', 'GET'])
def update_lager():
    data2 = ""
    if(request.method == "POST"):
        addProduct = request.form['product']
        addCity = request.form['city']
        addAmount = request.form['amount']
        addID = database_helper.getIDbyCity(addCity)
        if(addID):
            data2 = database_helper.updatelager(addID[0], addProduct, addCity, addAmount)
        else:
            data2 = "Staden finns inte, lägg till den först!"
    return render_template('update_lager.html', data=data2)

@app.route('/home_page', methods = ['POST', 'GET'])
def home_page(): #sök på stad och se lagersaldo
    tempAmount = ""
    tempProduct = ""
    checkCity = ""
    jsonObject = ""
    tempID = ""
    if(request.method == "POST"):
        checkCity = request.form['city']
        tempAmount = database_helper.getAmountInCityByCity(checkCity)
        tempProduct = database_helper.getProductInCityByCity(checkCity)
        #jsonObject = json.dumps({'Amount' : tempAll, 'product' : tempProduct})
        tempID = database_helper.getIDbyCity(checkCity)

    return render_template('home_page.html', data=tempProduct,data2 = tempAmount, data3 = tempID, city=checkCity)

@app.route('/new_product', methods = ['POST', 'GET'])
def new_product():
    tempAmount = ""
    tempProduct = ""
    tempCity = ""
    tempProductID = ""
    tempPrice = ""
    tempdata1 = ""

    # Lägg till så man kan se alla produkter

    if(request.method == "POST"):
        tempProduct = request.form['product']
        tempProductID = request.form['productID']
        tempPrice = request.form['price']

        if(database_helper.checkProductInProducts(tempProduct)):
            tempdata1 = tempProduct + " finns redan inlagd!"
        else:
            database_helper.createProduct(tempProduct, tempProductID, tempPrice)
            tempdata1 = tempProduct + " lades till i systemet, för att lägga till i ett lager gå till uppdatera lagersaldo"

    return render_template('new_product.html', data = tempdata1, data1 = tempProduct)

@app.route('/new_lager', methods = ['POST', 'GET'])
def new_lager():
    deleteCity = ""
    createCity = ""
    createCityID = ""
    data1 = ""

    # Lägg till så man kan se alla lager

    if(request.method == "POST"):
        createCity = request.form['lager']
        createCityID = request.form['lagerID']
        #kolla om staden redan finns
        if(database_helper.getCityByID(createCityID)):
        # ID ska vara unikt
            data1 = "finns redan ett lager med detta id"
        else:
            database_helper.createLager(createCity, createCityID)
        #deleteCity = request.form['lagerToDelete']
        #    database_helper.deleteCity(deleteCity)
    return render_template('new_lager.html', data=data1)
