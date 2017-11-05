#color of text\/; track total gold\/;casino/cave\/, time, pass to root route\/
from flask import Flask, render_template, request, redirect,session, flash
import random
import re
import datetime
app = Flask(__name__)
app.secret_key='poshit0'
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
    try:
        session['gold']
    except:
        session['gold']=0
    logger=zip(session['log'],session['clr'])
    return render_template('index.html',logger=logger)#zip(session['log'],session['color']))
@app.route('/process_money',methods=['POST'])
def process():
    if request.form['building']=='farm':
        gain=random.randrange(10,20)
        session['gold']+=gain
        session['clr'].append('green')
        session['log'].append('Earned {} golds from the {}! ({} )'.format(gain,request.form['building'],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        session.modified = True
    if request.form['building']=='cave':
        gain=random.randrange(5,10)
        session['gold']+=gain
        session['clr'].append('green')
        session['log'].append('Earned {} golds from the {}! ({} )'.format(gain,request.form['building'],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        session.modified = True
    if request.form['building']=='casino':
        gain=random.randrange(-50,50)
        session['gold']+=gain
        if gain <0 :
            color='red'
        else:
            color='green'
        session['clr'].append(color)
        session['log'].append('Earned {} golds from the {}! ({} )'.format(gain,request.form['building'],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        session.modified = True
        # var=type(session['log'])
    return redirect('/')#,test=len(session['log']),var=var)
app.run(debug=True)