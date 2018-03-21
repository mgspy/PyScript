# note that this will only work on a windows computer

import os
from sys import argv

script = argv
name = str(script[0])

terminal = 'start payload.rtf'
os.system(terminal)
os.mkdir('clone')
os.system(r'copy payload.txt clone')
os.system(r'copy' + name + 'clone')
