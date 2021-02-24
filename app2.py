import io
import os
import json                    
import base64                  
import logging   
import random   
import cv2       
import numpy as np
from PIL import Image
from flask import Flask, request, Response, jsonify, abort
from datetime import datetime, date
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)          
#app.logger.setLevel(logging.DEBUG)

os.environ["DATABASE_URL" ] = "postgres://lqdwcanfmizgnc:bae307e8297fb669e4d3e02be1a59e7d886b7c7eaa6a12b577340f5f6a0294ea@ec2-50-16-198-4.compute-1.amazonaws.com:5432/dabop3r1q3qe44";
UPLOAD_FOLDER = './static/img/'
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Session(app)

# Set up database
engine = create_engine(os.environ["DATABASE_URL"])
db = scoped_session(sessionmaker(bind=engine))
 
  
@app.route("/", methods=["GET", "POST"])
def index():  
    if request.method == "POST":       
        # print(request.json)      
        if not request.json or 'image' not in request.json: 
            abort(400)
             
        # get the base64 encoded string
        im_b64 = request.json['image']

        # convert it into bytes  
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))

        # convert bytes data to PIL Image object
        #img=np.array(np.rot90(img_bytes,-1))
        img = Image.open(io.BytesIO(img_bytes))
        #pil_image = PIL.Image.open('image.jpg')
        opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        n = random.random()
        filename = "user"+str(n)+".png"
        filepath = './static/img/user'+str(n)+'.png'
        # do some fancy processing here....
        #saving file cv2.imwrite(path,img_to_save)
        #cv2.imwrite(filepath,img)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #img = img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #img.save(os.path.join(app.root_path, '/static/img/', filename), 'png')
        cv2.imwrite(os.path.join('/static/img/', filename), opencvImage)
        #img = img.save(filepath)
        # PIL image object to numpy array
        img_arr = np.asarray(img)
        print('img shape', img_arr.shape)

        # process your img_arr here    
    
        # access other keys of json
        # print(request.json['other_key'])

        result_dict = {'output': os.path.join('/static/img/', filename)}
        return result_dict
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
  
def run_server_api():
    app.run(host='0.0.0.0', port=5000)
  
  
if __name__ == "__main__":     
    run_server_api()