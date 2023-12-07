







############################################################################################# 
#############################################################################################

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import tkinter
# from pygame import mixer
import random

############################################################################################# 
#############################################################################################

engine=pyttsx3.init()


#############################################################################################
#############################################################################################

#speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
#############################################################################################
#############################################################################################

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold*1
        audio=r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"{query}\n",)
    except Exception as e:
        #print(e)
        print("could'nt recognize say it again please...")
        return "none"
    return query

#############################################################################################
#############################################################################################

def wishMe():
    hour=int(datetime.datetime.now().hour)
    mini=int(datetime.datetime.now().minute)
 
    if hour>=0 and hour<12:
        print("good morning")
        speak("good morning")     
    elif hour>=12 and hour<18:
        print("good afternoon")
        speak("good afternoon")    
    else:
        print("good evening")
        speak("good evening")
        
#############################################################################################
#############################################################################################
    
#time fuction when user asks for time related things    
def Time():
    hour1=int(datetime.datetime.now().hour)
   
    if 'the time' in query:
        if (hour1<=12):
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime} am")
            speak(f"the time is {strTime} A M")
        else:
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime} pm")
            speak(f"the time is {strTime} P M")
    elif 'wish me' in query:
        wishMe()
        
#############################################################################################
#############################################################################################

def youtube():
    youtubesearch=['play song on youtube','youtube songs','song on youtube']
    if query in youtubesearch:
        print("which song?")
        speak("which song?")
        query2=takeCommand().lower()
        print("okay")
        speak("okay")
        webbrowser.open("https://www.youtube.com/results?search_query="+query2)
        
    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
    return a
        
#############################################################################################
#############################################################################################
          
def google():
    if 'google' in query:
        query2=query.replace("in google", "")
        webbrowser.open("https://www.google.co.in/search?q="+query2)
    elif 'open google' in query:
        
        webbrowser.open("https://www.google.co.in")
#############################################################################################
#############################################################################################

def info():
    if 'when was' in query:
        query2=query
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    if 'who won' in query:
        query2=query
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    
    elif 'who is the' in query:
        query2=query
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'what is meant by' in query:
        query2=query
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'what is the meaning' in query:
        query2=query
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'wikipedia' in query:
        speak("searching ....")
        query2=query.replace("wikipedia", "") 
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'tell me the meaning' in query:
        query2=query
        results=wikipedia.summary(query2, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    
#############################################################################################
#############################################################################################

def startstop():
    if 'start' in query:
        print("yes sure tell me what i can do for you")
        speak("yes sure tell me what i can do for you")
    elif 'lets start' in query:
        print("yes sure tell me what i can do for you")
        speak("yes sure tell me what i can do for you")
    elif 'lets begin' in query:
        print("yes sure tell me what i can do for you")
        speak("yes sure tell me what i can do for you")
    elif 'do stuff for me' in query:
        print("yes sure tell me what i can do for you")
        speak("yes sure tell me what i can do for you")
    elif 'stop' in query:
        print("as you say, see you soon")
        speak("as you say, see you soon")
        return a==False
    elif 'shut up' in query:
        print("as you say, see you soon")
        speak("as you say, see you soon")
        return a==1
    elif 'shut the fuck up' in query:
        print("as you say, see you soon")
        speak("as you say, see you soon")
        return a==1
    elif 'end this' in query:
        print("as you say, see you soon")
        speak("as you say, see you soon")
        return a==1
        
#############################################################################################
#############################################################################################

def news():
    if "today's news" in query:
        print("showing you news")
        speak("showing you news")
        webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
    elif "show me news" in query:
        print("showing you news")
        speak("showing you news")
        webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
    elif "tell me today's news" in query:
        print("showing you news")
        speak("showing you news")
        webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
        
        
#############################################################################################
############################################################################################# 


def songrecommendor():
    
    if 'recommend a song' in query:
        songlanguage=['hindi','english']
        songtype=['party','pop','sad']
        print("choose language 1.hindi 2.english")
        speak("choose language")
        songlang=takeCommand().lower()
        print("choose language 1.party 2.pop 3.sad")
        speak("choose type of song")
        songtype=takeCommand().lower()
        print("I suggest you these playlist")
        speak("I suggest you these playlist")
        webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)
    
    elif 'recommend me a song' in query:
        songlanguage=['hindi','english']
        songtype=['party','pop','sad']
        print("choose language 1.hindi 2.english")
        speak("choose language")
        songlang=takeCommand().lower()
        print("choose language 1.party 2.pop 3.sad")
        speak("choose type of song")
        songtype=takeCommand().lower()

        print("I suggest you these playlist")
        speak("I suggest you these playlist")
        webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

    elif 'song recommender' in query:
        songlanguage=['hindi','english']
        songtype=['party','pop','sad']
        print("choose language 1.hindi 2.english")
        speak("choose language")
        songlang=takeCommand().lower()
        print("choose language 1.party 2.pop 3.sad")
        speak("choose type of song")
        songtype=takeCommand().lower()
        print("I suggest you these playlist")
        speak("I suggest you these playlist")
        webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

    elif 'i want to listen a song' in query:
        songlanguage=['hindi','english']
        songtype=['party','pop','sad']
        print("choose language 1.hindi 2.english")
        speak("choose language")
        songlang=takeCommand().lower()
        print("choose language 1.party 2.pop 3.sad")
        speak("choose type of song")
        songtype=takeCommand().lower()
        print("I suggest you these playlist")
        speak("I suggest you these playlist")
        webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

    elif 'please suggest song' in query:
        songlanguage=['hindi','english']
        songtype=['party','pop','sad']
        print("choose language 1.hindi 2.english")
        speak("choose language")
        songlang=takeCommand().lower()
        print("choose language 1.party 2.pop 3.sad")
        speak("choose type of song")
        songtype=takeCommand().lower()
        print("I suggest you these playlist")
        speak("I suggest you these playlist")
        webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)

    elif 'suggest me a song' in query:
        songlanguage=['hindi','english']
        songtype=['party','pop','sad']
        print("choose language 1.hindi 2.english")
        speak("choose language")
        songlang=takeCommand().lower()
        print("choose language 1.party 2.pop 3.sad")
        speak("choose type of song")
        songtype=takeCommand().lower()
        print("I suggest you these playlist")
        speak("I suggest you these playlist")
        webbrowser.open("https://open.spotify.com/search/"+songlang+"%20"+songtype)
    return a==1
        
