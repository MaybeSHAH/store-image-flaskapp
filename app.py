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




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)