from __future__ import print_function
import urllib

link = "http://www.cnn.com/"
f = urllib.urlopen(link)           
myfile = f.readline() 

string = list(myfile)

listfile = myfile.split()

for j in range(len(string)):
	if string[j] == "<":
		print ("\n")
	print(string[j], end="")


#for i in range(len(listfile)):
#	print(listfile[i])
