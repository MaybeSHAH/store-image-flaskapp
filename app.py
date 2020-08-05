import os
import requests
import math
import re
import random
#import cv2
import qrcode
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash,check_password_hash
from helpers import login_required

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        # Get user info
        vname = request.form.get('vname')
        person = request.form.get('person')
        cname = request.form.get('cname')
        w_type = 'Visitor'
        
        # example data
        data = vname , person, cname, w_type 
        # output file name
        n = random.random()
        filename = "static/img/qrcode"+str(n)+".png"
        # generate qr code
        img = qrcode.make(data)
        
        # save img to a file
        img.save(filename)
        '''
        img = cv2.imread(filename)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
        #leader_obj = db.execute('SELECT ign FROM users WHERE username = :username', {'username': username1}).fetchone()
        '''
        if leader_obj:
            """Some text"""
        else:
            flash("Leader Not Registered", 'danger')
            return redirect(url_for('index'))'''
        #make sure validated username submits::
        
        '''
        # Store the user_id in session
        # user = db.execute('SELECT id from users WHERE username = :username', {'username': username}).fetchone()
        # user_id = user.id
        # session['user_id'] = user_id'''
            
        #db.execute("INSERT INTO \"Info\" (empname, empid, address) VALUES (:empname, :empid, :address)", {"empname": empname, "empid": empid, "address": address})
        #db.commit()

        #flash("Data created Successfully!", 'success')
        return render_template('result.html', filename=filename)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template('userreg.html')


@app.route("/signup", methods=['POST'])
def signup():
    """Register a user."""

    # User reached route via POST (as by submiting a form via POST)
    if request.method == "POST":

        # Get user info
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')
        if len(username) <= 3 or len(username) > 20:
            flash("Username Length Must be between 3 to 20")
            return redirect('/signup')
        elif len(password) < 6 or len(password) >12:
            flash("Password length must be between 6 to 12")
            return redirect('/signup')

        # Check if passwords match
        if password != re_password:
            flash("Passwords don't match!")
            return redirect('/signup')
        
        # Check if username is available
        if db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount == 0:
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username": username, "password": generate_password_hash(password)})
            db.commit()
            # Store the user_id in session
            # user = db.execute('SELECT id from users WHERE username = :username', {'username': username}).fetchone()
            # user_id = user.id
            # session['user_id'] = user_id
            flash("Registered!", 'success')
            return redirect(url_for('index'))
        else:
            return render_template('error.html', msg="Username already taken.")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template('signup.html')

@app.route("/userreg", methods=['POST'])
def userreg():

    # User reached route via POST (as by submiting a form via POST)
    if request.method == "POST":
        # Get user info
        empname = request.form.get('ename')
        empid = request.form.get('eid')
        address = request.form.get('address')
        #leader_obj = db.execute('SELECT ign FROM users WHERE username = :username', {'username': username1}).fetchone()
        '''
        if leader_obj:
            """Some text"""
        else:
            flash("Leader Not Registered", 'danger')
            return redirect(url_for('index'))'''
        #make sure validated username submits::
        
        '''
        # Store the user_id in session
        # user = db.execute('SELECT id from users WHERE username = :username', {'username': username}).fetchone()
        # user_id = user.id
        # session['user_id'] = user_id'''
            
        #db.execute("INSERT INTO \"Info\" (empname, empid, address) VALUES (:empname, :empid, :address)", {"empname": empname, "empid": empid, "address": address})
        #db.commit()

        #flash("Data created Successfully!", 'success')
        return redirect(url_for('index'))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template('userreg.html')



@app.route('/logout')
def logout():
    """ Logout user out """

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)