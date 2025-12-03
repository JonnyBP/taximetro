import time

def taximeter():
    #Función para manejar y mostrar opciones

    print("Welcome to the F5 Taximeter\n" \
            "Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if trip_active == True:
                print("Error: A trip is already in progress")
                continue
            trip_active = True
            print("moviendo")
        
        elif command in ("stop", "move"):
            if trip_active == False:
                print("Error: The trip isn't active")
                continue
            print("Acción")

        elif command == "finish":
            if trip_active == False:
                print("Error: No active trip to finish")
                continue
            trip_active = False
            print("Recorrido terminado")

        elif command == "exit":
            print("Un gusto, vuelve pronto")
            break
        else:
            print("Unknown command.")
taximeter()