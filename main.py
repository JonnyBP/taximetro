import time
import logging
import datetime
import os


record_file = "Record.txt"

def trip_record(move_time, stop_time, total_fare):  # Save the history of an entire trip
    
    # Format to write
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    line_record = (
        f"[{timestamp}] "
        f"MOVING: {move_time:.2f}s | "
        f"STOPPED: {stop_time:.2f}s | "
        f"FARE: ${total_fare:.2f}\n"
    )

    # Add a new line to the file
    try:
        with open(record_file, "a") as f:
            f.write(line_record)
        return True
    except IOError as e:
        
        print(f"ERROR: Could not write to file {record_file}. {e}")
        logging.error(f"Could not write to file: {e}")
        return False
    


logging.basicConfig(
    level=logging.DEBUG,  # Minimum level of messages to display (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s', # Message format
    filename='taximeter.log',  
    filemode='a'    # ‘a’ to append 
)

def calculate_fare(sec_stopped, sec_moving):    # Function to calculate rate
    fare = sec_stopped * 0.02 + sec_moving * 0.05
    print(f"Total for the trip: €{fare:.2f}\n")
    return fare

def calculate_time(state, stopped_time, moving_time, start_time):   # Function to calculate time

    duration = time.time() - start_time  # Set 0
    if state == "stopped":
        stopped_time += duration
    else:
        moving_time += duration
    return stopped_time, moving_time   

def taximeter():    # Function to manage and display options

    print("=" * 55)
    print("    WELCOME TO THE TAXIMETER SERVICE F5   ")
    print("Available commands: 'start', 'stop', 'move', 'end'")

    # Declare variables
    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None  # 'stopped' o 'moving'

    while True:
        print("-" * 55)
        command = input("> ").strip().lower()
        
        if command == "start":
            if trip_active == True:
                print("‼️  Error: A trip is already in progress")
                logging.error("A trip is already in progress")
                continue
            
            print("Start Trip\nTrip started. Initial state: 'stopped'.")
            logging.info("Trip started. Initial state: 'stopped'.")
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Start in the ‘stopped’ state.
            
        
        elif command in ("stop", "move"):
            if trip_active == False:
                print("‼️  Error: You must start the trip first.")
                logging.error("You must start the trip first.")
                continue             

            # Calculate the stop and move times.
            stopped_time, moving_time = calculate_time(state, stopped_time, moving_time, start_time)

            # Time count change
            if command == "stop":
                state = 'stopped'
            else:
                state = 'moving'

            print(f"🔰   The status has changed to '{state}'.")
            logging.info(f"The status has changed to '{state}'.")  
            start_time = time.time()

        elif command == "finish":
            if trip_active == False:
                print("‼️  Error: There are no active trips.")
                logging.error("There are no active trips.")
                continue
            trip_active = False
            logging.info("Trip finished.")

            # Calculate the stop and move times.
            stopped_time, moving_time = calculate_time(state, stopped_time, moving_time, start_time)

            print(stopped_time) # Check times
            print(moving_time)

            fare = calculate_fare(stopped_time, moving_time) # Function to calculate rate
            trip_record(moving_time, stopped_time, fare)

            # Reset variables
            trip_active = False
            state = None

        elif command == "exit":
            print("That's all for today.\n")
            logging.debug("App closed. Come back soon.")
            break
        else:
            print("⚠️   Unknown command.")
            logging.warning("Unknown command.")

if __name__ == "__main__":
    taximeter()