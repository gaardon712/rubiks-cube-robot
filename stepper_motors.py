import RPi.GPIO as GPIO
import time
from array import *
import scramble
import simulator

#variable declarations

delay = 0.001
GreenFace = array('i',[3,5,7,8])
OrangeFace = array('i',[10,11,12,13])
BlueFace = array('i',[15,16,18,19])
RedFace = array('i',[21,22,23,24])
WhiteFace = array('i',[26,29,31,32])
YellowFace = array('i',[33,35,36,37])
TestArray = array('i',[40, 38, 37, 35])

coil1 = 0
coil2 = 0
coil3 = 0
coil4 = 0

#setup for the board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

def turnFace(face):
    changeFace(face)
    for x in range(710):  #705 - 710
        GPIO.output(coil1, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(coil4, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(coil2, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(coil1, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(coil3, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(coil2, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(coil4, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(coil3, GPIO.LOW)
        time.sleep(delay)


    GPIO.setup(coil1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(coil2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(coil3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(coil4, GPIO.OUT, initial=GPIO.LOW)
#Method to change turning face
def changeFace(face):
    print(face)
    global coil1
    global coil2
    global coil3
    global coil4
    if(face == "R" or face == "R2"):
        coil1 = GreenFace[0]
        coil2 = GreenFace[1]
        coil3 = GreenFace[2]
        coil4 = GreenFace[3]
    elif(face == "B" or face == "B2"):
        coil1 = OrangeFace[0]
        coil2 = OrangeFace[1]
        coil3 = OrangeFace[2]
        coil4 = OrangeFace[3]
    elif(face == "L'"):
        coil1 = BlueFace[0]
        coil2 = BlueFace[1]
        coil3 = BlueFace[2]
        coil4 = BlueFace[3]
    elif(face == "F" or face == "F2"):
        coil1 = RedFace[0]
        coil2 = RedFace[1]
        coil3 = RedFace[2]
        coil4 = RedFace[3]
    elif(face == "D" or face == "D2"):
        coil1 = WhiteFace[0]
        coil2 = WhiteFace[1]
        coil3 = WhiteFace[2]
        coil4 = WhiteFace[3]
    elif(face == "U" or face == "U2"):
        coil1 = YellowFace[0]
        coil2 = YellowFace[1]
        coil3 = YellowFace[2]
        coil4 = YellowFace[3]
    elif(face == "R'"):
        coil1 = GreenFace[3]
        coil2 = GreenFace[2]
        coil3 = GreenFace[1]
        coil4 = GreenFace[0]
    elif(face == "B'"):
        coil1 = OrangeFace[3]
        coil2 = OrangeFace[2]
        coil3 = OrangeFace[1]
        coil4 = OrangeFace[0]
    elif(face == "L" or face == "L2"):
        coil1 = BlueFace[3]
        coil2 = BlueFace[2]
        coil3 = BlueFace[1]
        coil4 = BlueFace[0]
    elif(face == "F'"):
        coil1 = RedFace[3]
        coil2 = RedFace[2]
        coil3 = RedFace[1]
        coil4 = RedFace[0]
    elif(face == "D'"):
        coil1 = WhiteFace[3]
        coil2 = WhiteFace[2]
        coil3 = WhiteFace[1]
        coil4 = WhiteFace[0]
    elif(face == "U'"):
        coil1 = YellowFace[3]
        coil2 = YellowFace[2]
        coil3 = YellowFace[1]
        coil4 = YellowFace[0]
    else:
        print("WARNING, THE CODE IS ENTERING THE TEST ARRAY")
        coil1 = TestArray[0]
        coil2 = TestArray[1]
        coil3 = TestArray[2]
        coil4 = TestArray[3]

def scramble_real_cube():
    scr = simulator.scramble_cube()
    print(simulator.get_cubestring())
    for x in scr:
        if(x == "L" or x == "R" or x == "F" or x == "B" or x == "U" or x == "D"):
            turnFace(x)
        elif(x == "L2" or x == "R2" or x == "F2" or x == "B2" or x == "U2" or x == "D2"):
            turnFace(x)
            turnFace(x)
        else:
            turnFace(x)

def solve_real_cube():
    solution = simulator.solve_cube(simulator.get_cubestring())
    print(solution)
    for x in solution:
        if(x == "L" or x == "R" or x == "F" or x == "B" or x == "U" or x == "D"):
            turnFace(x)
        elif(x == "L2" or x == "R2" or x == "F2" or x == "B2" or x == "U2" or x == "D2"):
            turnFace(x)
            turnFace(x)
        else:
            turnFace(x)
