import time
import speech_recognition as s
import tkinter as tk
from tkinter import *
import pyttsx3 as pp
engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(word):
    engine.say(word)
    engine.runAndWait()
hkr_root=tk.Tk()
hkr_root.maxsize(600,1000)
hkr_root.minsize(600,1000)
hkr_root.geometry("600x1000")
#def ADD():
 #   print("enter two value")
  #  n=int(input())
   # n2=int(input())
   # print(n+n2)
#def divide():
 #   print("this is divide")
#hkr_root.title=Label(text="HKR SMART CALCULATOR")
#//hkr_root.title.pack()
#hkr_label=Label(text="Hello this is hkr smart clci",font="comicsansms 40",bg="red",fg="black",relief=RIDGE)
#photo=PhotoImage(file="himanshu.png")
#photo_label=Label(image=photo)

#f1=Frame(hkr_root,bg="grey",borderwidth="19",relief=GROOVE)
#f1.pack(side=TOP,anchor="nw")
#b1=Button(hkr_root,fg="red",text="TO ADD",command=ADD)
#b1.pack(side=TOP,padx=9,anchor="nw")
#b2=Button(hkr_root,fg="red",text="TO divide",command=divide)
#b2.pack(side=TOP,padx=9,anchor="nw")
#f2=Frame(hkr_root,bg="purple",borderwidth="19",relief=GROOVE)
#f2.pack(side=LEFT,fill="y")
#l1=Label(f2,text="Hello this is left side")
#l1.pack()
title_label=Label(text="WELCOME TO SMART CALCULATOR",bg="gold",fg="black",font="comicsansms 22 bold",padx=15,pady=5,relief=GROOVE).grid(column=0)
titlen11_label=Label(text="\n")
titlen11_label.grid(column=0)
#title_label
#photo_label.pack()
#hkr_label.pack()
import sympy
from sympy import cot
from sympy import sec
from sympy import isprime
from sympy import primerange
import math

somemessage = ["\n\n\n     --------------WELCOME TO SMART CALCULATOR------------------    ",
               "                      MY NAME IS HKR    \n", "    THANK YOU SO MUCH.HAVE A NICE DAY   \n",
               "!!!!!!!!!!!!!!SORRY THIS IS BEYOND MY CAPACITY!!!!!!!!!!!!!\n","\n                        Sorry i am not supposed to answer this question:)\n" ,"\n                I am developed by a human"]


def extract_numbers_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return (l)


def lcm(l):
    a, b = l
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def hcf(l):
    a, b = l
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


def add(l):
    return sum(l)


def sub(l):
    a, b = l
    return (a - b)


def multiply(l):
    t = 1
    for i in range(len(l)):
        t = t * l[i]
    return (t)


def division(l):
    a, b = l
    return (a / b)


def smallest(l):
    return (min(l))


def largest(l):
    return (max(l))


def reminder(l):
    a, b = l
    return (a % b)
def percent(l):
    a,b=l
    re=((a/100)*b)
    return re


def FACTORIAL(l):
    a = l[0]
    return math.factorial(a)


def square(l):
    a = l[0]
    return (a * a)


def squareroot(l):
    a = l[0]
    return (math.sqrt(a))


def cube(l):
    a = l[0]
    return (a * a * a)


def sin(l):
    a = l[0]
    return (math.sin(a))


def cos(l):
    a = l[0]
    return (math.cos(a))


def tan(l):
    a = l[0]
    return (math.tan(a))


def cot(l):
    a = l[0]
    return (sympy.cot(a))


def sec(l):
    a = l[0]
    return (sympy.sec(a))


def primerange(l):
    a, b = l
    return (sympy.primerange(a, b))


def checkprime(l):
    a = l[0]
    print(list(sympy.prime(a)))


def isceil(l):
    a = l[0]
    return (math.ceil(a))


def isfloor(l):
    a = l[0]
    return (math.floor(a))


def degree(l):
    a = l[0]
    return (math.degrees(a))


def end():
    print(somemessage[2])
    input("Press Enter key to exit")
    exit()


def gcdd(l):
    a, b = l;
    return (math.gcd(a, b))
def permutation(l):
    a,b=l
    re=(sympy.factorial(a)/(sympy.factorial(a-b)))
    print("          |----------------------------------|")
    print("          |       FORMULA FOR PERMUTATION    |")
    print("          | <------------------------------> |")
    print("          |           f(a)                   |")
    print("          |          -------                 | ")
    print("          |          (a-b)f                  | ")
    print("          |                                  |    ")
    print("          |NOTE:f Denote's Factorial         | ")
    print("          |----------------------------------| \n")
    return int(re)
def combination(l):
    a,b=l
    re=(sympy.factorial(a)/(sympy.factorial(b)*sympy.factorial(a-b)))
    return int(re)

def myname():
    print(somemessage[1])

def old():
    print(somemessage[4])
def sorry():
    print(somemessage[3])
def devlop():
    print(somemessage[5])


