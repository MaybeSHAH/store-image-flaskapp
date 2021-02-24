import base64
import json    
import os                
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
api = 'http://localhost:5000/'
#api = 'http://208.109.9.105/'
image_file = './static/pics/user0.5584097163113495.png'
os.environ["DATABASE_URL" ] = "postgres://lqdwcanfmizgnc:bae307e8297fb669e4d3e02be1a59e7d886b7c7eaa6a12b577340f5f6a0294ea@ec2-50-16-198-4.compute-1.amazonaws.com:5432/dabop3r1q3qe44";

engine = create_engine(os.environ["DATABASE_URL"])
db = scoped_session(sessionmaker(bind=engine))
with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "other_key": "value"})
response = requests.post(api, data=payload, headers=headers)
try:
    #response = requests.get(url)
    print(type(response))
    print(response)
    data = response.json()     
    print(data['output'])  
    db.execute('INSERT INTO records ( "r_url", "r_date" , "r_time" ,"r_faceMask" ,"r_handSanitized","r_uvSanitized", "r_fogging", "r_temperature", "r_name", "r_phone", "r_personToMeet", "r_cold", "r_fever", "r_cough") VALUES (:url, CAST(:date as DATE), CAST(:time as TIME), :fm, :hs, :us, :fogg, :temp, :name, :phone, :person, :cold, :fever, :cough)',{'url': data['output'], 'date': '20210218', 'time': '04:33:21', 'fm': True, 'hs': True, 'us': True, 'fogg': True, 'temp': True, 'name': 'shah', 'phone': 9999999999, 'person': 'sanjay', 'cold': True, 'fever': True, 'cough': True})
    db.commit()
    print("saved successfully")       
except requests.exceptions.RequestException:
    print(response.text)

#url_name = json.loads(response.text)
#print(url_name['name'])
