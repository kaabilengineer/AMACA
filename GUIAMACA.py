 

# from tkcalendar import calendar
from multiprocessing import Process
import customtkinter
from tkinter import *
import speech_recognition as sr
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import threading
from Tkvideo import *
import m

    
        

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")



                        





i=0
th=threading.Thread(target=m.GANESHA)                
s1="white"
s2="blue"#2f6de1
s3="#2f6de1"    
stri="gh"                
def win():


        try: 
                filed=open('color.txt','r')
                color1=filed.readline()
                color1=color1.strip()
                filed.close()
                root = customtkinter.CTk()
                root.title("𝗔𝗠𝗔𝗖𝗔")
                root.iconbitmap('amacasymbol.ico')
                root.configure(fg_color="#282727")
                root.geometry("1000x600")
                root.resizable(width=False, height=False)
                
                def close():
                        # root.destroy()
                        m.ex()
                
                root1=customtkinter.CTkFrame(root,height=600,border_color=color1,border_width=3,fg_color="black")
                root1.pack(side=TOP,fill=[BOTH])
                frame1=customtkinter.CTkFrame(root1,height=594,width=90,fg_color="black")#383838
                frame1.pack(side=LEFT,padx=3,pady=3,fill=[BOTH])
                

                img=PhotoImage(file='1.png')
                img2=PhotoImage(file='3.png')
                img3=PhotoImage(file='help.png')
                img4=PhotoImage(file='c.png')



        
                frame2=customtkinter.CTkFrame(root1,height=50,width=1000,fg_color="black",corner_radius=0)

                frame2.pack(side=TOP,padx=3,pady=3,fill=[BOTH])
                la1=customtkinter.CTkLabel(master=frame2,text="𝗔𝗠𝗔𝗖𝗔​",text_color=color1,text_font=("",45),height=30)
                la1.place(relx=0.35,rely=-0.19)

                button4=customtkinter.CTkButton(master=frame1,height=60,width=60,command=close,text="",image=img4,fg_color="#E0001F",corner_radius=10)
                button4.place(rely=0.55,relx=0.15)
                global frame5
                frame5=customtkinter.CTkTextbox(root1,height=544,width=600,fg_color="black",border_width=3,border_color=color1,text_font=("",14),text_color="white")
                frame5.pack(side=LEFT,padx=3,pady=3)

        
                def func():
                        j=0
                
                        # file11=open('out.txt','r')
                        # t1=len(file11.readlines())
                        # file11.close()
                        while True:
                                # if(j==0):
                                file12=open('out.txt','r')
                        
                                texts=file12.read()
                                frame5.insert(END, texts)
                                file12.close()
                                fil23=open('out.txt','w')
                                fil23.close()
                                sleep(3)
                                # speak1(m.t7)
                                # file12.close()
                                        
                                
        
                                # file11=open('out.txt','r')
                                # global t1
                                # t1=len(file11.readlines())
                                # file11.close()
                                # j=j+1
                                        
                                # if(t<t1):
                                        
                                #         j=0
                                #         speak1(j)
                        
                                
                
                        
                                
                th3=threading.Thread(target=func)

                th3.start()
                        # speak1(m.text)
                # th2 =threading.Thread(target=text1)
                # th2.start()
                frame6=customtkinter.CTkFrame(root1,height=544,width=310,fg_color="black",border_width=3,border_color=color1)

                frame6.pack(padx=3,pady=3)

                label55=Label(frame6,height=250,width=200,background="black")
                label55.place(relx=0.2,rely=0.2)
                player = tkvideo(r"bb2.gif", label55, loop = 1, size = (250,250),hz=25)
                player.play()
        
                def ss():
                        global i
                        if(i==0):
                                
                                th.start()
                                i=i+1
                        else:   
                                th1=threading.Thread(target=m.GANESHA)
                                m.st()
                                th1.start()
                                # m.GANESHA()
                button44=customtkinter.CTkButton(frame6,text="𝗔𝗠𝗔𝗖𝗔",text_color=color1,text_font=("",20),fg_color="black",command=ss)
                button44.place(relx=0.25,rely=0.7)

                def s():
                
                        settinfr(frame5)
                #      button1['state'] = DISABLED
                def r():
                        perinfofr(frame5)
                def t():
                        aboutme(frame5)
                        
                button1=customtkinter.CTkButton(frame1,image=img,width=60,height=60,text="",fg_color=color1,command=s)
                
                button1.place(rely=0.1,relx=0.13)
                button2=customtkinter.CTkButton(frame1,image=img2,width=60,height=60,text="",fg_color=color1,command=r)

                button2.place(rely=0.25,relx=0.13)
                def sp():
                        global s1
                        global s3
                        fileds=open("color.txt",'w')
                        s=s1
                        s1=s3
                        s3=s
                        fileds.write(s1)
                        fileds.close()

                        root.destroy()
                        win()
        
                def settinfr(root1):
                        
                
                        frame65=customtkinter.CTkFrame(root1,height=400,width=400,border_color=color1,border_width=3,fg_color="#383838")
                
                        l1=customtkinter.CTkLabel(frame65,text="Settings",text_font=("",22),text_color=color1)
                        

                        label121=customtkinter.CTkLabel(frame65,text="Change theme:",text_font=("",20),text_color=color1)
                        frame65.place(relx=0,rely=0)
                        l1.place(relx=0.3,rely=0.010001334)
                        label121.place(relx=0.06,rely=0.09)
                
                        def sd():

                                frame65.destroy()

                        buttonct=customtkinter.CTkButton(frame65,width=100,height=50,text="change theme",text_font=("",16),command=sp,fg_color=color1,text_color="black")
                        buttonct.place(relx=0.3,rely=0.2)
                        img4=PhotoImage(file='cl.png')

                        button121=customtkinter.CTkButton(frame65,width=60,height=30,text="",command=sd,corner_radius=5,fg_color="#E0001F",image=img4)
                        button121.place(relx=0.839998666,rely=0.010001334)
                def perinfofr(root12):
                        def sd1():

                                frame652.destroy()                  
                        frame652=customtkinter.CTkFrame(root12,height=400,width=400,border_color=color1,border_width=3,fg_color="black")
                
                        l12=customtkinter.CTkLabel(frame652,text="Personal Info",text_font=("",22),text_color=color1)
                        frame652.place(relx=0,rely=0)
                        l12.place(relx=0.3,rely=0.010001334)
                        img4b=PhotoImage(file='cl.png')
                        button121b=customtkinter.CTkButton(frame652,width=60,height=30,text="",command=sd1,corner_radius=5,fg_color="#E0001F",image=img4b)
                        button121b.place(relx=0.839998666,rely=0.010001334)
                        label121b=customtkinter.CTkLabel(frame652,text="Name:",text_font=("",20),text_color=color1)
                        label121b.place(relx=0.01,rely=0.09)
                        label121c=customtkinter.CTkLabel(frame652,text="DOB:",text_font=("",20),text_color=color1)
                        label121c.place(relx=0.01,rely=0.25)
                        st=StringVar()
                        g=customtkinter.CTkEntry(frame652,textvariable=st,height=15,text_font=("bold",15))
                        g.place(relx=0.3,rely=0.1)
                        # cal = Calendar(frame652, selectmode = 'day',year = 2020, month = 5,day = 22)
                        # cal.place(rely=0.4,relx=0.1)
                        # # print()
                        
                
                        def stry():     
                                st1=st.get()
                                print(st1)
                                filess=open('name.txt','w')
                                filess.write(st1+"\n")
                                filess.close()
                        # def stry1():     
                        #         st2=cal.get_date()
                        #         print(st2)
                        #         filess1=open('dob.txt','w')
                        #         filess1.write(st2+"\n")
                        #         filess1.close()
                        
                        b2=customtkinter.CTkButton(frame652,height=30,width=50,text="save name",fg_color=color1,command=stry,text_color="black",text_font=("",15))
                        b2.place(relx=0.67,rely=0.1)
                        bu3=customtkinter.CTkButton(frame652,height=30,width=50,text="save date",fg_color=color1,text_color="black",text_font=("",15))
                        bu3.place(relx=0.7,rely=0.8)
                def aboutme(root3):
                        def sd3():

                                frame653.destroy()                  
                        frame653=customtkinter.CTkFrame(root3,height=400,width=400,border_color=color1,border_width=3,fg_color="black")
                
                        l12=customtkinter.CTkLabel(frame653,text="About us",text_font=("",22),text_color=color1)
                        frame653.place(relx=0,rely=0)
                        l12.place(relx=0.3,rely=0.010001334)
                        img4b=PhotoImage(file='cl.png')
                        button121b=customtkinter.CTkButton(frame653,width=60,height=30,text="",command=sd3,corner_radius=5,fg_color="#E0001F",image=img4b)
                        button121b.place(relx=0.839998666,rely=0.010001334)
                        file13=open('info.txt','r')
                        cont=file13.read()
                        cont=cont.strip()
                        file13.close()
                        l13=customtkinter.CTkTextbox(frame653,text_font=("",14),text_color="white",height=300,width=350,fg_color="black")

                        l13.place(rely=0.1,relx=0.03)
                        l13.insert(END,cont)
                button3=customtkinter.CTkButton(frame1,width=60,height=60,text="",fg_color=color1,image=img3,command=t)
                button3.place(rely=0.4,relx=0.13)          

                


                

                root.mainloop()
        except EXCEPTION as e1:
                raise SystemExit()
# KeyboardInterrupt()
        
#2f6de1
