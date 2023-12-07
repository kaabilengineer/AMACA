import customtkinter

def f():
            # speak1("GANESHA")
            
            frame1=customtkinter.CTkFrame(height=600,width=480,fg_color="#282727")
            
            frame1.pack(fill="x")
            
            button3=customtkinter.CTkButton(text="User login",text_font=("italic",12,"bold"),text_color="#282727",fg_color="#2f6de1",bg_color="#282727")
            
            button4=customtkinter.CTkButton(text="Admin login",text_font=("italic",12,"bold"),text_color="#282727",fg_color="#2f6de1",bg_color="#282727")
            
            l3=customtkinter.CTkLabel(text="or",text_font=("italic",20),bg_color="#282727")
            
            button3.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
            
            l3.place(relx=0.5,rely=0.6,anchor=customtkinter.CENTER)
            
            button4.place(relx=0.5,rely=0.7,anchor=customtkinter.CENTER)


customtkinter.set_appearance_mode("System") 

customtkinter.set_default_color_theme("blue")

# customtkinter.set_window_scaling(3)

root= customtkinter.CTk()
root.configure(fg_color="#282727")
root.geometry("600x480")
# root.minsize(600,400)
# root.maxsize(600,400)

frame1=customtkinter.CTkFrame(height=140,fg_color="#2f6de1")
# frame1.place(relx="0.5",rely="0.1",anchor=customtkinter.CENTER)

frame1.pack(fill="x")

l1=customtkinter.CTkLabel(master=frame1,text="ꪖ​ꪑꪖ​ᥴꪖ​",text_color="#282727",height=130,text_font=("italic",42)  )

l1.pack(anchor="n")

button1=customtkinter.CTkButton(text="Login",text_font=("italic",12,"bold"),text_color="#282727",fg_color="#2f6de1",command=f)

button2=customtkinter.CTkButton(text="Sign up",text_font=("italic",12,"bold"),text_color="#282727",fg_color="#2f6de1",command=f)

l2=customtkinter.CTkLabel(text="or",text_font=("italic",20))

button1.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)

l2.place(relx=0.5,rely=0.6,anchor=customtkinter.CENTER)

button2.place(relx=0.5,rely=0.7,anchor=customtkinter.CENTER)

root.mainloop()