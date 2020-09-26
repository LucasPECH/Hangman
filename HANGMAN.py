again=True
while again==True: #Condition to play again

    #Choice of the sexe
    sexe=0
    while sexe!="woman" and sexe!="man":
        sexe=str(input("woman or man? ")) 
        print(end="\n")

    #library of words to guess
    biblio=["cast","chose","claws","coach","constantly","contrast","cookies","customs","damage","deeply","depth","discussion","doll","donkey"]

    #Choose of the word to guess in this game
    from random import*
    indexmot=int(randint(0,len(biblio)-1))
    motdeviner=biblio[indexmot] #Word to guess
    listemotdeviner=[]
    for cpt in range(len(motdeviner)): #The word to guess in form of list
        listemotdeviner.append(motdeviner[cpt])

    usedletter=[] #List of used letter

    life=6 #Life counter

    win=False #Victory condition

    #Print the first message
    print("used letter:")
    print(end="\n")
    print("you have the right to make up 6 errors")

    #Print the first hangman
    if life==6:
        fichier6=open("PENDU6.txt", "r")
        pendu6=fichier6.read()
        print(pendu6)

    #List of dashes of the word length
    data=[]
    for cpt in range(len(motdeviner)):
        data.append("--")
    for i in data:
        print(i,end=" ")
    print(end='\n')

    #We start to guess the letters
    while life>0 and win==False:
        cpt2=0
        visited=False
        lettre1=str(input("guess a letter: "))
        print(end="\n")
        #Check if the letter has been already tried
        for i in range(len(usedletter)): 
            if lettre1==usedletter[i]:
                print("You've already tried this letter, try again")
                visited=True
        if visited==False:
            usedletter.append(lettre1) #Had to used letter list
            print("used letter:")
            for i in usedletter:
                print(i,end=" ")
            print(end="\n")
            #Search letter in the word to guess
            for i in range(len(listemotdeviner)):
                if lettre1==listemotdeviner[i]:
                    cpt2=cpt2+1
            if cpt2==0:
                    life=life-1
            else:
                for i in range(len(listemotdeviner)):
                    if lettre1==listemotdeviner[i]:
                        data[i]=lettre1 #Change dashes into the good letter
            print("you have the right to make up", life,"errors")            
            #Print hangman in fonction of the life
            if life==0 and sexe=="man":
                fichier0=open("PENDU0.txt", "r")
                pendu0=fichier0.read()
                print(pendu0)
            if life==0 and sexe=="woman":
                fichier00=open("PENDUE0.txt", "r")
                pendu00=fichier00.read()
                print(pendu00)
            if life==1 and sexe=="man":
                fichier1=open("PENDU1.txt", "r")
                pendu1=fichier1.read()
                print(pendu1)
            if life==1 and sexe=="woman":
                fichier01=open("PENDUE1.txt", "r")
                pendu01=fichier01.read()
                print(pendu01)
            if life==2:
                fichier2=open("PENDU2.txt", "r")
                pendu2=fichier2.read()
                print(pendu2)
            if life==3:
                fichier3=open("PENDU3.txt", "r")
                pendu3=fichier3.read()
                print(pendu3)
            if life==4:
                fichier4=open("PENDU4.txt", "r")
                pendu4=fichier4.read()
                print(pendu4)
            if life==5:
                fichier5=open("PENDU5.txt", "r")
                pendu5=fichier5.read()
                print(pendu5)
            if life==6:
                fichier6=open("PENDU6.txt", "r")
                pendu6=fichier6.read()
                print(pendu6)
            cpt3=0 #Dashes counter
            for i in data:
                if i!="--":
                    cpt3=cpt3+1
            if cpt3==len(listemotdeviner): #Victory condition
                win=True
            else:
                win=False
            for i in data:
                print(i,end=" ")
            print(end="\n")
        if win==True:
            print(end="\n")
            print("You win well played !!")
            print(end="\n")
        if life==0:
            print(end="\n")
            print("You loose.")
            print("The word was:",motdeviner)
            print(end="\n")
    
    otherone=str(input("Write yes for an other game "))#New game condition changing
    print(end="\n")
    if otherone=="yes":
        again=True
    else:
        again=False









