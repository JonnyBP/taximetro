import time

def taximeter():
    #Función para manejar y mostrar opciones

    print("Welcome to the F5 Taximeter\n" \
            "Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    # Declaramos variables

    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None  # 'stopped' o 'moving'


    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if trip_active == True:
                print("Error: A trip is already in progress")
                continue
            
            print("Start Trip\nTrip started. Initial state: 'stopped'.")
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Iniciamos en estado 'stopped'
            
        
        elif command in ("stop", "move"):
            if trip_active == False:
                print("Error: The trip isn't active")
                continue
            print("Acción")

            # Calculamos los tiempos de stop y move
            duration = time.time() - start_time  # lo ponemos a 0
            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration     


        elif command == "finish":
            if trip_active == False:
                print("Error: No active trip to finish")
                continue
            trip_active = False

            # Calculamos los tiempos de stop y move
            duration = time.time() - start_time  # lo ponemos a 0
            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration  

            print(duration)

        elif command == "exit":
            print("Un gusto, vuelve pronto")
            break
        else:
            print("Unknown command.")
taximeter()