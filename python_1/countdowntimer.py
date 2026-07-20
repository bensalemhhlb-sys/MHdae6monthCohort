print("Welcome to your notebook")
import time
# set countdown time in minutes
def timer(time_sec):
    while time_sec:
    minutes = 10
    # message to show when time is up
    message = "time's up, please log in"
    # conert minuts to seconds
    total_seconds = minutes * 60
    while total_seconds > 0:
        min, secs = divmod(time_sec, 60)
        timeformat = "{:02d}:{:02d}". format(minutes, seconds)
        time.sleep
        time_sec -= 1
    