# python
import time

def timer(minutes):
    print("Welcome to your notebook")
    
    message = "Time's up, please log in"
    total_seconds = minutes * 60
    
    while total_seconds > 0:
        # Calculate minutes and seconds from the remaining total
        mins, secs = divmod(total_seconds, 60)
        
        # Format as MM:SS
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        
        # Overwrite the current line with the updated time
        print(f"Time remaining: {timeformat}", end="\r")
        
        # Pause for exactly 1 second
        time.sleep(1)
        
        total_seconds -= 1
        
    # Clear the countdown line and print the final message
    print("\n" + message)

# Example: Run the countdown for 10 minutes
timer(10)