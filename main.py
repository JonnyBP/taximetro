import time
import logging
import datetime
import os

# ==============================================================================
# 1. SETUP AND CALCULATION FUNCTIONS
# ==============================================================================

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
        
        print(f"‼️  Error: Could not write to file {record_file}. {e}")
        logging.error(f"Could not write to file: {e}")
        return False

def calculate_fare(sec_stopped, sec_moving, fare_stopped, fare_moving):    # Function to calculate rate
    fare = sec_stopped * fare_stopped + sec_moving * fare_moving
    #print(fare_stopped,fare_moving)
    print(f"Total for the trip: €{fare:.2f}\n")
    return fare

logging.basicConfig(
    level=logging.DEBUG,  # Minimum level of messages to display (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s', # Message format
    filename='taximeter.log',  
    filemode='a'    # ‘a’ to append 
)

# ==============================================================================
# 2. LOGIC CLASS (State Management and Events)
# ==============================================================================

class TaximeterLogic:

    def __init__(self,fare_stopped, fare_moving):
        # Declare variables
        self.trip_active = False
        self.start_time = time.time()
        self.stopped_time = 0
        self.moving_time = 0 
        self.state = None  # 'stopped' o 'moving'
        self.fare_stopped = fare_stopped
        self.fare_moving = fare_moving
        self.fare = 0
        
    def update_time(self):   # Function to calculate time
        if not self.trip_active or not self.state:
            print(f"Time is not updated. trip_active= {self.trip_active}, current_state= {self.state}")
            logging.debug(f"Time is not updated. trip_active= {self.trip_active}, current_state= {self.state}")
            return

        duration = time.time() - self.start_time    
        if self.state == "stopped":
            self.stopped_time += duration
        elif self.state == "moving":
            self.moving_time += duration
        else:
            print(f"Not recognized state: '{self.state}'")

        self.start_time = time.time()
    
# CONTROL METHODS (Replace the command 'if')

    def start_trip(self):
        if self.trip_active == True:
            print("‼️  Error: A trip is already in progress")
            logging.warning("A trip is already in progress")
            return

        self.state = 'stopped'   
        self.trip_active = True
        self.start_time = time.time()
        self.stopped_time = 0
        self.moving_time = 0

        print("Start Trip\nTrip started. Initial state: 'stopped'.")
        logging.info(f"Trip started. Initial state: '{self.state}'.")

    def change_state(self, new_state):
        if self.trip_active == False:
            print("‼️  Error: You must start the trip first.")
            logging.warning("You must start the trip first.")
            return

        # Calculate the stop and move times.
        self.update_time()
        self.state = new_state

        logging.info(f"The status has changed to '{new_state}'.")
        return f"🔰   The status has changed to '{new_state}'."
        
    def finish_trip(self):
        if self.trip_active == False:
            print("‼️  Error: There are no active trips.")
            logging.warning("There are no active trips.")
        
        self.update_time()

        self.fare = calculate_fare(self.stopped_time, self.moving_time, self.fare_stopped,self.fare_moving) # Function to calculate rate
        trip_record(self.moving_time, self.stopped_time, self.fare)
        
        # Reset variables
        self.trip_active = False
        self.state = None
        logging.info("Trip finished.")
    
    # Function for GUI
    def get_status(self):
        """Devuelve el estado actual para la GUI."""
        return {
            "active": self.trip_active,
            "state": self.state,
            "moving_time": self.moving_time,
            "stopped_time": self.stopped_time,
            "total_fare": self.fare if not self.trip_active else 0.0
        }


def custom_fare():  # Request rates from the user 
    
    print("\n--- RATE SETTINGS ---")
    
    user_input = input("Use default rates? (y/n): ").lower()

    if user_input == "y":
        # Convert values
        fare_stopped = 2 / 100     # 0.02 €
        fare_moving = 5 / 100      # 0.05 €
        print("Using default rates")
        logging.debug("Taximeter initialized with customized rates.")
        return fare_stopped, fare_moving
    
    else:
        print("Entering custom rates (in cents)")
        
        try:
            #fare_base = float(input("Tarifa Base: ")) / 100
            fare_stopped = float(input("Cost per second STOPPED: ")) / 100
            fare_moving = float(input("Cost per second MOVEMENT: ")) / 100
            logging.debug(f"Rates: Moving= {fare_moving}, Stopped= {fare_stopped}")
            return fare_stopped, fare_moving
        
        except ValueError:
            print("Error in input. Using default rates.")
            logging.error("The user entered a non-numeric value for the rate. Using default values.")
            return 2/100, 5/100

# ==============================================================================
# 3.  Section to be removed if GUI is used
# ==============================================================================

def taximeter(logic):
    # Create an instance of the logic
    #logic = TaximeterLogic()

    print("=" * 55)
    print("    WELCOME TO THE TAXIMETER SERVICE F5   ")
    print("Available commands: 'start', 'stop', 'move', 'end'\n")

    while True:

        print("-" * 55)
        command = input("> ").strip().lower()
            
        if command == "start":
            message = logic.start_trip()
            print(message)
                
        elif command == "move":
            message = logic.change_state('moving')
            print(message)
            
        elif command == "stop":
            message = logic.change_state('stopped')
            print(message)

        elif command == "finish":
            message = logic.finish_trip()
            print(message)

        elif command == "exit":
            if logic.trip_active == True:
                logic.finish_trip()

            print("That's all for today.\n")
            logging.info("App closed. Come back soon.")
            break
        else:
            print("⚠️   Unknown command.")
            logging.warning("Unknown command.")


if __name__ == "__main__":
    stopped, moving = custom_fare()
    logic = TaximeterLogic(stopped, moving)
    taximeter(logic)