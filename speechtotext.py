# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:27:26 2019

@author: soura
"""

import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something :')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    
    except:
        print('Sorry, could not recognize your voice')
        