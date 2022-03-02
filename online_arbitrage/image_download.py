import requests
import csv
import sys
from datetime import datetime
import os

csv_path = sys.argv[1]
img_path = sys.argv[2]

dt_time = datetime.today().strftime('%Y-%m-%d')
os.mkdir(img_path + dt_time)

with open(csv_path,'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    
    for count, row in enumerate(reader):
        image_et = row[13]
        response_et = requests.get(image_et)
        file_et = open(img_path + dt_time + '\\' + str(count) +'_image_et.jpg', 'wb')
        file_et.write(response_et.content)
        file_et.close()
        
        
        image_cs = row[14]
        response_cs = requests.get(image_cs)
        file_cs = open(img_path + dt_time + '\\'+ str(count) +'_image_cs.jpg', 'wb')
        file_cs.write(response_cs.content)
        file_cs.close()