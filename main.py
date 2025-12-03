import time

def calculate_fare(sec_stopped, sec_moving):    # Function to calculate rate
    fare = sec_stopped * 0.02 + sec_moving * 0.05
    print(f"Total for the trip: {fare}\n")
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
                continue
            
            print("Start Trip\nTrip started. Initial state: 'stopped'.")
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Start in the ‘stopped’ state.
            
        
        elif command in ("stop", "move"):
            if trip_active == False:
                print("‼️  Error: You must start the trip first.")
                continue             

            # Calculate the stop and move times.
            stopped_time, moving_time = calculate_time(state, stopped_time, moving_time, start_time)

            # Time count change
            if command == "stop":
                state = 'stopped'
            else:
                state = 'moving'

            print(f"🔰   The status has changed to '{state}'.") 
            start_time = time.time()

        elif command == "finish":
            if trip_active == False:
                print("‼️  Error: There are no active trips.")
                continue
            trip_active = False

            # Calculate the stop and move times.
            stopped_time, moving_time = calculate_time(state, stopped_time, moving_time, start_time)

            print(stopped_time) # Check times
            print(moving_time)

            calculate_fare(stopped_time, moving_time) # Function to calculate rate

            # Reset variables
            trip_active = False
            state = None

        elif command == "exit":
            print("That's all for today.\n")
            break
        else:
            print("⚠️   Unknown command.")

if __name__ == "__main__":
    taximeter()