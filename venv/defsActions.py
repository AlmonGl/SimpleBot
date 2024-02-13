import random

import pydirectinput
import pyautogui
import time
import random
from defsCV import *

def fightNOW():
    t1 = enemyInFront()
    if (t1[0]>0):
        turnTo(t1[0]+107)
        pydirectinput.moveTo(t1[0]+10,t1[1]-5)
        pydirectinput.click()
        time.sleep(0.2)
        pydirectinput.press("2")
        time.sleep(1)
        pydirectinput.press("2")
        time.sleep(1)
        pydirectinput.press("2")
        pydirectinput.keyDown("right")
        time.sleep(0.1)
        pydirectinput.keyUp("right")
        return True
    t1=enemyInRear()
    if (t1[0]>0):
        pydirectinput.keyDown("left")
        time.sleep(0.8)
        pydirectinput.keyUp("left")
    else:
        pyautogui.mouseDown(button='left')
        time.sleep(0.5)
        pyautogui.move(0, 150)
        time.sleep(0.5)
        pyautogui.mouseUp(button='left')
        pydirectinput.keyDown("left")
        time.sleep(0.2)
        pydirectinput.keyUp("left")
    return False

def findEnemyAndMoveTo():
    if (not checkFullHP()):
        pydirectinput.press("b")
        time.sleep(2.7)
        pydirectinput.press("v")
    t1 = findRedLine()
    if (t1[0]>0):
        turnTo(t1[0])
        if (t1[1]>520):
            pydirectinput.keyDown("left")
            time.sleep(0.8)
            pydirectinput.keyUp("left")
        if (0<t1[1]<340):
            pydirectinput.keyDown("w")
            time.sleep(1.5)
            pydirectinput.keyUp("w")
    if (t1[0]<0):
        x = random.randint(1, 8)
        print(x)
        if (1<=x<=2):
            pydirectinput.keyDown("w")
            time.sleep(1.9)
            pydirectinput.keyUp("w")
        elif (x==4 or x ==3):
            pydirectinput.keyDown("left")
            time.sleep(0.5)
            pydirectinput.keyUp("left")
        elif (x==5):
            pydirectinput.keyDown("right")
            time.sleep(0.5)
            pydirectinput.keyUp("right")
        elif (x>=6):
            time.sleep(2)

def findAndTargetNpc(id):
    t1 = [-1,-1]
    while (t1[0]<0):
        time.sleep(2)
        t1 = targetNPC(id)
        if (t1[0]>0):
            while not ((850<=t1[0]<=1050) and (450<=t1[1]<=520)):
                turnTo(t1[0])
                t1 = targetNPC(id)
                if (t1[1]<450):
                    pydirectinput.keyDown("w")
                    time.sleep(0.3)
                    pydirectinput.keyUp("w")
                if (t1[1]>520):
                    pydirectinput.press("s")
                t1 = targetNPC(id)
            pyautogui.moveTo(t1[0],t1[1])
        else:
            x = random.randint(1,4)
            if (x==1):
                pydirectinput.keyDown("left")
                time.sleep(0.2)
                pydirectinput.keyUp("left")
            if (x==2):
                pydirectinput.keyDown("right")
                time.sleep(0.2)
                pydirectinput.keyUp("right")
            pydirectinput.keyDown("w")
            time.sleep(1)
            pydirectinput.keyUp("w")

def takeQuestFromTarget(id):
    pydirectinput.rightClick()
    time.sleep(0.5)
    t1 = targetAcceptQuest()
    if (t1[0]<0):
        findAndTargetNpc(id)
        return False
    pydirectinput.moveTo(t1[0],t1[1])
    time.sleep(0.5)
    pydirectinput.leftClick(duration=0.5)
    return True
def completeQuestFromTarget(id):
    pydirectinput.rightClick()
    time.sleep(0.5)
    pydirectinput.moveTo(307,438)
    time.sleep(0.5)
    pydirectinput.leftClick(duration=0.5)
    pydirectinput.moveTo(101,655)
    pydirectinput.leftClick(duration=0.5)
def turnTo(x):
    if (0<x<850):
        ti = 0
        if (0<x<150):
            ti = 0.3
        elif (150<x<300):
            ti = 0.2
        elif (301<x<399):
            ti = 0.1
        elif (401<x<599):
            ti = 0.1

        elif (600<x<=849):
            ti = 0.1
        if (ti>0.1):
            pydirectinput.keyDown("left")
            time.sleep(ti)
            pydirectinput.keyUp("left")
        if (ti==0.1):
            pydirectinput.press("left")

    if (1050<x<1920):
        ti = 0
        if (1751<x<1920):
            ti = 0.3
        elif (1601<x<1750):
            ti = 0.2
        elif (1201<x<1600):
            ti = 0.1
        elif (1050<x<1200):
            ti = 0.1
        if (ti>0.1):
            pydirectinput.keyDown("right")
            time.sleep(ti)
            pydirectinput.keyUp("right")
        if (ti==0.1):
            pydirectinput.press("right")

