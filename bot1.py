from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot import trainers
import pyttsx3
import speech_recognition as sr
import os

def s(command):
    
    engine=pyttsx3.init()
    engine.say(command,178)
    engine.runAndWait()
# voices=engine.getProperty('voices')

# engine.setProperty('voice',voices[1].id)
mybt=ChatBot("Amaca",storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3')
trainw=ChatterBotCorpusTrainer(mybt)
trainw.train('chatterbot.corpus.english')


while True:
     
        botin=input('>')
        botout=mybt.get_response(botin)
        # speak1(botout)
        s(botout)
       