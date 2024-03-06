from customtkinter import *
import mysql.connector
from dotenv import load_dotenv
import os
from categories.transport_module import TransportModule

class Modules:
    def __init__(self, master, username):
        #$######## PANTALLA ############
        self.root = CTkToplevel(master)
        self.root.grab_set()
        
        self.root.config(bg="#FFFFFF")
        self.root.geometry("500x500")
        self.root.minsize(800, 600)
        
        #$########## BASE DE DATOS ############
        load_dotenv()
        host=os.getenv("HOST")
        user=os.getenv("USER")
        password=os.getenv("PASSWORD")
        
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        
        self.username = username
        
        self.widgets()
        
    
    
    #*############### FUNCTIONS ################
    def get_points(self):
        cursor=self.conexion.cursor()
        cursor.execute(f"SELECT * FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
        
        data=[]
        for bd in cursor:
            data.append(bd)

        p_1=data[0][2]
        p_2=data[0][3]
        p_3=data[0][4]
        p_4=data[0][5]
        
        suma = int((p_1 + p_2 + p_3 + p_4)/5)
        
        return suma

    def open_transport_module(self):
        TransportModule(self.root)
    
    """
    transporte publico
    calle
    eventos
    .....
    """
    
    #*################ WIDGETS ################
    def widgets(self):
        #$############# FRAME 1 ##################
        frame_1 = CTkFrame(
            self.root,
            fg_color="#FFFFFF",
            bg_color="#FFFFFF",
        )
        frame_1.pack(fill = 'x', pady=(15,0), expand=True)
        
        module_1 = CTkButton(
            frame_1,
            corner_radius=10,
            bg_color="#FFFFFF",
            fg_color="#444444",
            text="Module 1",
            width=340,
            height=200,
            command=self.open_transport_module
        )
        module_1.pack(pady=15, side="left", padx=30)
        
        module_2 = CTkButton(
            frame_1,
            corner_radius=10,
            bg_color="#FFFFFF",
            fg_color="#444444",
            text="Module 2",
            width=340,
            height=200
        )
        module_2.pack(pady=15, side="right", padx=30)
        
        #$############# FRAME 2 ################
        frame_2 = CTkFrame(
            self.root,
            fg_color="#FFFFFF",
            bg_color="#FFFFFF",
        )
        frame_2.pack(fill = 'x', pady=(0,15), expand=True)
        
        module_3 = CTkButton(
            frame_2,
            corner_radius=10,
            bg_color="#FFFFFF",
            fg_color="#444444",
            text="Module 3",
            width=340,
            height=200
        )
        module_3.pack(pady=15, side="left", padx=30)
        
        module_4 = CTkButton(
            frame_2,
            corner_radius=10,
            bg_color="#FFFFFF",
            fg_color="#444444",
            text="Module 4",
            width=340,
            height=200
        )
        module_4.pack(pady=15, side="right", padx=30)
        
        
        
        #$############### PROGRESS BAR ############
        progress_bar = CTkProgressBar(
            self.root,
            progress_color="blue",
            border_color="#FFFFFF",
            corner_radius=50,
            height=20,
            width=500,
            bg_color="#FFFFFF",
            fg_color="#CCCCCC",
            determinate_speed=6.25,
        )
        progress_bar.pack(pady=20)
        progress_bar.set(0)
        
        for i in range (self.get_points()):
            progress_bar.step()
        


if __name__ == "__main__":
    username = "user"
    root = CTk()
    app = Modules(root, username)
    root.mainloop()