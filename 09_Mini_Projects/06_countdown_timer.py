# Project 06: Terminal Countdown Timer
import time

def start_timer():
    print("================================")
    print("        COUNTDOWN TIMER         ")
    print("================================")

    try:
        total_seconds = int(input("Enter duration in seconds: "))
    except ValueError:
        print("Error: Please enter an integer.")
        return

    print(f"\nStarting timer for {total_seconds} seconds...\n")
    for remaining in reversed(range(0, total_seconds + 1)):
        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        print(f"\rTime Remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)
        time.sleep(1)

    print("\n\n🔔 TIME IS UP!")

if __name__ == "__main__":
    start_timer()
