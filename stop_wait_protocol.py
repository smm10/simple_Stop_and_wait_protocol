#stop_wait
import random

import time


#acknowledge = 0
#frame_no = 0

def sender(data):
    #global acknowledge
    #global frame_no
    #print(acknowledge,frame_no)
    ack = receiver(transmission(data))
    

    if ack ==1:
        print("ack successfully received from the user")
        flag = False

    else:
        flag = True
            

    while flag == True:
        print("resending the data")
        if receiver(transmission(data))==1:
            flag = False
            print("data sent successfully")
        else:
            pass
            
        
    
    
def receiver(data):
    #global acknowledge
    #global frame_no
    #print(acknowledge,frame_no)
    if data==-1:
        return 0 #this is the ack
    else:
        return 1 # this is the ack




    
def transmission(data):
    time.sleep(1)
    return random.choice([data,-1])
    



data = "1233"

sender(data)

