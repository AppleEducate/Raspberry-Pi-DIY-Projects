import time, sys
Seq = [[1,0,0,1], # Define step sequence
       [1,1,0,0],
       [0,0,1,1],
       [0,0,0,1]]
all_clear = True
running = True
    global all_clear
    while running:
        value = sensor.distance
        if value < 0.1: # trigger if obstacle within 10cm
            all_clear = False
        else:
            all_clear = True

    StepDir = seqsize # Set to 1 or 2 for fwd, -1 or -2 for back
    if direction == 'B':
                    Lpin.on() # Left wheel only
                    Rpin.on() # Right wheel only
                Lpin.off()
                Rpin.off()
        if (StepCounter<0):
        time.sleep(WaitTime) #pause 
        counter+=1

t1.start() # start bump watch thread