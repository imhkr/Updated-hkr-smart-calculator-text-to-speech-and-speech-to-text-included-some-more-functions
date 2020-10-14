import sympy
from sympy import cot
from sympy import sec
from sympy import isprime
from sympy import primerange
import math
somemessage=["\n\n\n--------------WELCOME TO SMART CALCULATOR------------------","               MY NAME IS HKR    \n","    THANK YOU SO MUCH.HAVE A NICE DAY   \n","!!!!!!!!!!!!!!SORRY THIS IS BEYOND MY CAPACITY!!!!!!!!!!!!!"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return (l)
def lcm(l):
    a,b=l
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(l):
    a,b=l
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(l):
 return sum(l)
   
def sub(l):
    a,b=l
    return (a-b)
def multiply(l):
    t=1
    for i in range(len(l)):
        t=t*l[i]
    return (t)
def division(l):
    a,b=l
    return (a/b)
def smallest(l):
    return(min(l))
def largest(l):
     return(max(l))
def reminder(l):
    a,b=l
    return(a%b)
def FACTORIAL(l):
    a=l[0]
    return math.factorial(a)
def square(l):
    a=l[0]
    return(l*l)
def squareroot(l):
    a=l[0]
    return(math.sqrt(a))
def cube(l):
    a=l[0]
    return(a*a*a)
def sin(l):
    a=l[0]
    return(math.sin(a))
def cos(l):
    a=l[0]
    return (math.cos(a))
def tan(l):
    a=l[0]
    return (math.tan(a))
def cot(l):
    a=l[0]
    return (sympy.cot(a))
def sec(l):
    a=l[0]
    return (sympy.sec(a))
def primerange(l):
    a,b=l
    return (sympy.primerange(a,b))
def checkprime(l):
    a=l[0]
    print(list(sympy.prime(a)))
def isceil(l):
    a=l[0]
    return (math.ceil(a))
def isfloor(l):
    a=l[0]
    return (math.floor(a))
def degree(l):
    a=l[0]
    return (math.degrees(a))
def end():
    print(somemessage[2])
    input("Press Enter key to exit")
    exit()
def gcdd(l):
    a,b=l;
    return (math.gcd(a,b))
def myname():
    print(somemessage[1])
def sorry():
    print(somemessage[3])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"GCD":gcdd,"CEIL":isceil,"DEGREE":degree,"FLOOR":isfloor,"PRIMEFROM":primerange,"MINUS":sub,"SQRT":squareroot,"SEC":sec,"COT":cot,"CHECKPRIME":checkprime,"SIN":sin,"COS":cos,"TAN":tan,"SQUAREROOT":squareroot,"SQUARE":square,"sq":square,"CUBE":cube,"FACTORIAL":FACTORIAL,"FACT":FACTORIAL,"SUBTRACT":sub,"REMINDER":reminder,"MODULO":reminder,"MODULOS":reminder,"MOD":reminder,"SMALLEST":smallest,"MINIMUM":smallest,"LARGEST":largest,"MAXIMUM":largest,"SUBTRACTION":sub,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"INTO":multiply,"DIVIDE":division,"DIVISION":division,"DIVIDEBY":division,"DIVIDE BY":division,"LCM":lcm,"HCF":hcf}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}
