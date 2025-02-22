from flask import Flask, render_template, request, redirect, url_for, flash, session

from logging import FileHandler, WARNING
import os
import sys
import cvlib as cv

import numpy as np
import time
from cvlib.object_detection import draw_bbox
import cv2
import numpy as np
import mysql.connector as mysql

app = Flask(__name__)

app.secret_key = os.urandom(24)

fn = ""


@app.route('/')
def home():
    return render_template('Homepage.html')


@app.route('/about')
def about():
    return render_template('Aboutus.html')


@app.route('/contact')
def contact():
    return render_template('Contactus.html')


@app.route('/Register')
def Register():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='OnlineAds')
    cursor = db_connection.cursor()
    cursor.execute("select MAX(Regid) from Register")
    data = cursor.fetchone()
    rid = data[0]
    if rid == None:
        rid = "1"
        print(rid)
    else:
        rid = rid + 1
    return render_template('Register.html', Regid=rid)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":

        try:
            Regid = request.form['Regid']
            rname = request.form['rname']
            gender = request.form['gender']
            contact = request.form['contact']
            email = request.form['email']
            Address = request.form['Address']
            city = request.form['city']
            role = request.form['role']
            uname = request.form['uname']
            password = request.form['password']
            db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                          database='OnlineAds')
            cursor = db_connection.cursor()

            cursor.execute(
                "INSERT INTO Register (rname, gender,contact,email,Address,city,role,uname,password) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s)",
                (rname, gender, contact, email, Address, city, role, uname, password))

            db_connection.commit()

            # flash("Data Inserted Successfully")
            return redirect(url_for('Register'))
        except (Exception) as e:
            print(e)
        return render_template('Register.html')


@app.route('/insertprebook', methods=['POST'])
def insertprebook():
    if request.method == "POST":

        try:
            print("1")
            ownername = request.form['ownername']
            vnumber = request.form['vnumber']
            vname = request.form['vname']
            username = request.form['username']
            contact = request.form['contact']
            email = request.form['email']
            print("2")
            db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                          database='OnlineAds')
            cursor = db_connection.cursor()

            cursor.execute(
                "INSERT INTO prebook (ownername, vnumber,vname,username,contact,email) VALUES (%s, %s, %s, %s,%s,%s)",
                (ownername, vnumber, vname, username, contact, email))

            db_connection.commit()

            # flash("Data Inserted Successfully")
            return render_template('Prebooking.html')
        except (Exception) as e:
            print(e)

        return render_template('Prebooking.html')


@app.route('/checklogin', methods=['POST'])
def checklogin():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']
        utype = request.form['utype']
        if username == 'Admin' and password == 'Admin' and utype == 'Admin':
            return redirect(url_for('ViewAds1'))
        else:
            db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                          database='OnlineAds')
            cursor = db_connection.cursor()
            cursor.execute("SELECT  uname,password,role FROM Register WHERE uname = '%s' AND password = '%s'" % (
                username, password))
            account = cursor.fetchone()
            uname, pw, role = account
            session["uname"] = uname
            if account:
                if role == "Seller":
                    cursor.close()
                    return redirect(url_for('postads'))
                elif role == "Buyer":
                    cursor.close()
                    return redirect(url_for('viewpost'))
            else:
                flash("Record not found")
    return render_template('login.html')


@app.route('/viewpost')
def viewpost():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='OnlineAds')
    cursor = db_connection.cursor()
    cursor.execute("select * from postads")
    data = cursor.fetchall()
    cursor.close()
    return render_template('ViewAds.html', postlist=data)


@app.route('/postads')
def postads():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='OnlineAds')
    cursor = db_connection.cursor()
    cursor.execute("select MAX(postid) from PostAds")
    data = cursor.fetchone()
    postid = data[0]
    if postid == None:
        postid = "1"
    else:
        postid = postid + 1
    return render_template('PostAds.html', postid=postid)


@app.route('/prebook')
def prebook():
    return render_template('Prebooking.html')


