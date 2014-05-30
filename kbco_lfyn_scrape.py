###Mongo DB for the KBCO site
##Name: CRossi
from pymongo import MongoClient
import urllib2
import re
import mandrill

def check_name(their_name):
    fucksoup = urllib2.urlopen('http://www.kbco.com/pages/lookforyourname.html').read()
    if (re.search(their_name, fucksoup, re.IGNORECASE)):
        return True
    return False

mongo = MongoClient().kbco_names
names_to_check = mongo.subscriptions.find()

for person in  names_to_check:
	if check_name(person['name']):
		print person['email']
		mandrill_client = mandrill.Mandrill('t6tvThT4JPvondnBhfqyGQ')
		message = {
			'from_email': 'solari18@hotmail.com',
		    	'from_name': 'Example Name',
		    	'subject': 'example subject',
		    	'text': 'Example text content',
		    	'to': [{'email': person['email'],
			    'name': person['name'],
			    'type': 'to'}]

		}



		result = mandrill_client.messages.send(message=message)
		print result
