import urllib2
import json
import webbrowser
dt=raw_input("Give me an ingredient: ")
k='http://food2fork.com/api/search?key=63901198aa257c2ca3d2f29669b87094&q=';
lista=list(k)
lista.extend([dt])
t=''.join(lista)
response = urllib2.urlopen(t)
html = response.read()
html=html.replace("<br>","")
html=html.strip()
lines=html.split("\n")
header= lines[0].split(",")
w=list(header[0])
del w[0:10]
while w[0]=="0":
    dt=raw_input("You gave wrong ingredient so give a right ingredient: ")
    k='http://food2fork.com/api/search?key=63901198aa257c2ca3d2f29669b87094&q=';
    lista=list(k)
    lista.extend([dt])
    t=''.join(lista)
    response = urllib2.urlopen(t)
    html = response.read()
    html=html.replace("<br>","")
    html=html.strip()
    lines=html.split("\n")
    header= lines[0].split(",")
    w=list(header[0])
    del w[0:10]
print "The food has ",header[3]
response1 = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')
html1 = response1.read()
html1=html1.replace("<br>","")
html1=html1.strip()
lines1=html1.split("\n")
header1= lines1[0].split(",")
print "And the beer has ",header1[1];
x=raw_input("For more informaation about the recipe of the food press 1: ")
if x!="1":    
    print "Thank you for the patient,press any key to exit"
else:
        x=list(header[4]);
        del x[0:16];
        del x[-1];
        k=''.join(x);
        webbrowser.open(k)