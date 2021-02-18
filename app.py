import os
import requests
import math
import re
import random
import jsonpickle
import numpy as np
import cv2
from flask import Flask, request, Response
from datetime import datetime, date
import pytz
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

os.environ["DATABASE_URL" ] = "postgres://lqdwcanfmizgnc:bae307e8297fb669e4d3e02be1a59e7d886b7c7eaa6a12b577340f5f6a0294ea@ec2-50-16-198-4.compute-1.amazonaws.com:5432/dabop3r1q3qe44";

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.environ["DATABASE_URL"])
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        r = request
        # convert string of image data to uint8
        nparr = np.fromstring(r.data, np.uint8)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        n = random.random()
        filepath = "static/pics/user"+str(n)+".png"
        # do some fancy processing here....
        #saving file cv2.imwrite(path,img_to_save)
        cv2.imwrite(filepath,img)
        # build a response dict to send back to client
        filename = {'name': filepath }
        response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
        # encode response using jsonpickle
        response_pickled = jsonpickle.encode(filename)

        return Response(response=response_pickled, status=200, mimetype="application/json")
        # User reached route via GET (as by clicking a link or via redirect)
    else:
        '''var_url = 'static/img/qrcode0.27349510842284597.png'
        var_date = date.today();
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        var_time = now.strftime("%H:%M:%S")
        var_fm = var_hs = var_us = var_fogg = var_temp = var_name = var_phone = var_pm = var_cold = var_fever = var_cough = 1;
        '''
        #leader_obj = db.execute('INSERT INTO records ( r_url, r_date , r_time , r_faceMask , r_handSanitized, r_uvSanitized, r_fogging, r_temperature, r_name, r_phone, r_personToMeet, r_cold, r_fever, r_cough) VALUES (:url, CAST(:date as DATE), CAST(:time as TIME), :fm, :hs, :us, :fogg, :temp, :name, :phone, :pm, :cold, :fever, :cough)', {'url': var_url, 'date': var_date, 'time': var_time, 'fm': var_fm, 'hs': var_hs, 'us': var_us, 'fogg': var_fogg, 'temp': var_temp,
         #   'name': var_name, 'phone': var_phone, 'pm': var_pm, 'cold': var_cold, 'fever': var_fever, 'cough': var_cough}).fetchone()
        
        #INSERT INTO info ( url, date , time ,faceMask ,handSanitized,uvSanitized,fogging,temprature,name,phone,personToMeet,cold,fever,cough) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        records = db.execute('SELECT * FROM records').fetchall()
        print (records)
        return render_template('table.html', records=records)
        




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)