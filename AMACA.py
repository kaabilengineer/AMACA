import customtkinter 
from tkinter import *
customtkinter.set_appearance_mode("System") 

customtkinter.set_default_color_theme("blue")



root= customtkinter.CTk()
root.configure(fg_color="#282727")
root.attributes("-fullscreen", True)
optionmenu_1 = customtkinter.CTkOptionMenu(  values=["Option 1", "Option 2", "Option 3"])
optionmenu_1.pack(anchor='nw')
root.mainloop()