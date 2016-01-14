Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import pyquery
>>> import requests
>>> for i in range(10):
	p = pyquery.PyQuery("http://caodan.org/"+str(i+1)+"-ask.html")
	content = p(".content").text()
	file_object = open("/home/huang/wenti/"+str(i+1)+".txt","w")
	file_object.write(content.encode("utf-8"))
	print i+1
	file_object.close()

	
1
2
3
4
5
6
7
8
9
10
>>> import urllib2
>>> for i in range(10):
	img=urllib2.urlopen("http://caodan.org/wp-content/uploads/vol/"+str(i+1)+".jpg")
	file_object = open("/home/huang/photos/"+str(i+1)+".jpg","wb")
	file_object.write(img.read())
	print i+1
	file_object.close()
	
>>> 
>>> 
