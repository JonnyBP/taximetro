import customtkinter as ctk
from main import TaximeterLogic, custom_fare

class TaximeterApp(ctk.CTk):

    def __init__(self, logic_instance):
        super().__init__()

        self.logic = logic_instance
        self.title("Taximeter")
        self.geometry("800x450")
        ctk.set_appearance_mode("System") # Modo oscuro/claro del sistema


        self.setup_ui()
        self.display_status()

    def setup_ui(self):

        self.title_label = ctk.CTkLabel(self, text="TAXIMETER F5", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=15)

        # Botones
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=30, padx=30)

        # START
        self.start_button = ctk.CTkButton(button_frame, text="START", command=self.start_command, width=200)
        self.start_button.grid(row=0, column=0, padx=10, pady=5)
        
        # MOVE
        self.move_button = ctk.CTkButton(button_frame, text="MOVE", command=lambda: self.state_command('moving'), width=200)
        self.move_button.grid(row=0, column=1, padx=10, pady=5)
        
        # STOP
        self.stop_button = ctk.CTkButton(button_frame, text="STOP",command=lambda: self.state_command('stopped'), width=200)
        self.stop_button.grid(row=0, column=2, padx=10, pady=5)
        
        # LABEL STATUS
        self.status_label= ctk.CTkLabel(self, text= "INACTIVE", font=("Arial",20))
        self.status_label.pack(pady=10)

        # LABEL STATUS
        self.fare_label= ctk.CTkLabel(self, text= "", font=("Arial",25))
        self.fare_label.pack(pady=10)

        # FINISH
        self.finish_button = ctk.CTkButton(self, text="FINISH",command=self.finish_command, fg_color="red", hover_color="#CC0000")
        self.finish_button.pack(pady=50)

        # Simple command
    def start_command(self):
        self.logic.start_trip()
        self.fare_label.configure(text="", font=("Arial",25))
        self.display_status()
    
    def state_command(self, new_state):
        self.logic.change_state(new_state)
        self.display_status()
    
    def finish_command(self):
        self.logic.finish_trip()
        self.display_final_result()

    def display_status(self):
        status = self.logic.get_status()

        if status["active"]:
            #self.fare_label.configure(text="", font=("Arial",25))
            self.status_label.configure(text=f"ESTADO: {status['state'].upper()}")
        else:
            #self.fare_label.configure(text="INICIE VIAJE", text_color="gray")
            self.status_label.configure(text="")

    def display_final_result(self):
        status = self.logic.get_status()
            
        self.fare_label.configure(text=f"Finished trip: €{status['total_fare']:.2f}", text_color="green")
        self.status_label.configure(
            text=f"FINALIZADO | Mov: {status['moving_time']:.2f}s | Par: {status['stopped_time']:.2f}s"
        )


# Ejecutar
if __name__ == "__main__":

    stopped, moving = 0.05,0.02 
    
    # 2. Crear la instancia de la lógica (¡ESTO ES NECESARIO!)
    logic = TaximeterLogic(stopped, moving)
    
    # 3. Crear la aplicación de la GUI y PASARLE la lógica
    app = TaximeterApp(logic_instance=logic) 
    
    # 4. Iniciar el bucle principal de CustomTkinter
    app.mainloop()