from __future__ import print_function
import requests
import os
import json
import cv2

#from datetime import datetime, date
#import pytz

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
addr = 'http://localhost:5000'
test_url = addr + '/'
os.environ["DATABASE_URL" ] = "postgres://lqdwcanfmizgnc:bae307e8297fb669e4d3e02be1a59e7d886b7c7eaa6a12b577340f5f6a0294ea@ec2-50-16-198-4.compute-1.amazonaws.com:5432/dabop3r1q3qe44";

# Set up database
engine = create_engine(os.environ["DATABASE_URL"])
db = scoped_session(sessionmaker(bind=engine))

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}
#send image from here
img = cv2.imread('static/img/qrcode0.27349510842284597.png')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))
#take this name as url for storing in db
# expected output: {'name': 'static/pics/user0.7558292794583046.png'}
url_name = json.loads(response.text)
print(url_name['name'])
'''date = date.today()
tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz)
var_time = now.strftime("%H:%M:%S")
print(date)
print(var_time)'''
db.execute('INSERT INTO records ( "r_url", "r_date" , "r_time" ,"r_faceMask" ,"r_handSanitized","r_uvSanitized", "r_fogging", "r_temperature", "r_name", "r_phone", "r_personToMeet", "r_cold", "r_fever", "r_cough") VALUES (:url, CAST(:date as DATE), CAST(:time as TIME), :fm, :hs, :us, :fogg, :temp, :name, :phone, :person, :cold, :fever, :cough)',{'url': url_name['name'], 'date': '20210218', 'time': '04:33:21', 'fm': True, 'hs': True, 'us': True, 'fogg': True, 'temp': True, 'name': 'shah', 'phone': 2345, 'person': 'sanjay', 'cold': True, 'fever': True, 'cough': True})

#db.execute(sql)
db.commit()
print("saved successfully")
        