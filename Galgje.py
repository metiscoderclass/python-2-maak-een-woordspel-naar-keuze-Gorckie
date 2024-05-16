import getpass
import sys

def welkom():
    print("Hallo, en welkom bij....")
    print("**************************************************")
    print("* ___      __     __     ___    ____   ____   __ *")
    print("*/ __)    /__\   (  )   / __)  (_  _) ( ___) (  )*")
    print("*( (_-.  /(__)\   )(__ ( (_-. .-_)(    )__)  (__)*")
    print("*\___/  (__)(__) (____) \___/ \____)  (____) (__)*")
    print("*                                                *")
    print("**************************************************")
    print("")
    print("Voor het spelen zijn er nog wat dingen die je moet weten:")
    print("1. Vraag even aan iemand anders om een geheim woord voor je in te vullen.")
    print("2. Als je een watje bent en opeens wil stoppen met spelen typ je 'qq'")
    print("3. Als je het woord denkt te weten dan typ je dat in inplaats van een letter.")
    print("Succes.")

def kies_woord():
    geheim_woord=getpass.getpass("Welk woord moet er geraden worden?").lower()
    return geheim_woord
    
def galg():
    if pogingen == 0:
        print(" _______________")
        print("  |/      ")
        print("  |      ")
        print("  |       ")
        print("  |     ")
        print("  |      ")
        print("  |")
        print("__|________")
        
    elif pogingen == 1:
        print(" _______________")
        print("  |/      |")
        print("  |      ")
        print("  |       ")
        print("  |     ")
        print("  |      ")
        print("  |")
        print("__|________")
        
    elif pogingen == 2:
        print(" _______________")
        print("  |/      |")
        print("  |      ( )")
        print("  |       ")
        print("  |     ")
        print("  |      ")
        print("  |")
        print("__|________")
        
    elif pogingen == 3:
        print(" _______________")
        print("  |/      |")      
        print("  |      ( )")
        print("  |       |")
        print("  |     ")
        print("  |      ")
        print("  |")
        print("__|________")

    elif pogingen == 4:
        print(" _______________")
        print("  |/      |")
        print("  |      (_)  ")
        print("  |       |")
        print("  |     -( )- ")
        print("  |      ")
        print("  |")
        print("__|________")

    elif pogingen == 5:
        print(" _______________")
        print("  |/      |")
        print("  |      (_)  ")
        print("  |       |")
        print("  |     -( )-")
        print("  |      | |")
        print("  |")
        print("__|________")
        print("")
        print("Sorry, het lijkt erop dat je dood bent.")
        print("Wat je had MOETEN raden is:",geheim_woord)
        print("volgende keer beter!")
        sys.exit()

def klopthet():
    global gok
    correct = False

    while not correct:
        gok = input("welke letter kan er in dit woord zitten?")

        
        if not gok.isalpha():
                print("Aleen letters!") 
                
        elif gok == "qq":
                print("lafaard!")
                exit()
                
        elif gok == geheim_woord:
            print("*********************************************************************************************")
            print("*  ___    ___    ___   ____  __    ____    ___    ____   _____  ____   ____   _____    ___  *")
            print("* / __)  (____) ( __) (____)(  )  (_  _)  / __\  (_  _) (_   _)( ___) ( ___) (  __ )  |   \ *")
            print("*( (_-.   )__)  ( __)  )__)  )(__  _)(_  ( (__    _)(_    | |   )__)   )__)  (  __ \  | () )*")
            print("* \___/  (____) (_)   (____)(____)(____)  \___/  (____)   |_|  ( ___) ( ___) (__) \_\ |___/ *")
            print("*                                                                                           *")
            print("*********************************************************************************************")
            print("")
            sys.exit("Je hebt het geraden!")
            
        elif len(gok) != 1:
                print("Het blijkt dat je of meer dan een letter of het verkeerde woord hebt geraden.")
                
        elif gok in foute_letters or gok in geraden:
                print("Deze heb je al gekozen! >:(")
                
        else:
                return gok
            

def info():
    print("Foute letters:",foute_letters)
    print("al geraden:",geraden)
    galg()

welkom()
    
doorgaan = True

while doorgaan == True:
    geheim_woord = kies_woord()

    foute_letters = []
    geraden = []
    pogingen = 0

    while pogingen < 6:
        klopthet()
            
        if gok in geheim_woord:
            geraden.append(gok)
            info()
        
        else:
            foute_letters.append(gok)
            pogingen += 1
            info()
         
    
              
