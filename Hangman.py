import easygui
import random
import requests as requests
import sys
HangmanTITLE="HangmanTITLE.gif"
sysMENU=0
while sysMENU==0:
    MENU=easygui.enterbox("Welcome to Hangman.  Type S to Start, H for Help and Q to Quit","Hangman",image=HangmanTITLE)
    if MENU=="H" or MENU=="h":
        Help=easygui.msgbox("The description of Hangman is as follows:   The computer thinks of a word and the user(s) try to guess it by suggesting letters, within a certain number of guesses.","Hangman")      
    if MENU=="s" or MENU=="S":
        sysMENU=1        
    if MENU=="q" or MENU=="Q":
        sys.exit(0)
loop=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0
I=0
J=0
K=0
L=0
M=0
N=0
O=0
P=0
Q=0
R=0
S=0
T=0
U=0
V=0
W=0
X=0
Y=0
Z=0
difficultyimage="diff.gif"
msg= "Type a letter that you think is in the word or type the word you want to guess      "
quitter=""
invalidcharacters=0
youmusttype=0
guessed=[""]
WordSite = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
SameReply=0
VictoriousMsg="Congratulations you have won hangman."
Vict= "Vict.gif"
loser= "loser.gif"
image1= "hangman_default_0.gif"
image2= "hangman head 1.gif"
image3= "hangman body 2.gif"
image4= "hangman left leg 3.gif"
image5= "hangman both legs 4.gif"
image6= "hangman left arm 5.gif"
image7= "hangman complete 6.gif"
OLDreply="qwerfghjjhgfds"
reply="fgvbgjnjkhj"
Victory=0
length=0
VictoryMsg=""
loss= "Sorry you have lost type r to play, if you do not want to play again just press enter."
SameLetter=" (You put the same letter as last time)"
noreply="(You didn't type a reply you must type a letter)"
invalidcharacters="(You typed an invalid character you must type a letter)"
mainloop=1
while mainloop==1:
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    r=0
    s=0
    t=0
    u=0
    v=0
    w=0
    x=0
    y=0
    z=0
    A=0
    B=0
    C=0
    D=0
    E=0
    F=0
    G=0
    H=0
    I=0
    J=0
    K=0
    L=0
    M=0
    N=0
    O=0
    P=0
    Q=0
    R=0
    S=0
    T=0
    U=0
    V=0
    W=0
    X=0
    Y=0
    Z=0
    Victory=0
    Life=7
    loop=0
    difficulty=""
    word=""
    while difficulty!="Easy" and difficulty!="easy" and difficulty!="medium" and difficulty!="Medium" and difficulty!="Hard" and difficulty!="hard":
        difficulty=easygui.enterbox("Indicate what difficulty you would like the game on by typing either easy medium or hard","Hangman",image=difficultyimage)
    if difficulty=="Hard" or difficulty=="hard":
        while len(word)<9:
            response = requests.get(WordSite)
            WORDS = response.content.splitlines()
            word=random.choice(WORDS)
            word=str(word)
            word=(word.replace("b", ""))
            word=(word.replace("'", ""))
            word=(word.replace("'", ""))
    if difficulty=="Medium" or difficulty=="medium":
        while len(word)<6 or len(word)>=10:
            response = requests.get(WordSite)
            WORDS = response.content.splitlines()
            word=random.choice(WORDS)
            word=str(word)
            word=(word.replace("b", ""))
            word=(word.replace("'", ""))
            word=(word.replace("'", ""))
    if difficulty=="Easy" or difficulty=="easy":
        while len(word)<3 or len(word)>=7:
            response = requests.get(WordSite)
            WORDS = response.content.splitlines()
            word=random.choice(WORDS)
            word=random.choice(WORDS)
            word=str(word)
            word=(word.replace("b", ""))
            word=(word.replace("'", ""))
            word=(word.replace("'", ""))
    display=word
    word1=word
    while loop==0:
        display=word
        blank=" "
        display=blank.join(display)
        if q==0 and Q==0:
            display=display.replace("q","_")
            display=display.replace("Q","_")
        if w==0 and W==0:
            display=display.replace("w","_")
            display=display.replace("W","_")
        if e==0 and E==0:
            display=display.replace("e","_")
            display=display.replace("E","_")
        if r==0 and R==0:
            display=display.replace("r","_")
            display=display.replace("R","_")
        if t==0 and T==0:
            display=display.replace("t","_")
            display=display.replace("T","_")
        if y==0 and Y==0:
            display=display.replace("y","_")
            display=display.replace("Y","_")
        if u==0 and U==0:
            display=display.replace("u","_")
            display=display.replace("U","_")
        if i==0 and I==0:
            display=display.replace("i","_")
            display=display.replace("I","_")
        if o==0 and O==0:
            display=display.replace("o","_")
            display=display.replace("O","_")
        if p==0 and P==0:
            display=display.replace("p","_")
            display=display.replace("P","_")
        if a==0 and A==0:
            display=display.replace("a","_")
            display=display.replace("A","_")
        if s==0 and S==0:
            display=display.replace("s","_")
            display=display.replace("S","_")
        if d==0 and D==0:
            display=display.replace("d","_")
            display=display.replace("D","_")
        if f==0 and F==0:
            display=display.replace("f","_")
            display=display.replace("F","_")
        if g==0 and G==0:
            display=display.replace("g","_")
            display=display.replace("G","_")
        if h==0 and H==0:
            display=display.replace("h","_")
            display=display.replace("H","_")
        if j==0 and J==0:
            display=display.replace("j","_")
            display=display.replace("J","_")
        if k==0 and K==0:
            display=display.replace("k","_")
            display=display.replace("K","_")
        if l==0 and L==0:
            display=display.replace("l","_")
            display=display.replace("L","_")
        if z==0 and Z==0:
            display=display.replace("z","_")
            display=display.replace("Z","_")
        if x==0 and X==0:
            display=display.replace("x","_")
            display=display.replace("X","_")
        if c==0 and C==0:
            display=display.replace("c","_")
            display=display.replace("C","_")
        if v==0 and V==0:
            display=display.replace("v","_")
            display=display.replace("V","_")
        if b==0 and B==0:
            display=display.replace("b","_")
            display=display.replace("B","_")
        if n==0 and N==0:
            display=display.replace("n","_")
            display=display.replace("N","_")
        if m==0 and M==0:
            display=display.replace("m","_")
            display=display.replace("M","_")
                         
        invalidcharacters=0
        youmusttype=0
        miniloop=1
        if word1=="":
                Victory=1
                loop=1
                miniloop=0
            #Changes image to show proper life
        while miniloop==1:
            ProperReply=True
            if Life==7:
                reply= easygui.enterbox(msg+display+"    You have 7 lives left","Hangman",image=image1)
            if Life==6:
                reply= easygui.enterbox(msg+display+"    You have 6 lives left","Hangman",image=image2)
            if Life==5:
                reply= easygui.enterbox(msg+display+"    You have 5 lives left","Hangman",image=image3)
            if Life==4:
                reply= easygui.enterbox(msg+display+"    You have 4 lives left","Hangman",image=image4)
            if Life==3:
                reply= easygui.enterbox(msg+display+"    You have 3 lives left","Hangman",image=image5)
            if Life==2:
                reply= easygui.enterbox(msg+display+"    You have 2 lives left","Hangman",image=image6)
            if Life==1:
                reply= easygui.enterbox(msg+display+"    You have 1 lives left","Hangman",image=image7)


            #Checking for invalid inputs
                
            if Life==1 or Life==2 or Life==3 or Life==4 or Life==5 or Life==6 or Life==7:
                guessed.append(reply)

            if reply=="":
                ProperReply=False
                youmusttype=1
                loop=1
                miniloop=0
                
            if Life==0:
                loop=1
                ProperReply=False
                miniloop=0
                
            invalidcharacters=0 
            if reply not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
                ProperReply=False
                invalidcharacters=1
                
            SameReply=0
            if reply in OLDreply:
                ProperReply=False
                SameReply=1
                
            if reply not in word1 and ProperReply==True:
                Life-=1
                miniloop=0
                
                OLDreply=reply
            if len(reply)>1:
                while reply in word1:
                    word1=(word1.replace(reply,""))
                    miniloop=0
                
            if len(reply)==1:
                while reply in word1:
                    word1=(word1.replace(reply,""))
                    OLDreply=reply
                    miniloop=0
                    if reply=="a":
                        a=1
                    if reply=="b":
                        b=1
                    if reply=="c":
                        c=1
                    if reply=="d":
                        d=1
                    if reply=="e":
                        e=1
                    if reply=="f":
                        f=1
                    if reply=="g":
                        g=1
                    if reply=="h":
                        h=1
                    if reply=="i":
                        i=1
                    if reply=="j":
                        j=1
                    if reply=="k":
                        k=1
                    if reply=="l":
                        l=1
                    if reply=="m":
                        m=1
                    if reply=="n":
                        n=1
                    if reply=="o":
                        o=1
                    if reply=="p":
                        p=1
                    if reply=="q":
                        q=1
                    if reply=="r":
                        r=1
                    if reply=="s":
                        s=1
                    if reply=="t":
                        t=1
                    if reply=="u":
                        u=1
                    if reply=="v":
                        v=1
                    if reply=="w":
                        w=1
                    if reply=="x":
                        x=1
                    if reply=="y":
                        y=1
                    if reply=="z":
                        z=1
                    if reply=="A":
                        A=1
                    if reply=="B":
                        B=1
                    if reply=="C":
                        C=1
                    if reply=="D":
                        D=1
                    if reply=="E":
                        E=1
                    if reply=="F":
                        F=1
                    if reply=="G":
                        G=1
                    if reply=="H":
                        H=1
                    if reply=="I":
                        I=1
                    if reply=="J":
                        J=1
                    if reply=="K":
                        K=1
                    if reply=="L":
                        L=1
                    if reply=="M":
                        M=1
                    if reply=="N":
                        N=1
                    if reply=="O":
                        O=1
                    if reply=="P":
                        P=1
                    if reply=="Q":
                        Q=1
                    if reply=="R":
                        R=1
                    if reply=="S":
                        S=1
                    if reply=="T":
                        T=1
                    if reply=="U":
                        U=1
                    if reply=="V":
                        V=1
                    if reply=="W":
                        W=1
                    if reply=="X":
                        X=1
                    if reply=="Y":
                        Y=1
                    if reply=="Z":
                        Z=1
                while (reply.swapcase()) in word1:
                    reply=(reply.swapcase())
                    word1=(word1.replace(reply,""))
                    miniloop=0
                    if reply=="a":
                        a=1
                    if reply=="b":
                        b=1
                    if reply=="c":
                        c=1
                    if reply=="d":
                        d=1
                    if reply=="e":
                        e=1
                    if reply=="f":
                        f=1
                    if reply=="g":
                        g=1
                    if reply=="h":
                        h=1
                    if reply=="i":
                        i=1
                    if reply=="j":
                        j=1
                    if reply=="k":
                        k=1
                    if reply=="l":
                        l=1
                    if reply=="m":
                        m=1
                    if reply=="n":
                        n=1
                    if reply=="o":
                        o=1
                    if reply=="p":
                        p=1
                    if reply=="q":
                        q=1
                    if reply=="r":
                        r=1
                    if reply=="s":
                        s=1
                    if reply=="t":
                        t=1
                    if reply=="u":
                        u=1
                    if reply=="v":
                        v=1
                    if reply=="w":
                        w=1
                    if reply=="x":
                        x=1
                    if reply=="y":
                        y=1
                    if reply=="z":
                        z=1
                    if reply=="A":
                        A=1
                    if reply=="B":
                        B=1
                    if reply=="C":
                        C=1
                    if reply=="D":
                        D=1
                    if reply=="E":
                        E=1
                    if reply=="F":
                        F=1
                    if reply=="G":
                        G=1
                    if reply=="H":
                        H=1
                    if reply=="I":
                        I=1
                    if reply=="J":
                        J=1
                    if reply=="K":
                        K=1
                    if reply=="L":
                        L=1
                    if reply=="M":
                        M=1
                    if reply=="N":
                        N=1
                    if reply=="O":
                        O=1
                    if reply=="P":
                        P=1
                    if reply=="Q":
                        Q=1
                    if reply=="R":
                        R=1
                    if reply=="S":
                        S=1
                    if reply=="T":
                        T=1
                    if reply=="U":
                        U=1
                    if reply=="V":
                        V=1
                    if reply=="W":
                        W=1
                    if reply=="X":
                        X=1
                    if reply=="Y":
                        Y=1
                    if reply=="Z":
                        Z=1
                        
                
                
    if Life==0:
        quitter= easygui.enterbox(loss+"  The word was "+str(word),"Hangman", image=loser)            
    if Victory==1:
        VictoryMsg=easygui.enterbox(VictoriousMsg+" Type q to quit or press enter to play again","Hangman",image=Vict)
    if VictoryMsg=="q" or VictoryMsg=="Q":
        sys.exit(0)
    if quitter=="q" or quitter=="Q":
        sys.exit(0)