@app.route('/insertAds', methods=['POST'])
def insertAds():
    global img
    if request.method == "POST":

        postid = request.form['postid']
        ownername = request.form['ownername']
        contact = request.form['contact']
        vname = request.form['vname']
        vtype = request.form['vtype']
        vnumber = request.form['vnumber']
        vmodelno = request.form['vmodelno']
        vmodelname = request.form['vmodelname']
        postalcode = request.form['postalcode']
        address = request.form['address']
        noofowner = request.form['noofowner']
        description = request.form['description']
        price = request.form['price']
        f = request.files['file']
        f1=f.filename
        print(f1)
        print(f.filename)


        img = cv2.imread("D:/" + f.filename)



        classNames = []
        classFile = "D:/Online Ads final/Online Ads final/coco.names"

        with open(classFile, "rt") as f:
            classNames = f.read().rstrip("\n").split("\n")

        configPath = "D:/Online Ads final/Online Ads final/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        weightsPath = "D:/Online Ads final/Online Ads final/frozen_inference_graph.pb"

        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        def getObjects(img, thres, nms, draw=True, objects=[]):
            classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
            # print(classIds,bbox)
            if len(objects) == 0: objects = classNames
            objectInfo = []
            if len(classIds) != 0:
                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    className = classNames[classId - 1]
                    if className in objects:
                        objectInfo.append([box, className])
                        if (draw):
                            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                            cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                            cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


            return img, className

        result, objectInfo = getObjects(img, 0.45, 0.2, objects=['car', 'motorcycle', 'person'])
        print(objectInfo)
        if objectInfo == 'car' or objectInfo == 'motorcycle':
            print("after data")
            db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                          database='OnlineAds')
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT  ownername,vnumber,vname,vmodelno,vmodelname,pincode FROM Vehicledetails  where ownername = '%s' AND vnumber = '%s' AND vname = '%s' AND vmodelno = '%s' AND vmodelname = '%s' AND pincode = '%s'  " %
                (ownername, vnumber, vname, vmodelno, vmodelname, postalcode))
            data = cursor.fetchone()
            cursor.close()
            if data:
                print("after data")
                db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='OnlineAds')
                cursor = db_connection.cursor()
                cursor.execute(
                    "INSERT INTO postads (ownername, contact,vname,vtype,vnumber,vmodelno,vmodelname,postalcode,address,noofowner,description,price,video)  VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                 (
                ownername, contact, vname, vtype, vnumber, vmodelno, vmodelname, postalcode, address, noofowner,description, price, f1))

                db_connection.commit()

        # flash("Data Inserted Successfully")
            return render_template('sucess.html')
        return render_template('sucess.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/Logout')
def Logout():
    return render_template('Login.html')


@app.route('/Addfeedback')
def Addfeedback():
    return render_template('Feedback.html')


@app.route('/Viewfeedback')
def Viewfeedback():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='OnlineAds')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * FROM feedback")
    data = cursor.fetchall()
    cursor.close()
    return render_template('Viewfeedback.html', feedbacklist=data)


@app.route('/viewbooking')
def viewbooking():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='OnlineAds')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * FROM prebook")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewbooking.html', book=data)


@app.route('/insertfeedback', methods=['POST'])
def insertfeedback():
    if request.method == "POST":
        try:
            cdate = request.form['cdate']
            clientname = request.form['clientname']
            prodname = request.form['prodname']
            prodtype = request.form['prodtype']
            feedback = request.form['feedback']
            description = request.form['descri']
            db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                          database='OnlineAds')
            cursor = db_connection.cursor()
            cursor.execute(
                "INSERT INTO Feedback (cdate,clientname,prodname,prodtype,feedback,description) VALUES ( %s, %s, %s,%s,%s,%s)",
                (cdate, clientname, prodname, prodtype, feedback, description))

            db_connection.commit()
            # flash("Data Inserted Successfully")
            return redirect(url_for('Addfeedback'))
        except (Exception) as e:
            print(e)
        return redirect(url_for('Addfeedback'))


@app.route('/rules')
def rules():
    return render_template('Rules.html')


if __name__ == "__main__":
    # app.run(host='localhost', port=5000)
    app.run()

# pip install Flask-Session
