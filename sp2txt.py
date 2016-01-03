#coding: utf-8

import speech_recognition as sr
import sys

class sp2txt:
    def __init__(self):
        """ Initialize """
        self.recognizer = sr.Recognizer()
  
    def read_wave(self, wav):
        """ Open Wave Sound """
        with sr.WavFile(wav) as source:
            return self.recognizer.record(source)
    
    def translate(self, audio):
        """ Try speech recognition by IBM Bluemix Speech To Text-ew API """
        try:
            return ("%s\b.") % self.recognizer.recognize_ibm(
                    audio,
                    username="your id",
                    password="your pass") 
        
        except LookupError:
            return ("Could not understand audio")

if __name__ == '__main__':
    r = sp2txt()

    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        filepath = sys.stdin.read().splitlines()
    else:
        del argvs[0]
        filepath = argvs

    for filename in filepath:
        audio = r.read_wave(filename)
        print r.translate(audio)