operations = {"+":add,"PLUS": add, "ADD": add, "ADDITION": add, "SUM": add, "GCD": gcdd, "CEIL": isceil, "DEGREE": degree,
              "FLOOR": isfloor, "PRIMEFROM": primerange, "MINUS": sub, "SQRT": squareroot, "SEC": sec, "COT": cot,
              "CHECKPRIME": checkprime, "SIN": sin, "COS": cos, "TAN": tan, "SQUAREROOT": squareroot, "SQUARE": square,
              "sq": square, "CUBE": cube, "FACTORIAL": FACTORIAL, "FACT": FACTORIAL, "SUBTRACT": sub,
              "REMINDER": reminder, "MODULO": reminder, "MODULOS": reminder, "MOD": reminder, "SMALLEST": smallest,
              "MINIMUM": smallest, "LARGEST": largest, "MAXIMUM": largest, "SUBTRACTION": sub, "MULTIPLY": multiply,
              "MULTIPLICATION": multiply, "INTO": multiply, "DIVIDE": division, "DIVISION": division,
              "DIVIDEBY": division, "DIVIDE BY": division, "LCM": lcm, "HCF": hcf,"PERCENT":percent,"%":percent,"PERMUTATION":permutation,"PERMU":permutation,"PARMU":permutation,"PR":permutation,"COMBINATION":combination,"COMBI":combination,"CB":combination}
commands = {"NAME": myname, "END": end, "EXIT": end, "CLOSE": end,"DEVELOPED":devlop,"MADE":devlop,"CREATED":devlop,"AGE":old,"OLD":old}


#import sys
#sys.path.append('/mymodules/')
#import mymodules
#from mymodules.calculation import *
def gettheoutput():
    print(somemessage[0])
    print(somemessage[1])
    sr = s.Recognizer()
    while True:
        time.sleep(1)
        print()
        print("Please tell me your query sir or mam")
        with s.Microphone() as m:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            text=query
       # text = input("enter your query here->>>>\t")
        for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                    l = extract_numbers_from_text(text)
                    r = operations[word.upper()](l)
                    speak(r)
                    print("|--------------------------------|")
                    print("|                                |")
                    print("| YOUR ANSWER IS HERE ->> ",r, " |")
                    print("|                                |")
                    print("|--------------------------------|")
                except:
                    print("Sorry retry ")
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
        else:
            sorry()
  #  goto while True:
value=Label(hkr_root,text="Please click on start button",font="comicsansms 16",bg="teal")
value.grid(column=0)
#addvalue=StringVar
#getinput=Entry(hkr_root,textvariable=addvalue)
#getinput.grid(row=0,column=1)
titlen_label=Label(text="\n")
titlen_label.grid(column=0)
Button(hkr_root,text="Start",command=gettheoutput,font="comicsansms 15",fg="red").grid(column=0)
titlen_label=Label(text="\n")
titlen_label.grid(column=0)
#l=Label(text="NOTE:",font="comicsansms 19 ",bg="red",pady=24)
#l.grid(row=4,column=0)

l=Label(text="!ATTENTION!  PLEASE PRESS START BUTTON AND THEN ENTER YOUR QUERY.\n",font="comicsansms 11 ",bg="sky blue",fg="RED",relief=RIDGE)
l.grid(column=0,sticky=tk.NSEW)

title1_label=Label(text=''' ->>YOU CAN WRITE YOUR QUERY IN THIS FORM.\n->>HEY HKR CAN YOU ADD 2 AND 5.\n->>HEY CAN YOU FIND THE GCD OF N OR N NO.\n->>FIND THE VALUE OF COS 90.\n->>ADD 5 6 753 344 AND 234 FOR ME.\n->>ETC\n''',bg="white",fg="brown",font="comicsansms 13")
title1_label.grid(column=0)
#titlen2_label=Label(text="\n")
#titlen2_label.grid()
titlen11_label=Label(text="\n")
titlen11_label.grid(column=0)
l1=Label(text="FEATURES(CAN BE USE TO FIND)",font="comicsansms 14 ",bg="lime")
l1.grid(column=0,sticky=tk.NS)
#l1.pack(side=LEFT)
#titlen_label=Label(text="\n")
#titlen_label.grid(column=4)

title1_label=Label(text="\n -------UNDERSTAND ALLMOST ALL LANGUAGE----- \n ",bg="WHITE",fg="red",font="comicsansms 11 bold")
title1_label.grid(column=0)
title1_label=Label(text=''' ->>ADDITION \n ->>SUBTRACTION \n ->> DIVISION \n ->>MULTIPLICATION\n ->>DEGREE \n ->>TRIGONOMETRY VALUES OF SIN ,COS,TAN,COT,SEC\n ->>NUMBER IS PRIME OR NOT \n ->>SQAURE ROOT\n ->>CUBE\n ->>SQAURE\n ->>HCF\n ->>AND MANY MORE''',bg="WHITE",fg="navy",font="comicsansms 11")
title1_label.grid(column=0)
hkr_root.mainloop()