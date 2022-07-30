from time import sleep
import os 
  
#installing the python module

cmd = 'pip install https.server'

#sleep command for the program

sleep(2)

#in the place of 127.0.0.1 put the user ip address

#running the python command in cmd

anothercmd = 'python -m http.server --bind 127.0.0.1 8080'

os.system(cmd)
os.system(anothercmd)

