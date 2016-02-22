from __future__ import print_function
import urllib

link = 'https://www.youtube.com/watch?v=UBtzpXSMcZg'
f = urllib.urlopen(link)
myFile = f.readline()

string = list(myFile)

listFile = myFile.split()
for j in range(len(string)):
    if string[j] == "<":
        print("\n")
    print(string[j], end="")


# for i in range(len(listfile)):
#	print(listfile[i])