#############################################################################################
#############################################################################################
# def hbd():
   
#     if 'wish me birthday' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif "it's my birthday" in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif 'today is my birthday' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif 'play birthday song' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
    
        
        
#############################################################################################
#############################################################################################


# def offsong():
  
#     if 'play song' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif 'please play a song' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif 'listen song' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif 'song for me' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()

#     elif 'offline song' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
#     elif 'play offline song' in query:
         

#         mixer.init()
#         mixer.music.load('C:\\Users\\athar\\Downloads\\birthday.mp3')
#         mixer.music.play()
             
#############################################################################################
#############################################################################################

def jokes():
    jokelist=["One joke, coming up! What is a sea monsters favorite snack?           Ships and dip.",              "How do robots eat guacamole?                With computer chips.",             "What happens to a lawyer who jumps out of a plane at 35,000 feet without a parachute?         Who cares?",             "How can you tell when a lawyer is lying?              His lips are moving.",             "I pretend to work;         They pretend to pay me",             "It just occurred to me that the opposite of Artificial Intelligence is             Real Stupid",                "I hear they’ve made a new artificially intelligent Oreo?               It’s one smart cookie.",             "Why are artificial intelligences in movies always female?             Because they’re never wrong.",              "What do you get when you cross a wall unit with artificial intelligence?         Shelf-awareness." ,                "When the first device with AI takes a picture of itself…       It’ll be selfie aware.",            "Why did the programmers act so nice to the AI?             Because it was really self conscious.",                "So I recently learned about AI.            It’s absolutely game changing.",            "Scientists predict human-level artificial intelligence by 2040.            Maybe sooner if the bar keeps dropping.",                "Where did the music teacher leave her keys?            In the piano!",                "What do you call a guy who’s really loud?              Mike.",            "Why do birds fly south in the winter?               It’s faster than walking!",                "What did the Dalmatian say after lunch?            That hit the spot!",             "What kind of math do birds love?           Owl-gebra!",                "What goes up and down but doesn’t move?               The staircase.",            "You know what I saw today?             Everything I looked at.",                "I hate Russian dolls…              they're so full of themselves!",            "What do you call bears with no ears?            B.",            "What's a foot long and slippery?                  A slipper!",                "What do you call a boomerang that doesn't come back?               A stick!",                "Here, I bought you a calendar.                 Your days are numbered now.",            "I have many jokes about rich kids.          sadly none of them work.",                "What did 0 say to 8?               Nice belt!",            "How do trees get online?           They just log on!",                "50 cent was two steps away from 60 when he was given his meal, why?            Because 50 ate.",                "I had a dream where an evil queen forced me to eat a gigantic marshmallow.              When I woke up, my pillow was gone.",            "Can a kangaroo jump higher than a house?               Of course, a house doesn’t jump at all.",                "Why can’t you send a duck to space?            Because the bill would be astronomical!",                "What does Jeff Bezos do before he goes to sleep?           He puts his PJ-Amazon!",             ]
   
    onemore='yes'
    
    if 'tell me a joke' in query:
        while onemore=='yes':
            jokecount=random.randint(0,30)
        
            print(jokelist[jokecount])
            speak(jokelist[jokecount])
            again=['do you want to hear one more?','want one more?','want another joke?']
            againi=random.randint(0,2)
            print(again[againi])
            speak(again[againi])
            #jokelist.pop(0)
            onemore=takeCommand().lower()
    elif 'want a joke' in query:
        while onemore=='yes':
            jokecount=random.randint(0,30)
        
            print(jokelist[jokecount])
            speak(jokelist[jokecount])
            again=['do you want to hear one more?','want one more?','want another joke?']
            againi=random.randint(0,2)
            print(again[againi])
            speak(again[againi])
            #jokelist.pop(0)
            onemore=takeCommand().lower()
    elif 'joke' in query:
        while onemore=='yes':
            jokecount=random.randint(0,30)
        
            print(jokelist[jokecount])
            speak(jokelist[jokecount])
            again=['do you want to hear one more?','want one more?','want another joke?']
            againi=random.randint(0,2)
            print(again[againi])
            speak(again[againi])
            #jokelist.pop(0)
            onemore=takeCommand().lower()
    
            
#############################################################################################
#############################################################################################
__name__="__main__"

if __name__=="__main__":
 

    
    wishMe()
    print("AMACA here")
    speak("AMACA here")
    a=0
    
    while a==0:
        
        query=takeCommand().lower()
        
        
        Time()
        
        
        google()
        
        
        news()
        
        
        youtube()
        
        
        info()
        
        
        jokes()
        
        songrecommendor()
        
        
        startstop()
        
        
        
       
 
   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



 


# In[ ]:





# In[ ]:




