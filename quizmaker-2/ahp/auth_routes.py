from flask import Blueprint, render_template, request, flash, url_for, make_response
from flask import session as sssession
from werkzeug.security import generate_password_hash, check_password_hash
from random import choice
import string
sahlt = ''
boo = string.ascii_letters + string.digits + string.punctuation


auth = Blueprint('auth', __name__, template_folder='templates')
from . import *
from . import Session,get_data

@auth.route('/login', methods=["POST", "GET"])
def login():
  try:
    check = check_if_login(sssession['password'],sssession['name'])
  except:
    check = ''
    if check == 'success':
        return render_template('success.html', x=sssession['name'],b=True)
  if request.method == "POST":

        # use login in function from database with a post request of data
        a = str(request.form["email"])
        b = str(request.form["pswd"])
        x = loginn(a, b)
        if x[0] == 'h':
            flash('wrong password', 'danger')
            return render_template('login.html',b=False)
        elif x[0] == 'l':
            flash('user does not exist', 'danger')
            return render_template('login.html',b=False)
        else:
            sssession['password'] = x[1]
            sssession['name'] =  a
            g=get_data(sssession['name'])      
            print(f'g={g}')
            return render_template('success.html', x=a,b=True,ys=g[0],sou=g[1])

  return render_template('login.html', b = False)

@auth.route('/Logout', methods=["POST", "GET"])
def Logout():
  sssession.clear()
  return render_template('home.html',b=False)

@auth.route('/signin', methods=["POST", "GET"])
def signin():
  try:
    check = check_if_login(sssession['password'],sssession['name'])
  except:
    check = ''
  if check == 'success':
        return render_template('success.html', x=sssession['name'],b=True)
  if request.method == "POST":
        b = str(request.form["email"])
        c = str(request.form["pswd"])
        d = str(request.form["pswd2"])
        if 'gutzy' in b:
          flash('stop it chaim','danger')
          return render_template('signin.html',b=False)
        if len(c) < 6:
            flash('your password needs to be greater than 6 numbers', 'danger')
            return render_template('signin.html',b=False)
        if c != d:
            flash('your passwords do not match', 'danger')
            return render_template('signin.html',b=False)
        x = signup(b,c,d)
        if x == None:
            return render_template('signin.html',b=False)
        else:
            sssession['password'] = x
            sssession['name'] =b
            return render_template('success.html',x=sssession['name'])
  return render_template('signin.html',b = False)
