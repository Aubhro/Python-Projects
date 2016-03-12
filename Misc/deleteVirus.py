

import os
path = os.getcwd()
print path

"""
Finds out if user is on mac, linux, or windows.
"""
if path[1] == 'U':
	opsys = 'mac'
elif path[1] == ':':
	opsys = 'win'
elif path[1] == 'h':
	opsys = 'linux'
else:
    opsys = "null"

print opsys
"""
If you uncomment code and replace directory path and file name,
program will delete file.
"""
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
