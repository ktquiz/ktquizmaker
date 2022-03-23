from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
import ahp
import json
from flask import session as sssession

key = "6661828b5f94e4bldkjsfajfeiebae79788c477ae6b74f70zzxcxcxcvzxcf182afe054f9c5ba26dbdb36"
from ahp.auth_routes import check_if_login
from ahp import app as app
@app.route('/', methods=["POST", "GET"])
def home():
    try:
        check = check_if_login(sssession['password'], sssession['name'])
        print(check)
        if check == 'success':
            return render_template('success.html', x=sssession['name'], b=True)
        return render_template('home.html', b=False)

    except:
        return render_template('home.html', b=False)


app.config['SECRET_KEY'] = key

app.run(host'0.0.0.0', port=55454)
