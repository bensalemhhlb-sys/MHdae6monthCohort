
# countdown timer in its simplest form

# for i in range (10, 0, -1):
#     print(i)




# Project of a Countdown Timer
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        # this is to convert total time in seconds
        # into minutes and remaing seconds
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        # time format is to have 2 digits for min and for secs
        print(timeformat, end='\r')
        #(end='\r') to print text and jump back 
        # to the start of the same line 
        time.sleep(1)
        time_sec -= 1

    print("stop")
#enter the number of secons
countdown(60)