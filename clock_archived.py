import time
from datetime import datetime
import sys


def get_current_time():
    now = datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second
    milliseconds = str(now.microsecond)[:2]
    formatted_time = f" {hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds}"
    return formatted_time


def countdown_timer(seconds):
    end_time = time.time() + seconds
    while time.time() < end_time:
        remaining = end_time - time.time()
        if remaining <= 0:
            break

        mins, secs = divmod(int(remaining), 60)
        hours, mins = divmod(mins, 60)
        milliseconds = int((remaining - int(remaining)) * 100)

        formatted_time = f"{hours:02d}:{mins:02d}:{secs:02d}:{milliseconds:02d}"
        # print(formatted_time, end='\r')
        sys.stdout.write(f"\r{formatted_time}")
        sys.stdout.flush()
        time.sleep(0.01)

    print("Countdown finished!")


# Main loop
while True:
    try:
        user_input = input("\nEnter seconds to countdown (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        seconds = int(user_input)
        print(f"Starting countdown from {seconds} seconds...")
        time.sleep(1)
        countdown_timer(seconds)

    except ValueError:
        print("Please enter a valid number!")
    except KeyboardInterrupt:
        print("\nExiting...")
        break

# Continue with normal clock after countdown or exit
print("Back to normal clock:")
while True:
    try:
        current_time = get_current_time()
        print(current_time, end='\r')
        time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nExiting program...")
        break
