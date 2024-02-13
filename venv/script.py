import time
import keyboard
import pyautogui
import pydirectinput
import tkinter
from defsCV import *
from defsActions import *



#def checkOnandFight():

pyautogui.FAILSAFE = True
time.sleep(1)



quest = gameON = goTo = goFight = fightON = timer = targetON = test = 0
def dialogMain():
    main.mainloop()
def buttonGoSearchFight():
    global goFight
    goFight = 1
    main.destroy()
def buttonQuest1():
    global quest
    quest = 1
    main.destroy()
def testSmth():
    global test
    test = 1
    main.destroy()

main = tkinter.Tk()
main.geometry("100x100")
main.anchor("center")
B1 = tkinter.Button(main, text = "Search fight", command = buttonGoSearchFight)
B2 = tkinter.Button(main, text = "Quest 1", command = buttonQuest1)
B3 = tkinter.Button(main, text = "Test something", command = testSmth)
B1.pack()
B2.pack()
B3.pack()
dialogMain()
gameON = checkGameOn()



#only 2 commands available and checked, along with game status
while ((quest>0.7) or (goFight>0.7)) and (gameON>0.7):

    time.sleep(1)
    gameON = checkGameOn()
    fightON = chechFightON()
    if fightON>gameON:
        gameON=fightON
    if (goFight==1) and (fightON<0.7):
        while (fightON<0.7):
            time.sleep(0.2)
            findEnemyAndMoveTo()
            fightON = chechFightON()
    while (fightON>0.8):
        time.sleep(0.7)
        fightNOW()
        fightON = chechFightON()
    if (quest==1):
        if (checkQuestStatus(1)==0):
            if (checkIfLocationIs(1)>0.75):
                findAndTargetNpc(1)
                takeQuestFromTarget(1)
        if (checkQuestStatus(1)==1):
            pathToQuest1()
            goFight = 1
            while (goFight==1):
                fightON = chechFightON()
                while (fightON<0.7):
                    time.sleep(0.2)
                    findEnemyAndMoveTo()
                    fightON = chechFightON()
                while (fightON>0.8):
                    time.sleep(0.2)
                    fightNOW()
                    fightON = chechFightON()
                if (checkQuestStatus(1)==2):
                    goFight=0
        if (checkQuestStatus(1)==2):
            pathFromQuest1()
           #while
    timer = timer+1

print('TIMER IS', timer)
while (test==1):
    time.sleep(2)
    #pathFromQuest1()
    test=0


