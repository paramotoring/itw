from flask import render_template
from flask import Flask
app = Flask(__name__)
from datetime import datetime
from random import randint
from flask import request

working = False

def is_terry_working_default():
    day = datetime.today()
    firstday = datetime(2016,12,9,00,00,00)
    firstkellyday = datetime(2016,11,24,00,00,00)
    totaldays = (day - firstday).days % 3
    kellyday = (day - firstkellyday).days % 27
    global working

    if (kellyday == 0):
        working = False
        return "It's a Kellye Day! Terry is off!"
    elif (totaldays % 3 == 0):
        working = True
        return "Terry is working today :("
    else:
        working = False
        return "Terry is off today!"

def is_terry_working_input():
    user_input = request.form['date_selected']
    if not user_input:
        return is_terry_working_default()

    u = [int(x) for x in user_input.split('/')]
    day = datetime(u[2],u[0],u[1],00,00,00)
    firstday = datetime(2016,12,9,00,00,00)
    firstkellyday = datetime(2016,11,24,00,00,00)
    totaldays = (day - firstday).days % 3
    kellyday = (day - firstkellyday).days % 27
    global working
    if (kellyday == 0):
        working = False
        return "{} is a Kellye Day! Terry is off!".format(user_input)
    elif (totaldays % 3 == 0):
        working = True
        return "Terry is working on {} ".format(user_input)
    else:
        working = False
        return "Terry is off on {}!".format(user_input)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        response = is_terry_working_input()
        return render_template('index.html',
                              working=working,
                              response=response)
    else:
        response = is_terry_working_default()
        return render_template('index.html',
			      working=working,
                              response=response)

