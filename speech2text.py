
import pyaudio
from tkinter import *
import speech_recognition as sr 
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo,askokcancel
import threading

#>> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
#>> https://pypi.org/project/SpeechRecognition/
#>> https://pypi.org/project/PyAudio/


def speak():
    # initialize recognizer
    r = sr.Recognizer()            
    # mention source it will be either Microphone or audio files.     
    with sr.Microphone() as source: 
        text.delete('0.0',END)    
        text.insert(END,"Speak.....")
        print('speak ....')
         # listen to the source
        audio = r.listen(source)       
    try:
        # use recognizer to convert our audio into text part.
        audio_string = r.recognize_google(audio)    
        print("You said : {}".format(audio_string ))
        text.delete('0.0',END)
        text.insert(END,audio_string )
    except Exception as e:
        print(e,type(e))
        # In case of voice not recognized  clearly
        print("Sorry could not recognize your voice") 
        text.delete('0.0',END)
        text.insert(END, "Sorry could not recognize your voice")   

def call_speak():
    x = threading.Thread(target=speak)
    x.start()



def exit():
    if askokcancel('Comform Box','Do you really want to exit.'):
        root.quit()


root = Tk()
s = ttk.Style(root)
s.theme_use('clam')

root.geometry('425x400')
root.title("Speech To Text")

text = ScrolledText(root,width=36,height=15,bd=2, relief=RIDGE,
    wrap=WORD, font=('arial',14))
text.place(x=0,y=5)


ttk.Button(root,text='Speak',width=10,command=call_speak).place(x=70,y=350)
ttk.Button(root,text='Clear',width=10,command=lambda :text.delete('0.0',END)).place(x=170,y=350)
ttk.Button(root,text='Exit',width=10,command=exit).place(x=270,y=350)

root.mainloop()