from flask import Flask, render_template, request
import database_helper
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/update_inout', methods = ['POST', 'GET'])
def update():
    test = ""
    if(request.method == "POST"):
        test = request.form['product']
    return render_template('update_inout.html', data=test)

@app.route('/update_lager', methods = ['POST', 'GET'])
def update_lager():
    if(request.method == "POST"):
        addProduct = request.form['product']
        addCity = request.form['city']
        addAmount = request.form['amount']

        database_helper.updatelager(addProduct,addCity,addAmount)
    return render_template('update_lager.html')

@app.route('/home_page', methods = ['POST', 'GET'])
def home_page(): #sök på stad och se lagersaldo
    tempAll = ""
    checkCity = ""
    if(request.method == "POST"):
        checkCity = request.form['city']
        # kolla fall det finns
        tempAll = database_helper.getAmountInCityByCity(checkCity)
    return render_template('home_page.html', data=tempAll, city=checkCity)

@app.route('/new_product', methods = ['POST', 'GET'])
def new_product():
    return render_template('new_product.html')

@app.route('/new_lager', methods = ['POST', 'GET'])
def new_lager():
    deleteCity = ""
    createCity = ""
    createCityID = ""
    if(request.method == "POST"):
        #if(request.form.data['lagerToDelete'] != ""):
        #    deleteCity = request.form['lagerToDelete']
        #    database_helper.deleteCity(deleteCity)

        #if(request.form.data['lager'] != 'null'):
            createCity = request.form['lager']
            createCityID = request.form['lagerID']
            database_helper.createLager(createCity, createCityID)

    return render_template('new_lager.html')
