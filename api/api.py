from flask import Flask, flash, render_template, jsonify, request, redirect, url_for, session, send_file
import os, io, sys
import numpy as np
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import xml.etree.ElementTree as ET
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from PIL import Image
import sqlite3
from datetime import datetime
import time
import cv2
import base64
import csv


app = Flask(__name__)
CORS(app)
#app.UseCors(b => b.AllowAnyHeader().AllowAnyMethod().AllowAnyOrigin().AllowCredentials().WithExposedHeaders("Content-Disposition"));

@app.route('/api', methods=['GET','POST'])
@cross_origin()
def api():
    target = ""
    fuc = ''
    img = ''
    npimg = ''
    objj = list()

    if 'image' in request.files:
        file = request.files['image'].read()
        npimg = np.fromstring(file, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img.astype("uint8"))
        print(img)
        img.save('aaya.jpg')
        rawBytes = io.BytesIO()
        img.save(rawBytes, "JPEG")



    if 'XMLFILE' in request.files:
        fuc = request.files['XMLFILE']
        tree = ET.parse(fuc)
        root = tree.getroot()
        image_name = root.find('filename').text
        con = sqlite3.connect('task2.db')
        objj = list()

        for item in root.findall('object'):
            val = list()
            val.append(image_name)
            names = item.find('name').text
            xmin = int(item.find('bndbox/xmin').text)
            ymin = int(item.find('bndbox/ymin').text)
            xmax = int(item.find('bndbox/xmax').text)
            ymax = int(item.find('bndbox/ymax').text)
            val.extend([names,xmin,ymin,xmax,ymax])
            cur = con.cursor()
            cur.execute('''CREATE TABLE if not exists file
                           (dateTime text, image text, object text, xmin integer, ymin integer, xmax integer, ymax integer)''')

            # Insert a row of data
            timee = datetime.now()
            cur.execute("INSERT INTO file VALUES (?,?,?,?,?,?,?)",(timee,image_name,names,xmin,ymin,xmax,ymax))

            # Save (commit) the changes
            con.commit()

            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.

            objj.append(val)
        con.close()
        print(objj)
        #pic = secure_filename(files.image)
        #xml = secure_filename(files.XMLFILE)
    else:
        print("bhaag")



    retimage = draw_faces('aaya.jpg',objj)
    strr = ""
    with open("p4.png", "rb") as imageFile:
        strr = base64.b64encode(imageFile.read())
    '''retimage = Image.fromarray(retimage.astype("uint8"))
    rawBytes = io.BytesIO()
    retimage.save(rawBytes, "PNG")
    rawBytes.seek(0)
    img_base64 = base64.b64.encode(rawBytes.read())'''
    print(strr)


    return_img = 'p4.png'#draw_faces(pic,xml)
    return jsonify({'status' : str(strr)})
    #response = jsonify({"pooja": "chu"})
    #response.headers.add("Access-Control-Allow-Origin", "*")
    #return response


@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


def parseXml(data):
    tree = ET.parse(data)
    root = tree.getroot()
    image_name = root.find('filename').text
    con = sqlite3.connect('task2.db')
    objj = list()

    for item in root.findall('object'):
        val = list()
        val.append(image_name)
        names = item.find('name').text
        xmin = int(item.find('bndbox/xmin').text)
        ymin = int(item.find('bndbox/ymin').text)
        xmax = int(item.find('bndbox/xmax').text)
        ymax = int(item.find('bndbox/ymax').text)
        val.extend([names,xmin,ymin,xmax,ymax])
        cur = con.cursor()
        cur.execute('''CREATE TABLE if not exists file
                       (dateTime text, image text, object text, xmin integer, ymin integer, xmax integer, ymax integer)''')

        # Insert a row of data
        timee = datetime.now()
        cur.execute("INSERT INTO file VALUES (?,?,?,?,?,?,?)",(timee,image_name,names,xmin,ymin,xmax,ymax))

        # Save (commit) the changes
        con.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.

        objj.append(val)
    con.close()
    print(objj)

    return objj

@app.route('/savetoCSV', methods=['GET','POST'])
def savetoCSV():
    starttt = request.get_json()
    sta = starttt['user']
    startdata = sta['startdate']
    enddata = sta['enddate']
    con = sqlite3.connect('task2.db')
    cur = con.cursor()
    k = 0
    x = list()
    datelist = list()
    start = '23/2/2021'
    end = '29/3/2021'
    startdate = time.strptime(startdata, "%Y-%m-%d")
    enddate = time.strptime(enddata, "%Y-%m-%d")
    #enddate = time.strptime(end, "%d/%m/%Y")

    for row in cur.execute('SELECT * FROM file'):

        datetime_object,p = row[0].split(' ')
        newdate = time.strptime(datetime_object, "%Y-%m-%d")
        #print(newdate,'  date')
        if newdate >= startdate and newdate <= enddate:
            datelist.append(newdate)
            x.append(list(row))
        #print(row,k)
        k = k+1

    print(x)


    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(x)

    v = jsonify('innovators.csv')
    #return 'pooja'
    return send_file('innovators.csv', mimetype='text/csv')




        #return send_file('innovators.csv', mimetype='text/csv')




def draw_faces(filename, xmlfile):
	# load the image
    pyplot.switch_backend('Agg')
    data = pyplot.imread(filename)
    img = Image.open(filename)

    pyplot.imshow(data)

    # get the context for drawing boxes
    ax = pyplot.gca()
    #result_list = parseXml(xmlfile)

    for i in xmlfile:
        [img, object, x1, y1, x2, y2] = i
        #[x1, y1, x2, y2] = i
        width, height = x2-x1, y2-y1
        print(x1,y1,width,height)
		# get coordinates
        rect = Rectangle((x1,y1), width, height, fill=False, color='red')
        ax.add_patch(rect)
		# draw the box
        pyplot.text(x1,y1,object, fontsize=12, color='red')

		#pyplot.imshow(data[y1:y2, x1:x2])
		#img2 = img.crop((x1, y1, x2, y2))
		#img2.save(p+".jpg")
    pyplot.savefig('p4.png')
    pyplot.close()
    return send_file('p4.png', mimetype='image/gif')
	# plot each face as a subplot