def balanceCamera():
    pyautogui.mouseDown(button='left')
    time.sleep(0.5)
    pyautogui.move(0, 200)
    pyautogui.move(0, 200)
    time.sleep(0.5)
    pyautogui.mouseUp(button='left')

def turnLeft(x):
    pydirectinput.keyDown("left")
    time.sleep(0.7)
    pydirectinput.keyUp("left")

def pathToQuest1():
    time.sleep(1)
    pydirectinput.keyDown("left")
    time.sleep(0.6)
    pydirectinput.keyUp("left")
    pydirectinput.keyDown("w")
    time.sleep(3.5)
    pydirectinput.keyUp("w")
    pydirectinput.keyDown("right")
    time.sleep(0.4)
    pydirectinput.keyUp("right")
    pydirectinput.keyDown("w")
    time.sleep(2)
    pydirectinput.keyUp("w")
    pydirectinput.press("h")
    pydirectinput.keyDown("space")
    time.sleep(3)
    pydirectinput.keyUp("space")
    pydirectinput.keyDown("right")
    time.sleep(1)
    pydirectinput.keyUp("right")

    pyautogui.mouseDown(button='right')
    time.sleep(0.5)
    pyautogui.move(0, -250)
    time.sleep(0.5)
    pyautogui.mouseUp(button='right')

    t1=findQuestmarker(1,1)
    if (t1>0):
        t1 = 1920/2-t1
        pyautogui.mouseDown(button='right')
        time.sleep(0.5)
        pyautogui.move(-t1/4, 0)
        time.sleep(0.5)
        pyautogui.mouseUp(button='right')


    pydirectinput.keyDown("w")
    time.sleep(15)
    pydirectinput.keyUp("w")
    pydirectinput.keyDown("o")
    time.sleep(4)
    pydirectinput.keyUp("o")
    pydirectinput.press("v")

    balanceCamera()
def pathFromQuest1():
    balanceCamera()
    time.sleep(1)
    pydirectinput.press("h")
    pydirectinput.keyDown("space")
    time.sleep(2.5)
    pydirectinput.keyUp("space")
    pyautogui.mouseDown(button='right')
    time.sleep(0.5)
    pyautogui.move(0, -250)
    time.sleep(0.5)
    pyautogui.mouseUp(button='right')

    while (miniMapCheck(47)<0.9):
        pydirectinput.press("left")


    pydirectinput.keyDown("w")
    t1 = miniMapObjectCoord(1)
    while (t1[0]==0):
        t1 = miniMapObjectCoord(1)
    pydirectinput.keyUp("w")



    if (53<=t1[1]<=63):
        pydirectinput.keyDown("left")
        time.sleep(0.05)
        pydirectinput.keyUp("left")
        print("C")

    elif (t1[1]<=52):
        print("D")
        pydirectinput.keyDown("left")
        time.sleep(0.05)
        pydirectinput.keyUp("left")
    pydirectinput.keyDown("w")
    while (not checkIfLocationIs(3)):
        time.sleep(1)
    pydirectinput.keyUp("w")

    pydirectinput.keyDown("o")
    time.sleep(8)
    pydirectinput.keyUp("o")
    pydirectinput.press("h")
    time.sleep(1)
    pydirectinput.press("v")
    balanceCamera()
    findAndTargetNpc(2)
    pydirectinput.press("right", 6)
    pydirectinput.keyDown("w")
    time.sleep(9)
    pydirectinput.keyUp("w")
    pydirectinput.press("right", 4)
    findAndTargetNpc(3)
    while (miniMapCheck(60)<0.94):
        pydirectinput.press("left")
    pydirectinput.keyDown("w")
    time.sleep(2.6)
    pydirectinput.keyUp("w")
    pydirectinput.press("right", 4)
    pydirectinput.keyDown("w")
    time.sleep(1.8)
    pydirectinput.keyUp("w")
    pydirectinput.press("left", 3)
    pydirectinput.keyDown("w")
    time.sleep(2)
    pydirectinput.keyUp("w")
    findAndTargetNpc(1)
    completeQuestFromTarget(1)



