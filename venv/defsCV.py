from PIL import ImageGrab
import pydirectinput
import cv2
import time

inGame = cv2.imread('C:/Users/user/IdeaProjects/search1/1/inGame.png',cv2.IMREAD_GRAYSCALE)
inFight = cv2.imread('C:/Users/user/IdeaProjects/search1/1/inFight.png',cv2.IMREAD_GRAYSCALE)
enemyBar = cv2.imread('C:/Users/user/IdeaProjects/search1/1/enemyBar.png',cv2.IMREAD_COLOR)
secondMangleW = cv2.imread('C:/Users/user/IdeaProjects/search1/1/secondMangleWhite.png',cv2.IMREAD_COLOR)
targetEnemy = cv2.imread('C:/Users/user/IdeaProjects/search1/1/targetEnemy.png',cv2.IMREAD_COLOR)
questNotInRange = cv2.imread('C:/Users/user/IdeaProjects/search1/1/questNotInRange.png',cv2.IMREAD_COLOR)
questInRange = cv2.imread('C:/Users/user/IdeaProjects/search1/1/questInRange.png',cv2.IMREAD_COLOR)
imageAcceptQuest = cv2.imread('C:/Users/user/IdeaProjects/search1/1/acceptQ.png',cv2.IMREAD_COLOR)
npc1 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/questAC1.png',cv2.IMREAD_COLOR)
npc2 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/questAC2.png',cv2.IMREAD_COLOR)
npc3 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/questAC3.png',cv2.IMREAD_COLOR)
location1 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/location1.png',cv2.IMREAD_COLOR)
location2 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/location2.png',cv2.IMREAD_COLOR)
location3 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/location3.png',cv2.IMREAD_COLOR)
quest1isOngoing = cv2.imread('C:/Users/user/IdeaProjects/search1/1/quest1statusOngoing.png',cv2.IMREAD_COLOR)
quest1isComplete = cv2.imread('C:/Users/user/IdeaProjects/search1/1/quest1statusComplete.png',cv2.IMREAD_COLOR)
q1m1 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/q1marker1.png',cv2.IMREAD_COLOR)
q1m2 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/q1marker2.png',cv2.IMREAD_COLOR)
q1m3 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/q1marker3.png',cv2.IMREAD_COLOR)
cursor47 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/cursor47.png',cv2.IMREAD_COLOR)
cursor60 = cv2.imread('C:/Users/user/IdeaProjects/search1/1/cursor60.png',cv2.IMREAD_COLOR)
hpFull = cv2.imread('C:/Users/user/IdeaProjects/search1/1/hpFull.png',cv2.IMREAD_COLOR)

def checkGameOn():
    baseS = ImageGrab.grab(bbox=(0,0,300,200))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_GRAYSCALE)
    res = cv2.matchTemplate(screenCurrent,inGame,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val

def checkFullHP():
    baseS = ImageGrab.grab(bbox=(233,79,247,89))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,hpFull,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if (max_val>0.9):
        return True
    return False
def chechFightON():
    baseS = ImageGrab.grab(bbox=(0,0,300,200))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_GRAYSCALE)
    res = cv2.matchTemplate(screenCurrent,inFight,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val

def enemyInRear():
    baseS = ImageGrab.grab(bbox=(755,520,1161,700))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,enemyBar,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (max_val>0.8):
        return (max_loc[0]+755, max_loc[1]+520)
    else:
        return (0,0)
def enemyInFront():
    baseS = ImageGrab.grab(bbox=(755,328,1161,519))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,enemyBar,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (max_val>0.8):
        return (max_loc[0]+755, max_loc[1]+328)
    else:
        return (0,0)
def findRedLine():
    #start with close area
    baseS = ImageGrab.grab(bbox=(800,200,1300,700))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,enemyBar,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (max_val>0.9):
        return (max_loc[0]+800,max_loc[1]+200)

    #if not - all screen
    baseS = ImageGrab.grab(bbox=(0,0,1920,1080))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,enemyBar,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if (max_val>0.9):
        return max_loc
    return [-1,-1]

def secondMangleWhite():
    baseS = ImageGrab.grab(bbox=(405,993,418,1007))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,secondMangleW,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if (max_val>0.93):
        return True
    return False

def ifTargetEnemy():
    baseS = ImageGrab.grab(bbox=(0,56,334,77))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,targetEnemy,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if (max_val>0.93):
        return True
    return False

def targetNPC(id):
    baseS = ImageGrab.grab(bbox=(0,0,1920,1080))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    l = globals().get("npc" + str(id))
    res = cv2.matchTemplate(screenCurrent,l,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if (max_val>0.8):
        return [max_loc[0]+100,max_loc[1]+60]

    return [-1,-1]

def targetAcceptQuest():
    baseS = ImageGrab.grab(bbox=(0,556,250,850))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,imageAcceptQuest,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (max_val>0.8):
        return [max_loc[0]+45,max_loc[1]+566]
    return [-1,-1]

def checkIfLocationIs(id):
    baseS = ImageGrab.grab(bbox=(1656,18,1920,59))
    #baseS = ImageGrab.grab(bbox=(0,0,1920,1080))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    l = globals().get("location" + str(id))
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,l,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (max_val>0.80):
        return True
    return False
def checkQuestStatus(id):
    pydirectinput.press("l")
    time.sleep(0.5)
    baseS = ImageGrab.grab(bbox=(24,238,424,638))
    time.sleep(0.5)
    pydirectinput.press("l")
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res1 = cv2.matchTemplate(screenCurrent,quest1isOngoing,cv2.TM_CCORR_NORMED)
    res2 = cv2.matchTemplate(screenCurrent,quest1isComplete,cv2.TM_CCORR_NORMED)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
    if (max_val1>0.93):
        return 1
    elif (max_val2>0.9):
        return 2
    else:
        return 0

def findQuestmarker(id, number):
    baseS = ImageGrab.grab(bbox=(0,0,1920,1080))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    l = globals().get("q" + str(id)+ "m"+str(number))

    res = cv2.matchTemplate(screenCurrent,l,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (max_val>0.95):
        return max_loc[0]
    else:
        return 0

def miniMapCheck(degree):
    baseS = ImageGrab.grab(bbox=(1800,121,1823,144))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    l = globals().get("cursor"+str(degree))
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,l,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val

def miniMapObjectCoord(id):
    baseS = ImageGrab.grab(bbox=(1730,66,1892,200))
    baseS.save('C:/Users/user/IdeaProjects/search1/1/current.png')
    screenCurrent = cv2.imread('C:/Users/user/IdeaProjects/search1/1/current.png',cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screenCurrent,q1m3,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    print(max_loc)
    if (max_val>0.93):
        return max_loc
    else:
        return (0,0)