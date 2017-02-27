import requests
import json
import urllib2
def send_simple_message(t,k):
    return requests.post(
		"https://api.mailgun.net/v3/sandbox7303d09412ec485291ab583873bf6f18.mailgun.org/messages",
		auth=("api", "key-7f645cc5a2bee3a37fcc5328acb43497"),
		data={"from": "P16023 <jimisgkiolis2013@hotmail.com>",
			"to": t,
			"subject": "The perfect beer for you",
			"text":k})
response1 = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')
html1 = response1.read()
html1=html1.replace("<br>","")
html1=html1.strip()
lines1=html1.split("\n")
header1= lines1[0].split(",")
k=header1[1]
print "Welcome to the app of random selection beer!!"
print "You have two choises!!"
print "If you want to send to unipi@mailinator.com press 1."
print "If you want to send to tester@mailinator.com press 2."
x=raw_input()
while (x!="1" and x!="2"):
	print "Please insert a valid number!"
	print "If you want to send to unipi@mailinator.com press 1."
	print "If you want to send to tester@mailinator.com press 2."
	x=raw_input()
em1="unipi@mailinator.com"
em2="tester@mailinator.com"
if x=="1":
	send_simple_message(em1,k)
else:
	send_simple_message(em2,k)
print "And the beer has ",header1[1]
