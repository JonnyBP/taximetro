import time

def taximeter():
    #Función para manejar y mostrar opciones

    print("Welcome to the F5 Taximeter\n" \
            "Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            print("moviendo")
        
        elif command in ("stop", "move"):
            print("Acción")
        elif command == "finish":
            print("Recorrido terminado")
        elif command == "exit":
            print("Un gusto, vuelve pronto")
            break
        else:
            print("Unknown command.")
taximeter()