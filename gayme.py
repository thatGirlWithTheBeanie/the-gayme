import time
import random

count = 20

#### ----------- TRADE FROM PLAYER 1 -----------------
def tradep1():
    print("")
    print(player1n + ": who will you trade away?")
    tradea = input("")
    print("")
    if tradea not in player1:
        print("i'm sorry they are not in your deck")
        return
    else:

        time.sleep(1)
        print("")
        print(player1n + ": for which straight girl?")
        tradeb = input("")
        if tradeb not in player2:
            print("im sorry they are not in your deck")
            return
        time.sleep(1)
        print("")
        print("")

    print(player2n + " do you accept?")
    acceptt = input("")
    if acceptt == "yes":
        player1.insert(0,tradeb)
        player2.remove(tradeb)
        player2.insert(0,tradea)
        player1.remove(tradea)
        time.sleep(1)
        print("trade complete!")
        time.sleep(1)
        print("")
        print("")
        time.sleep(1)
        print("do you want to see your deck " + player1n)
        seedeck1 = input ("")
        if seedeck1 == "yes":
            print("on team Rainbow:")
            time.sleep(1)
            print("\n".join(player1))
            print("")
            print("")
        print("do you want to see your deck " + player2n)
        seedeck2 = input("")
        if seedeck2 == "yes":
            print("on team Black and white:")
            time.sleep(1)
            print("\n".join(player2))
            print("")
            print("")
### count = count -1
#### was here


#### ---------END OF TRADE PLAYER 1 ----------------------


#### ----------- TRADE FROM PLAYER 2 -----------------
def tradep2():
    print("")
    print(player2n + ": who will you trade away?")
    tradea = input("")
    print("")
    if tradea not in player2:
        print("i'm sorry they are not in your deck")
        return
    else:
        
        time.sleep(1)
        print("")
        print(player2n + ": for which queer?")
        tradeb = input("")
        if tradeb not in player1:
            print("im sorry they are not in the deck")
            return
        time.sleep(1)
        print("")
        print("")

    print(player1n + " do you accept?")
    acceptt = input("")
    if acceptt == "yes":
        player2.insert(0,tradea)
        player1.remove(tradeb)
        player1.insert(0,tradea)
        player2.remove(tradea)
        time.sleep(1)
        print("trade complete!")
        time.sleep(1)
        print("")
        print("")
        time.sleep(1)
        print("do you want to see your deck " + player2n)
        seedeck1 = input ("")
        if seedeck1 == "yes":
            print("on team Black and white:")
            time.sleep(1)
            print("\n".join(player2))
            print("")
            print("")
        print("do you want to see your deck " + player1n)
        seedeck2 = input("")
        if seedeck2 == "yes":
            print("on team Rainbow:")
            time.sleep(1)
            print("\n".join(player1))
            print("")
            print("")
### count = count -1
### was here

#### ---------END OF TRADE PLAYER 2 ----------------------


### define teams --- long live ellen!----
player1 = ["ellen", "adrianna dilonardo", "sarah rotella", "ellen page", "xena", "cosima", "willow", "santana", "ruby rose", "natasha negovanlis", "rose dix", "kristen stewart", "portia de rossi", "gaby dunn"]
player2 = ["laura prepon", "anna kendrick", "beyonce", "buffy", "evelyne brochu", "elise bauman", "tatiana maslany", "hayley atwell", "gillian anderson", "lucy lawless", "jenifer lawrence", "angelina jolie", "scarlett johansson", "rita volk"]
print ("")
print ("")
print ("")
print ("")
print ("")
print ("Welcome Queers!")
time.sleep(2)
print("")
print("please answer yes or no unless prompted")
print("")
time.sleep(2)
print("this is a two player game")
print("")
time.sleep(2)
print("would you like to read the rules?")
print("")
rulesq = input("")
if rulesq == "yes":
    time.sleep(1)
    print("")
    print("")
    print("")
    print("trade people to create yo' dream queer team")
    time.sleep(1)
    print("")
    print("you must only trade queers for equal or lesser value")
    print("")
    time.sleep(1)
    print("")
    print("e.g Kesha for Michelle obama")
    print("")

### player 1
print ("who is going to be team Rainbow?")
player1n = input ("")

if player1n == "adrianna":
    time.sleep(2)
    print ("ok seriously age, go to the bar and get a girl")
    time.sleep(1)

print("")
### player 2
print ("who is going to be team black and white?")
player2n = input ("")

if player2n == "adrianna":
    time.sleep(2)
    print ("you really need to stop obssesing Age, its not healthy")
    time.sleep(1)


print("")
### start
print ("are you ready?")
start = input ("")
if start == "yes":
    time.sleep(1)
    print ("OK then!")
elif start == "no":
    print ("well tough")

else:
    print ("yes or no please")

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


### teams listed
time.sleep(1)
print ("in team Rainbow we have... ")
print("")
print("\n".join(player1))
time.sleep(1)
print("")
print("")
print ("and in team black and white we have....")
print("")
print("\n".join(player2))
time.sleep(1)

print("")
print("")
print("")
print("")
   

while count in range(1, 21):
### first swap start
    print("who will go?")
    print (player1n + " or " + player2n)
    firstgo = input ("")
    if firstgo == player1n:
        time.sleep(1)
        tradep1()
    if firstgo == player2n:
        time.sleep(1)
        tradep2()
    print("")
    print("")
    print("")
    time.sleep(1)
    count = count - 1
    print ("you have ", count, "trades left")
    print("")
    time.sleep(1)

#### --------- end of game ------------

if 0 >= count:
    print("")
    print("")
    print("")
    print("")
    print("the game is over")
    time.sleep(1)
    print("")
    print ("your final decks are:")
    print("")
    print("Team Rainbow")
    print("-------------------")
    print("\n".join(player1))
    time.sleep(2)
    print("")
    print("Team Black and white")
    print("-------------------")
    print("\n".join(player2))
    time.sleep(2)
    print("")
    print("")
    print("do you want to see the credits?")
    response = input()
    if response == "yes":
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Game Designers:")
        print("")
        print("")
        time.sleep(1)
        print("Adrianna DiLonardo and Sarah Rotella")
        print("")
        time.sleep(1)
        print("with credit to Jamie")
        print("")
        time.sleep(1)
        print("and created by Sam")
    else:
        print ("good bye ^_^")
        
