import os
import shutil
path = os.getcwd()
print path

if path[1] == 'U':
	opsys = 'mac'
elif path[1] == ':':
	opsys = 'win'
elif path[1] == 'h':
	opsys = 'linux'
	
print opsys
'''
os.chdir('/Users/aubhrosengupta/Documents')
os.remove('textTry.py')
print opsys
	'''
'''
os.remove()
os.rmdir()
shutil.rmtree()
os.chdir(path)
'''
