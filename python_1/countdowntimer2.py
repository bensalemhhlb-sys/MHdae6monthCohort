#imported "time" module to deal with time related function
import time

#ask countdown-timer

count_down_time = int(input("Enter time in seconds: "))

#check countdown-time must be a positive number
while count_down_time >= 0:

    #convert time to various time format
    minutes = count_down_time // 60
    seconds = count_down_time % 60

    #set time's format
    time_format = f"{minutes:02d}:{seconds:02d}"

    #display LIVE countdown
    print(f"\rCountdown time:", time_format, end="", flush=True)

    #delay execution time by 1 second 
    time.sleep(1)

    #decrease current time by 1 second
    count_down_time = count_down_time-1

# display Time's up once countdown stopped
print("\nTime's up!!!")