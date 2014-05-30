###KBCO Code
##Name: CRossi
##Program to scrape the KBCO look_for_your_name page for my name, and email me if it is there
import urllib2
import re
from flask import Flask, request, render_template
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
def kbco_home_page():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def kbco_post():
        mongo = MongoClient().kbco_names
        mongo.subscriptions.insert({'name':request.form['name'],'email':request.form['email']})
	return render_template("signed_up.html")	

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
