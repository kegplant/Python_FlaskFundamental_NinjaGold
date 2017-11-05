from flask import Flask, render_template, request, redirect,session, flash
import random
import re
import datetime
app = Flask(__name__)
app.secret_key='poshit'
# our index route will handle rendering our form
@app.route('/')
def index():
    try:
        session['log']
    except:
        session['log']=['']
    try:
        session['clr']
    except:
        session['clr']=['green']
    return render_template('index.html')#zip(session['log'],session['color']))
@app.route('/process_money',methods=['POST'])
def process():
    if request.form['building']=='farm':
        gain=random.randrange(10,20)
        # session['clr'].append('green')
        session['log']=session['log']+['Earned {} golds from the {}! ({} )'.format(gain,request.form['building'],str(datetime.date.today()))]
        # var=type(session['log'])
    return render_template('index.html')#,test=len(session['log']),var=var)



app.run(debug=True)