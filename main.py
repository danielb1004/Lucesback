import unittest
import time
import asyncio

from flask import request, make_response, redirect, render_template, session, url_for, flash, jsonify


from flask_login import login_required, current_user

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app.db import db

app = create_app()

db.init_app(app)



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response



scenery = {
    '1': '0',
    '2': '0',
    '3': '0',
    '4': '0',
    '5': '0',
    '6': '0',
    '7': '0',
    '8': '0',
    '9': '0',
    '10': '0',
    '11': '0',
    '12': '0'
}

@app.route('/place/<place_id>', methods=['GET', 'POST'])
def place(place_id):
    response = jsonify({'R': scenery[place_id]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/control', methods=['GET', 'POST'])
def control():
    context = {
        'scenery': scenery
    }
    return render_template('index.html', **context)


#En esta ruta se recibe el formulario de control
@app.route('/control_path', methods=['POST'])
def control_path():
    if request.method == 'POST':
        strobo = '' if request.form.get('strobo') is None else request.form.get('strobo')
        festive = '' if request.form.get('festive') is None else request.form.get('festive')
        ola = '' if request.form.get('ola') is None else request.form.get('ola')
        lado = '' if request.form.get('lado') is None else request.form.get('lado')
        move = '' if request.form.get('move') is None else request.form.get('move')
        color = '' if request.form.get('blanco') is None else request.form.get('blanco')
        uno = '' if request.form.get('1') is None else request.form.get('1')
        dos = '' if request.form.get('2') is None else request.form.get('2')
        tres = '' if request.form.get('3') is None else request.form.get('3')
        cuatro = '' if request.form.get('4') is None else request.form.get('4')
        cinco = '' if request.form.get('5') is None else request.form.get('5')
        seis = '' if request.form.get('6') is None else request.form.get('6')
        siete = '' if request.form.get('7') is None else request.form.get('7')
        ocho = '' if request.form.get('8') is None else request.form.get('8')
        nueve = '' if request.form.get('9') is None else request.form.get('9')
        diez = '' if request.form.get('10') is None else request.form.get('10')
        once = '' if request.form.get('11') is None else request.form.get('11')
        doce = '' if request.form.get('12') is None else request.form.get('12')
        favcolor = '' if request.form.get('favcolor') is None else request.form.get('favcolor')
        if ola == 'on':
            range_input = 10
            olaf(range_input)
        if lado == 'on':
            range_input = 10
            asyncio.run(ladof(range_input))

        if strobo == 'on':
            if uno == 'on':
                scenery['1'] = 'strobo'
            if dos == 'on':
                scenery['2'] = 'strobo'
            if tres == 'on':
                scenery['3'] = 'strobo'
            if cuatro == 'on':
                scenery['4'] = 'strobo'
            if cinco == 'on':
                scenery['5'] = 'strobo'
            if seis == 'on':
                scenery['6'] = 'strobo'
            if siete == 'on':
                scenery['7'] = 'strobo'
            if ocho == 'on':
                scenery['8'] = 'strobo'
            if nueve == 'on':
                scenery['9'] = 'strobo'
            if diez == 'on':
                scenery['10'] = 'strobo'
            if once == 'on':
                scenery['11'] = 'strobo'
            if doce == 'on':
                scenery['12'] = 'strobo'
        
        if festive == 'on':
            if uno == 'on':
                scenery['1'] = 'festive'
            if dos == 'on':
                scenery['2'] = 'festive'
            if tres == 'on':
                scenery['3'] = 'festive'
            if cuatro == 'on':
                scenery['4'] = 'festive'
            if cinco == 'on':
                scenery['5'] = 'festive'
            if seis == 'on':
                scenery['6'] = 'festive'
            if siete == 'on':
                scenery['7'] = 'festive'
            if ocho == 'on':
                scenery['8'] = 'festive'
            if nueve == 'on':
                scenery['9'] = 'festive'
            if diez == 'on':
                scenery['10'] = 'festive'
            if once == 'on':
                scenery['11'] = 'festive'
            if doce == 'on':
                scenery['12'] = 'festive'
        
        if color == 'on':
            if uno == 'on':
                scenery['1'] = favcolor
            if dos == 'on':
                scenery['2'] = favcolor
            if tres == 'on':
                scenery['3'] = favcolor
            if cuatro == 'on':
                scenery['4'] = favcolor
            if cinco == 'on':
                scenery['5'] = favcolor
            if seis == 'on':
                scenery['6'] = favcolor
            if siete == 'on':
                scenery['7'] = favcolor
            if ocho == 'on':
                scenery['8'] = favcolor
            if nueve == 'on':
                scenery['9'] = favcolor
            if diez == 'on':
                scenery['10'] = favcolor
            if once == 'on':
                scenery['11'] = favcolor
            if doce == 'on':
                scenery['12'] = favcolor

        print(scenery)
            
    return redirect(url_for('control'))


def olaf(range_input):
    for i in range(0, range_input):
        scenery['5'] = 'black'
        scenery['7'] = 'black'
        scenery['1'] = 'white'
        scenery['3'] = 'white'
        scenery['9'] = 'white'
        scenery['11'] = 'white'
        scenery['6'] = 'black'
        scenery['8'] = 'black'
        scenery['10'] = 'black'
        scenery['12'] = 'black'
        time.sleep(0.5)
        scenery['2'] = 'white'
        scenery['4'] = 'white'
        scenery['9'] = 'white'
        scenery['11'] = 'black'
        time.sleep(0.5)
        scenery['5'] = 'white'
        scenery['7'] = 'white'
        scenery['10'] = 'white'
        scenery['1'] = 'black'
        scenery['3'] = 'black'
        scenery['9'] = 'black'
        scenery['2'] = 'black'
        scenery['4'] = 'black'
        time.sleep(0.5)
        scenery['6'] = 'white'
        scenery['8'] = 'white'
        scenery['10'] = 'white'
        scenery['12'] = 'white'
        scenery['9'] = 'black'
        time.sleep(0.5)
        scenery['5'] = 'black'
        scenery['7'] = 'black'
        scenery['1'] = 'black'
        scenery['3'] = 'black'
        scenery['9'] = 'black'
        scenery['11'] = 'black'
        scenery['6'] = 'black'
        scenery['8'] = 'black'
        scenery['10'] = 'black'
        scenery['12'] = 'black'
        time.sleep(0.5)
    
async def ladof(range_input):
    for i in range(0, range_input):
        scenery['5'] = 'black'
        scenery['7'] = 'black'
        scenery['10'] = 'black'
        scenery['12'] = 'black'
        scenery['6'] = 'black'
        scenery['8'] = 'black'
        scenery['1'] = 'white'
        scenery['3'] = 'white'
        scenery['9'] = 'white'
        scenery['11'] = 'white'
        scenery['2'] = 'white'
        scenery['4'] = 'white'
        time.sleep(0.8)
        scenery['5'] = 'white'
        scenery['7'] = 'white'
        scenery['10'] = 'white'
        scenery['12'] = 'white'
        scenery['6'] = 'white'
        scenery['8'] = 'white'
        scenery['1'] = 'black'
        scenery['3'] = 'black'
        scenery['9'] = 'black'
        scenery['11'] = 'black'
        scenery['2'] = 'black'
        scenery['4'] = 'black'
        time.sleep(0.8)
        scenery['5'] = 'black'
        scenery['7'] = 'black'
        scenery['10'] = 'black'
        scenery['12'] = 'black'
        scenery['6'] = 'black'
        scenery['8'] = 'black'
        scenery['1'] = 'white'
        scenery['3'] = 'white'
        scenery['9'] = 'white'
        scenery['11'] = 'white'
        scenery['2'] = 'white'
        scenery['4'] = 'white'
        time.sleep(0.8)
        scenery['5'] = 'white'
        scenery['7'] = 'white'
        scenery['10'] = 'white'
        scenery['12'] = 'white'
        scenery['6'] = 'white'
        scenery['8'] = 'white'
        scenery['1'] = 'black'
        scenery['3'] = 'black'
        scenery['9'] = 'black'
        scenery['11'] = 'black'
        scenery['2'] = 'black'
        scenery['4'] = 'black'
        time.sleep(0.8)
        scenery['5'] = 'black'
        scenery['7'] = 'black'
        scenery['10'] = 'black'
        scenery['12'] = 'black'
        scenery['6'] = 'black'
        scenery['8'] = 'black'
        scenery['1'] = 'white'
        scenery['3'] = 'white'
        scenery['9'] = 'white'
        scenery['11'] = 'white'
        scenery['2'] = 'white'
        scenery['4'] = 'white'
        time.sleep(0.8)
        scenery['5'] = 'white'
        scenery['7'] = 'white'
        scenery['10'] = 'white'
        scenery['12'] = 'white'
        scenery['6'] = 'white'
        scenery['8'] = 'white'
        scenery['1'] = 'black'
        scenery['3'] = 'black'
        scenery['9'] = 'black'
        scenery['11'] = 'black'
        scenery['2'] = 'black'
        scenery['4'] = 'black'
        time.sleep(0.8)
        
        