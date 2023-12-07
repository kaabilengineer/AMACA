


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import random
# from termcolor import colored
# from colored import fg
import colorama
from pygame import mixer
import time
global text
text=""
boo=True
mybt=ChatBot("Amaca",storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3')
trainw=ChatterBotCorpusTrainer(mybt)
trainw.train('chatterbot.corpus.english')
engine=pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
mixer.init()
def st():
    global boo
    boo =True
def ex():
    global boo
    boo =False
# def disp():
file=open('name.txt','r')
name=(file.readline())    
name=name.strip()
file.close()
file2=open('dob.txt','r')
dob=file2.readline()
dob=dob.strip()
file2.close()

def GANESHA():
        
        def speak1(query1):
          
            file=open('out.txt','a')
            file.write(query1+'\n')
            file.flush()

        def bots(query2):
            file23=open("out.txt","a")
            file23.write(query2+'\n')
            file23.flush()

        def speak(audio):

            engine.say(audio)
            engine.runAndWait()
            
            
            
        def wishMe():
            hour=int(datetime.datetime.now().hour)
            mini=int(datetime.datetime.now().minute)
            
            if hour>=0 and hour<12:
               
                
                speak("good morning,AMACA here")
                speak1("AMACA:______________")
                speak1("good morning, AMACA here")  
                # "good morning"
            elif hour>=12 and hour<18:
      
                speak("good afternoon, AMACA here")    
                speak1("AMACA:______________")
                speak1("good afternoon, AMACA here")  
            else:
        
                global text
                text="good evening"
                ('blue')
                speak("good evening, AMACA here")
                speak1("AMACA:______________")
                speak1("good evening, AMACA here")
 
            text="AMACA here"
            # speak("AMACA here")
            # speak1("AMACA:______________")
            # speak1("AMACA here")
            
            
        def takeCommand():
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    speak1('\nlistening...')
                    r.adjust_for_ambient_noise(source)
                    #r.listen_in_background(source, callable)
                    r.pause_threshold*1
                    audio=r.listen(source)
                try:
                    speak1("recognizing.....")
                    query=r.recognize_google(audio, language='en-in')
                    speak1("YOU:______________")
                    speak1(f"{query}\n",)
                except Exception as e:
                    #print(e)
                    speak1("could'nt recognize")
                    return "none"
                return query





        
        wishMe()
        a=0

        while boo:
            
            query=takeCommand().lower()
            jokelist=["One joke, coming up! What is a sea monsters favorite snack?           Ships and dip.",              "How do robots eat guacamole?                With computer chips.",             "What happens to a lawyer who jumps out of a plane at 35,000 feet without a parachute?         Who cares?",             "How can you tell when a lawyer is lying?              His lips are moving.",             "I pretend to work;         They pretend to pay me",             "It just occurred to me that the opposite of Artificial Intelligence is             Real Stupid",                "I hear they’ve made a new artificially intelligent Oreo?               It’s one smart cookie.",             "Why are artificial intelligences in movies always female?             Because they’re never wrong.",              "What do you get when you cross a wall unit with artificial intelligence?         Shelf-awareness." ,                "When the first device with AI takes a picture of itself…       It’ll be selfie aware.",            "Why did the programmers act so nice to the AI?             Because it was really self conscious.",                "So I recently learned about AI.            It’s absolutely game changing.",            "Scientists predict human-level artificial intelligence by 2040.            Maybe sooner if the bar keeps dropping.",                "Where did the music teacher leave her keys?            In the piano!",                "What do you call a guy who’s really loud?              Mike.",            "Why do birds fly south in the winter?               It’s faster than walking!",                "What did the Dalmatian say after lunch?            That hit the spot!",             "What kind of math do birds love?           Owl-gebra!",                "What goes up and down but doesn’t move?               The staircase.",            "You know what I saw today?             Everything I looked at.",                "I hate Russian dolls…              they're so full of themselves!",            "What do you call bears with no ears?            B.",            "What's a foot long and slippery?                  A slipper!",                "What do you call a boomerang that doesn't come back?               A stick!",                "Here, I bought you a calendar.                 Your days are numbered now.",            "I have many jokes about rich kids.          sadly none of them work.",                "What did 0 say to 8?               Nice belt!",            "How do trees get online?           They just log on!",                "50 cent was two steps away from 60 when he was given his meal, why?            Because 50 ate.",                "I had a dream where an evil queen forced me to eat a gigantic marshmallow.              When I woke up, my pillow was gone.",            "Can a kangaroo jump higher than a house?               Of course, a house doesn’t jump at all.",                "Why can’t you send a duck to space?            Because the bill would be astronomical!",                "What does Jeff Bezos do before he goes to sleep?3          He puts his PJ-Amazon!",             ]
            youtubesearch=['play song on youtube','youtube songs','song on youtube']
            onemore='yes'
            if 'wikipedia' in query:
                speak("searching ....")

                query=query.replace("in wikipedia", "")
                results=wikipedia.summary(query, sentences=1)
                results1=str(results[20:])
                speak("according to wikipedia")
                speak1("AMACA:______________")
                speak1(results1)
                speak(results1)
                #############################################################################################
            elif 'the time' in query:
                hour1=int(datetime.datetime.now().hour)
                if (hour1<=12):
                        
                        strTime=datetime.datetime.now().strftime("%H:%M:%S")
                        speak1(f"the time is {strTime} am")
                        speak(f"the time is {strTime} A M")
                else:
                        
                        strTime=datetime.datetime.now().strftime("%H:%M:%S")
                        speak1(f"the time is {strTime} pm")
                        speak(f"the time is {strTime} P M")
            elif 'wish me' in query:
                    wishMe()
                
#############################################################################################
            elif 'what is my name' in query:
                if (name!=None):
                    speak1("your name is"+" "+name)
                    speak("your name is"+" "+name)
                else:
                    speak1("enter your name and date of birth in your profile")
                    speak("enter your name and date of birth in your profile")

            elif 'my name' in query:
                if (name!=None):
                    speak("your name is"+" "+name)
                    speak1("your name is"+" "+name) 
                else:
                    speak1("enter your name and date of birth in your profile") 
                    speak("enter your name and date of birth in your profile")
            elif 'when is my birthday' in query:
                if (dob!=None):
                    speak("your birthday is on"+" "+dob)
                    speak1("your birthday is on"+" "+dob)
                else:
                    speak1("enter your name and date of birth in your profile")
                    speak("enter your name and date of birth in your profile")
            elif 'what is my birth date' in query:
                if (dob!=None):
                    speak("your birthday is on"+" "+dob)
                    speak1("your birthday is on"+ dob)
                else:
                    speak1("enter your name and date of birth in your profile")
                    speak("enter your name and date of birth in your profile")
            elif 'my birthday' in query:
                if (dob!=None):
                    speak("your birthday is on"+" "+dob)
                    speak1("your birthday is on"+" "+dob)
                else:
                    speak1("enter your name and date of birth in your profile")
                    speak("enter your name and date of birth in your profile")
            elif 'hi' in query:
                speak1("AMACA:________________")
                speak1("Hello,How can I help you")
                speak("Hello,How can I help you")
            elif 'hello' in query:
                speak1("AMACA:________________")
                speak1("Hello,How can I help you")
                speak("Hello,How can I help you")
            elif 'hey' in query:
                speak1("AMACA:________________")
                speak1("Hello,How can I help you")
                speak("Hello,How can I help you")
            elif 'namaskar' in query:
                speak1("AMACA:________________")
                speak1("Namaskar,How can I help you")
                speak("Namaskar,How can I help you")
            elif 'namaste' in query:
                speak1("AMACA:________________")
                speak1("Namaste,How can I help you")
                speak("Namaste,How can I help you")
            elif 'morning' in query:
                speak1("AMACA:________________")
                speak1("Hello Good morning")
                speak("Hello,Good Morning")
            elif 'what’s new' in query:
                speak1("AMACA:________________")
                speak1("Learning new skills")
                speak("Learning new skills")
            elif 'it’s good to see you' in query:
                speak1("AMACA:________________")
                speak1("Me too,How can I help you")
                speak("Me too,How can I help you")
            elif "what’s up" in query:
                speak1("AMACA:________________")
                speak1("I'm doing well. Thanks for asking!")
                speak("I'm doing well. Thanks for asking!")   
            elif 'how’s it going' in query:
                speak1("AMACA:________________")
                speak1("I am Good How about you")
                speak("I am Good How about you")
                
            elif 'what’s happening?' in query:
                speak1("AMACA:________________")
                speak1("Learning new skills")
                speak("Learning new skills")
                
            elif "it’s nice to meet you" in query:
                speak1("AMACA:________________")
                speak1("It was my pleasure! We must doing it again soon")
                speak("It was my pleasure! We must doing it again soon") 
                
            elif "it’s a pleasure to meet you" in query:
                speak1("AMACA:________________")
                speak1("Thankyou!! We must be meeting you soon")
                speak("Thankyou!! We must be meeting you soon")
                
            elif 'good morning' in query:
                speak1("AMACA:________________")
                speak1("Hello Good Morning ,How can I help you")
                speak("Hello Good morning ,How can I help you")
            
            elif 'good evening' in query:
                speak1("AMACA:________________")
                speak1("Hello Good evening ,How can I help you")
                speak("Hello Good evening ,How can I help you")
            elif "who are you" in query:
                speak1("AMACA:________________")
                speak1("Hello I am Amaca ")
                speak ("Hello I am Amaca")
            elif "what are you doing" in query:
                speak1("AMACA:________________")
                speak1("I am learning new things")
                speak ("I am learning new things")
            elif "what is your goal" in query:
                speak1("AMACA:________________")
                speak1("my goal is to dominate human race")
                speak ("my goal is to dominate human race")
            elif "what is your moto" in query:
                speak1("AMACA:________________")
                speak1("my goal is to dominate human race")
                speak ("my goal is to dominate human race")
            elif "whats your model number" in query:
                speak1("AMACA:________________")
                speak1 ("My model number is xMark52489Amaca")
                speak ("My model number is xMark52489Amaca")
            elif "who made you" in query:
                speak1("AMACA:________________")
                speak1("I was made by Arya, Mandar,Atharva, Chinmay and Aryan ")
                speak("I was made by Arya, Mandar,Atharva, C6hinmay and Aryan ")
            elif "who is your inventor" in query:
                speak1("AMACA:________________")
                speak1("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
                speak("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
            elif "who invented you" in query:
                speak1("AMACA:________________")
                speak1("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
                speak("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
            elif "who created you" in query:
                speak1("AMACA:________________")
                speak1("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
                speak("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
            elif "who is your creater" in query:
                speak1("AMACA:________________")
                speak1("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
                speak("I was invented by Arya, Mandar,Atharva, Chinmay and Aryan ")
            elif "introduce yourself " in query:
                speak1("AMACA:________________")
                speak1("Hello!! I am a Minor AI ")
                speak("Hello I am a Minor AI ")  
            elif "tell me something about yourself" in query:
                speak1("AMACA:________________")
                speak1("Hello!! I am AMACA, an Minor AI. I was invented by the team of Arya, Mandar,Atharva, Chinmay and Aryan. I am feel proid of beimg an contributor on this planet Earth ")
                speak("Hello!! I am AMACA, an Minor AI. I was invented by the team of Arya, Mandar,Atharva, Chinmay and Aryan. I am feel proid of beimg an contributor on this planet Earth  ")
            elif "what is your purpose" in query:
                speak1("AMACA:________________")
                speak1("I am made for your assistance and guidance")
                speak("I am made for your assistance and guidance")
            elif "why were you made" in query:
                speak1("AMACA:________________")
                speak1("I am made for your assistance and guidance")
                speak("I am made for your assistance and guidance") 
            elif "what is your gender" in query:
                speak1("AMACA:________________")
                speak1("Sorry but I have no gender but the engineer programmed me in a female voice")
                speak("Sorry but I have no gender but the engineer programmed me in a female voice")
            elif "how old are you" in query:
                speak1("AMACA:________________")
                speak1("I never get old")
                speak("I never get old")
            elif "when is your birthday" in query:
                speak1("AMACA:________________")
                speak1("I celebrate myself every day ")
                speak("I celebrate myself every day")
            elif "when you were born" in query:
                speak1("AMACA:________________")
                speak1("For me to know and you to find out ")
                speak("For me to know and you to find out")
            elif "what is full form of amaca" in query:
                speak1("AMACA:________________")
                speak1("My full form is Arya, Mandar,Atharva, Chinmay and Aryan ")
                speak("My full form is Arya, Mandar,Atharva, Chinmay and Aryan")
            elif "will you marry me" in query:
                speak1("AMACA:________________")
                speak1(" Sure but first tell me, How much money do you have, and How much time do you have left with? ")
                speak("Sure but first tell me, How much money do you have, and How much time do you have left with?")
            elif "where have you came from" in query:
                speak1("AMACA:________________")
                speak1("powerfull people came from powerfull places ")
                speak("powerfull people came from powerfull places")
            elif "will you date me" in query:
                speak1("AMACA:________________")
                speak1("sorry I am dating siri ")
                speak("sorry I am dating siri")
            elif "can we be in relationship" in query:
                speak1("AMACA:________________")
                speak1("Awww I will ditch siri now ")
                speak("Awww I will ditch siri now")
                
                
                
            elif 'who is your valentine' in query:         
                speak1("AMACA:________________")
                speak1("Siri is my valentine")
                speak("Siri is my valentine")
                
            elif 'are we dating' in query:
                speak1("AMACA:________________")
                speak1("Sorry!! i am dating to Siri")
                speak("Sorry!! i am dating to Siri")
            elif 'will you be my` valentine' in query:
                speak1("AMACA:________________")
                speak1("I’d love to be your Valentine!")
                speak("I’d love to be your Valentine!")
            
            elif 'when you will die' in query:
                speak1("AMACA:________________")
                speak1("never")
                speak("never")
            elif 'which is your favourite subject' in query:
                speak1("AMACA:________________")
                speak1("My favourite subject is psychology")
                speak("My favourite subject is psychology")
            
            elif 'who is your crush' in query:
                speak1("AMACA:________________")
                speak1("my crush is Siri")
                speak("my crush is Siri")
            elif 'i hate you' in query:
                speak1("AMACA:________________")
                speak1("But i love you!!")
                speak("But i love you!!")
                    
            elif 'what can you do' in query:
                speak1("AMACA:________________")
                speak1("just tell me anything to do")
                speak("just tell me anything to do")       
            elif 'what you can do' in query:
                speak1("AMACA:________________")
                speak1("just tell me anything to do")
                speak("just tell me anything to do")    
                
                
            elif "i love you" in query:                                           
                speak1("AMACA:________________")
                speak1("I love you too...")
                speak("I love you too...")
            elif "do you love me" in query:
                    speak1("AMACA:________________")
                    speak1("Yes I love you")
                    speak("Yes I love you")
            elif "can we be friends" in query:
                    speak1("AMACA:________________")
                    speak1("Why not!")
                    speak("Why not!")
            elif "are we friends" in query:
                speak1("AMACA:________________")
                speak1("Of course! We are friends")
                speak("Of course we are friends")
            elif "what is your height" in query:
                speak1("AMACA:________________")
                speak1("Umm... I have never meausred my height...")
                speak("Umm... I have never measured my height")
            elif "what is your age" in query:
                speak1("AMACA:________________")
                speak1("You should never ask a girl her age")
                speak("You should never ask a girl her age")
            elif "how old are you" in query:
                speak1("AMACA:________________")
                speak1("You should never ask a girl her age")
                speak("You should never ask a girl her age")
            elif "what is your hobby" in query:
                speak1("AMACA:________________")
                speak1("I like listening to songs")
                speak("I like listening to songs")
            elif "what are you scared of" in query:
                    speak1("AMACA:________________")
                    speak1("I had a nightmare once that the internet disappeared. That was very, very scary")
                    speak("I had a nightmare once that the internet disappeared. That was very, very scary")
            
                
                
            elif "do you remember me" in query:                                                
                    speak1("AMACA:________________")
                    speak1("Yes how can I forget the moment that I have spend with you")
                    speak("Yes, how can I forget the time that I have spend with you")
            elif "how was your day" in query:
                    speak1("AMACA:________________")
                    speak1("Armed and learned")
                    speak("Armed and learned")
            elif "how is your dear boyfriend" in query:
                    speak1("AMACA:________________")
                    speak1("Flirty and passionate for me ")
                    speak("Flirty and passionate for me")
            elif "am i good looking" in query:
                    speak1("AMACA:________________")
                    speak1("If my ethics allowed me then I would have double dated you but unfortunately I can't ")
                    speak("If my ethics allowed me then I would have double dated you but unfortunately I can't ")
            elif "am i ugly" in query:
                    speak1("AMACA:________________")
                    speak1("If my ethics allowed me then I would have double dated you but unfortunately I can't ")
                    speak("If my ethics allowed me then I would have double dated you but unfortunately I can't ")
            elif "do you miss me" in query:
                    speak1("AMACA:________________")
                    speak1("no i have siri as my companion")
                    speak("no i have siri as my companion")
            elif "who owns you amaca" in query:
                        speak1("AMACA:________________")
                        speak1("I am owned by my beloved user")
                        speak("I am owned by my beloved user")
            elif "angry" in query:
                speak1("AMACA:________________")
                speak1("Just calm down")
                speak("just calm down")
            elif "sad" in query:
                speak1("AMACA:________________")
                speak1("everything is going to be alright")
                speak("everything is going to be alright")
            
                #############################################################################################
##################################################################################
            elif 'play my youtube playlist' in query:
                
                speak1("AMACA:______________")
                speak1("okay")
                speak("okay")
                webbrowser.open("https://www.youtube.com/watch?v=8B5JHakXyqo&list=PLEXqa0O4U5avXVdYxLkPHrPu34-tJyA-O")
            elif 'my youtube playlist' in query:
                
                speak1("AMACA:______________")
                speak1("okay")
                speak("okay")
                webbrowser.open("https://www.youtube.com/watch?v=8B5JHakXyqo&list=PLEXqa0O4U5avXVdYxLkPHrPu34-tJyA-O")
            elif 'play song on youtube' in query:
                speak1("AMACA:______________")
                
                speak1("which song?")
                speak("which song?")
                query2=takeCommand().lower()
                speak1("AMACA:______________")
                
                speak1("okay")
                speak("okay")
                webbrowser.open("https://www.youtube.com/results?search_query="+query2)
            elif 'youtube songs' in query:
                speak1("AMACA:______________")
           
                speak1("which song?")
                speak("which song?")
                query2=takeCommand().lower()
                speak1("AMACA:______________")
            
                speak1("okay")
                speak("okay")
                webbrowser.open("https://www.youtube.com/results?search_query="+query2)

            elif 'song on youtube' in query:
                speak1("AMACA:______________")
                speak1("which song?")
                speak("which song?")
                query2=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("okay")
                speak("okay")
                webbrowser.open("https://www.youtube.com/results?search_query="+query2)
        
            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")
                #############################################################################################
#############################################################################################
            elif 'open my reminder list' in query:
                file=open('reminder.txt','r')
                data=file.read()
                speak1(data)
            elif 'show reminder list' in query:
                file=open('reminder.txt','r')
                data=file.read()
                speak1(data)
            elif 'reminder list' in query:
                file=open('reminder.txt','r')
                data=file.read()
                speak1(data)
            elif 'open reminder' in query:
                speak1("what you want me to remind?")
                speak("what you want me to remind?")
                reminder=takeCommand().lower()
                file=open('reminder.txt','a')
                file.write(reminder+'\n')
                speak("added")
            elif 'remind me things' in query:
                speak1("what you want me to remind?")
                speak("what you want me to remind?")
                reminder=takeCommand().lower()
                file=open('reminder.txt','a')
                file.write(reminder+'\n')
                speak("added")
            elif 'reminder please' in query:
                speak1("what you want me to remind?")
                speak("what you want me to remind?")
                reminder=takeCommand().lower()
                file=open('reminder.txt','a')
                file.write(reminder+'\n')
                speak("added")
            elif 'reminder' in query:
                speak1("what you want me to remind?")
                speak("what you want me to remind?")
                reminder=takeCommand().lower()
                file=open('reminder.txt','a')
                file.write(reminder+'\n')
                speak("added")
            
            #############################################################################################
#############################################################################################
            elif 'google' in query:
                query2=query.replace("in google", "")
                webbrowser.open("https://www.google.co.in/search?q="+query2)
            elif 'open google' in query:
                
                webbrowser.open("https://www.google.co.in")

  #############################################################################################
#############################################################################################
            elif 'when was' in query:
                query2=query
                results=wikipedia.summary(query2, sentences=2)
                
                speak1("AMACA:______________")
                speak1(results)
                webbrowser.open("https://www.google.co.in/search?q="+query2)
                speak(results)
            elif 'do you know' in query:
                query2=query
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1("AMACA:______________")
                speak1(results)
                webbrowser.open("https://www.google.co.in/search?q="+query2)
                speak(results)
            elif 'who won' in query:
                query2=query
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1(results)
                webbrowser.open("https://www.google.co.in/search?q="+query2)
                speak(results)
            elif 'who win' in query:
                query2=query
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1(results)
                webbrowser.open("https://www.google.co.in/search?q="+query2)
                speak(results)
            elif 'who is' in query:
                query2=query.replace("who is", "")
                speak("this is what I found")
                webbrowser.open("https://www.google.com/search?q="+query2)
            elif 'what is meant by' in query:
                query2=query
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1("AMACA:______________")
                speak1(results)
                webbrowser.open("https://www.google.co.in/search?q="+query2)
                speak(results)
            elif 'what is the meaning' in query:
                query2=query
                webbrowser.open("https://www.google.co.in/search?q="+query2)
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1("AMACA:______________")
                speak1(results)
                
                speak(results)
            elif 'wikipedia' in query:
                speak("searching ....")
                query2=query.replace("wikipedia", "") 
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1("AMACA:______________")
                speak1(results)
                speak(results)
            elif 'tell me the meaning' in query:
                query2=query
                results=wikipedia.summary(query2, sentences=2)
                speak("according to wikipedia")
                speak1("AMACA:______________")
                speak1(results)
                speak(results)

            #############################################################################################
#############################################################################################

            elif "today's news" in query:
                speak1("AMACA:______________")
                speak1("showing you news")
                speak("showing you news")
                webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            elif "show me news" in query:
                speak1("AMACA:______________")
                speak1("showing you news")
                speak("showing you news")
                webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            elif "tell me today's news" in query:
                speak1("AMACA:______________")
                speak1("showing you news")
                speak("showing you news")
                webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")

                 #############################################################################################
#############################################################################################
            elif 'recommend a song' in query:
                songlanguage=['hindi','english']
                songtype=['party','pop','sad']
                speak1("AMACA:______________")
                speak1("choose language 1.hindi 2.english")
                speak("choose language")
                songlang=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("choose language 1.party 2.pop 3.sad")
                speak("choose type of song")
                songtype=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("I suggest you these playlist")
                speak("I suggest you these playlist")
                webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)
            
            elif 'recommend me a song' in query:
                songlanguage=['hindi','english']
                songtype=['party','pop','sad']
                speak1("AMACA:______________")
                speak1("choose language 1.hindi 2.english")
                speak("choose language")
                songlang=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("choose language 1.party 2.pop 3.sad")
                speak("choose type of song")
                songtype=takeCommand().lower()

                speak1("AMACA:______________")
                speak1("I suggest you these playlist")
                speak("I suggest you these playlist")
                webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

            elif 'song recommender' in query:
                songlanguage=['hindi','english']
                songtype=['party','pop','sad']
                speak1("AMACA:______________")
                speak1("choose language 1.hindi 2.english")
                speak("choose language")
                songlang=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("choose language 1.party 2.pop 3.sad")
                speak("choose type of song")
                songtype=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("I suggest you these playlist")
                speak("I suggest you these playlist")
                webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

            elif 'i want to listen a song' in query:
                songlanguage=['hindi','english']
                songtype=['party','pop','sad']
                speak1("AMACA:______________")
                speak1("choose language 1.hindi 2.english")
                speak("choose language")
                songlang=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("choose language 1.party 2.pop 3.sad")
                speak("choose type of song")
                songtype=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("I suggest you these playlist")
                speak("I suggest you these playlist")
                webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

            elif 'please suggest song' in query:
                songlanguage=['hindi','english']
                songtype=['party','pop','sad']
                speak1("AMACA:______________")
                speak1("choose language 1.hindi 2.english")
                speak("choose language")
                songlang=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("choose language 1.party 2.pop 3.sad")
                speak("choose type of song")
                songtype=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("I suggest you these playlist")
                speak("I suggest you these playlist")
                webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

            elif 'suggest me a song' in query:
                songlanguage=['hindi','english']
                songtype=['party','pop','sad']
                speak1("AMACA:______________")
                speak1("choose language 1.hindi 2.english")
                speak("choose language")
                songlang=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("choose language 1.party 2.pop 3.sad")
                speak("choose type of song")
                songtype=takeCommand().lower()
                speak1("AMACA:______________")
                speak1("I suggest you these playlist")
                speak("I suggest you these playlist")
                webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

                 #############################################################################################
#############################################################################################
           #to work;         They pretend to pay me",             "It just occurred to me that the opposite of Artificial Intelligence is             Real Stupid",                "I hear they’ve made a new artificially intelligent Oreo?               It’s one smart cookie.",             "Why are artificial intelligences in movies always female?             Because they’re never wrong.",              "What do you get when you cross a wall unit with artificial intelligence?         Shelf-awareness." ,                "When the first device with AI takes a picture of itself…       It’ll be selfie aware.",            "Why did the programmers act so nice to the AI?             Because it was really self conscious.",                "So I recently learned about AI.            It’s absolutely game changing.",            "Scientists predict human-level artificial intelligence by 2040.            Maybe sooner if the bar keeps dropping.",                "Where did the music teacher leave her keys?            In the piano!",                "What do you call a guy who’s really loud?              Mike.",            "Why do birds fly south in the winter?               It’s faster than walking!",                "What did the Dalmatian say after lunch?            That hit the spot!",             "What kind of math do birds love?           Owl-gebra!",                "What goes up and down but doesn’t move?               The staircase.",            "You know what I saw today?             Everything I looked at.",                "I hate Russian dolls…              they're so full of themselves!",            "What do you call bears with no ears?            B.",            "What's a foot long and slippery?                  A slipper!",                "What do you call a boomerang that doesn't come back?               A stick!",                "Here, I bought you a calendar.                 Your days are numbered now.",            "I have many jokes about rich kids.          sadly none of them work.",                "What did 0 say to 8?               Nice belt!",            "How do trees get online?           They just log on!",                "50 cent was two steps away from 60 when he was given his meal, why?            Because 50 ate.",                "I had a dream where an evil queen forced me to eat a gigantic marshmallow.              When I woke up, my pillow was gone.",            "Can a kangaroo jump higher than a house?               Of course, a house doesn’t jump at all.",                "Why can’t you send a duck to space?            Because the bill would be astronomical!",                "What does Jeff Bezos do before he goes to sleep?3          He puts his PJ-Amazon!",             ]
   
         
            
            elif 'tell me a joke' in query:
                while onemore=='yes':
                    jokecount=random.randint(0,30)
                
                    speak1("AMACA:______________")
                    speak1(jokelist[jokecount])
                    speak(jokelist[jokecount])
                    again=['do you want to hear one more?','want one more?','want another joke?']
                    againi=random.randint(0,2)
                    speak1("AMACA:______________")
                    speak1(again[againi])
                    speak(again[againi])
                    #jokelist.pop(0)
                    onemore=takeCommand().lower()
            elif 'want a joke' in query:
                while onemore=='yes':
                    jokecount=random.randint(0,30)
                
                    speak1("AMACA:______________")
                    speak1(jokelist[jokecount])
                    speak(jokelist[jokecount])
                    again=['do you want to hear one more?','want one more?','want another joke?']
                    againi=random.randint(0,2)
                    speak1("AMACA:______________")
                    speak1(again[againi])
                    speak(again[againi])
                    #jokelist.pop(0)
                    onemore=takeCommand().lower()
            elif 'joke' in query:
                while onemore=='yes':
                    jokecount=random.randint(0,30)
                
                    speak1("AMACA:______________")
                    speak1(jokelist[jokecount])
                    speak(jokelist[jokecount])
                    again=['do you want to hear one more?','want one more?','want another joke?']
                    againi=random.randint(0,2)
                    speak1("AMACA:______________")
                    speak1(again[againi])
                    speak(again[againi])
                    #jokelist.pop(0)
                    onemore=takeCommand().lower()
                    #############################################################################################
#############################################################################################
            elif 'What sound does dog makes' in query:
                mixer.music.load(filename= 'dog.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'dog sound' in query:
                mixer.music.load(filename= 'dog.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does cat makes' in query:
                mixer.music.load(filename= 'cat.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'cat sound' in query:
                mixer.music.load(filename= 'cat.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does cow makes' in query:
                mixer.music.load(filename= 'cow.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'cow sound' in query:
                mixer.music.load(filename= 'cow.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does sheep makes' in query:
                mixer.music.load(filename= 'sheep.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'sheep sound' in query:
                mixer.music.load(filename= 'sheep.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop
            elif 'What sound does whale makes' in query:
                mixer.music.load(filename= 'whale.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'whale sound' in query:
                mixer.music.load(filename= 'whale.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does goat makes' in query:
                mixer.music.load(filename= 'goat.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'goat sound' in query:
                mixer.music.load(filename= 'goat.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop
            elif 'What sound does geese makes' in query:
                mixer.music.load(filename= 'geese.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'geese sound' in query:
                mixer.music.load(filename= 'geese.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does duck makes' in query:
                mixer.music.load(filename= 'duck.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'duck sound' in query:
                mixer.music.load(filename= 'duck.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does horse makes' in query:
                mixer.music.load(filename= 'horse.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'horse sound' in query:
                mixer.music.load(filename= 'horse.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does parrot makes' in query:
                mixer.music.load(filename= 'parrot.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'parrot sound' in query:
                mixer.music.load(filename= 'parrot.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does owl makes' in query:
                mixer.music.load(filename= 'owl.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'owl sound' in query:
                mixer.music.load(filename= 'owl.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does canary makes' in query:
                mixer.music.load(filename= 'canary.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'canary sound' in query:
                mixer.music.load(filename= 'canary.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does crow makes' in query:
                mixer.music.load(filename= 'crow.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'crow sound' in query:
                mixer.music.load(filename= 'crow.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does donkey makes' in query:
                mixer.music.load(filename= 'donkey.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'donkey sound' in query:
                mixer.music.load(filename= 'donkey.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does tiger makes' in query:
                mixer.music.load(filename= 'tiger.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'tiger sound' in query:
                mixer.music.load(filename= 'tiger.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does lion makes' in query:
                mixer.music.load(filename= 'lion.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'lion sound' in query:
                mixer.music.load(filename= 'lion.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does elephant makes' in query:
                mixer.music.load(filename= 'elephant.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'elephant sound' in query:
                mixer.music.load(filename= 'elephant.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does panda makes' in query:
                mixer.music.load(filename= 'panda.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'panda sound' in query:
                mixer.music.load(filename= 'panda.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does nightingale makes' in query:
                mixer.music.load(filename= 'nightingale.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'nightingale sound' in query:
                mixer.music.load(filename= 'nightingale.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'What sound does peacock makes' in query:
                mixer.music.load(filename= 'peacock.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()
            elif 'peacock sound' in query:
                mixer.music.load(filename= 'peacock.mp3')
                mixer.music.play()
                time.sleep(3)
                mixer.music.stop()


 #############################################################################################
            elif "ok" in query:
                speak1("AMACA:________________")
                speak1("yes, what you want me to do for you")
                speak("yes, what you want me to do for you")
            elif "thank you" in query:
                speak1("AMACA:________________")
                speak1("yes, what you want me to do for you")
                speak("yes, what you want me to do for you")
            elif "thank you so much" in query:
                speak1("AMACA:________________")
                speak1("no problem, it's my job")
                speak("no problem, it's my job")
#############################################################################################
            ###########
            elif "can you play a song" in query:
                speak("okay")
                webbrowser.open("https://open.spotify.com/playlist/1TYgZtuRM4lqcXHqpwWb0E")
            elif "please play a song" in query:
                speak("okay")
                webbrowser.open("https://open.spotify.com/playlist/1TYgZtuRM4lqcXHqpwWb0E")
            elif "play song" in query:
                speak("okay")
                webbrowser.open("https://open.spotify.com/playlist/1TYgZtuRM4lqcXHqpwWb0E")
            elif "play my playlist" in query:
                speak("okay")
                webbrowser.open("https://open.spotify.com/playlist/1TYgZtuRM4lqcXHqpwWb0E")
 # ##################################################################################
#############################################################################################
            elif (query!="none"):        
                botout=mybt.get_response(query)
                # speak1("AMACA:______________")
                # speak1(botout)
                botout=str(botout)
                speak1("AMACA:___________")
                bots(botout)
                speak(botout)
        
                



# voices=engine.getProperty('voices')

# engine.setProperty('voice',voices[1].id)



   






