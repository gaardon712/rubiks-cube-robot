import scramble
from rubik_solver import utils
import time

cube = []
#####################################################################
def setup():
    global cube
    cube =      ['y','y','y',
                 'y','y','y',
                 'y','y','y',
    'b','b','b',
    'b','b','b',
    'b','b','b',
                'r','r','r',
                 'r','r','r',
                 'r','r','r',
                            'g','g','g',
                            'g','g','g',
                            'g','g','g',
                                        'o','o','o',
                                        'o','o','o',
                                        'o','o','o',
                'w','w','w',
                'w','w','w',
                'w','w','w']
#####################################################################
def swap(index1, index2):
    global cube
    swaper = cube[index2]
    cube[index2] = cube[index1]
    cube[index1] = swaper
#####################################################################
def f():
    global cube
    swap(18, 20)
    swap(18, 26)
    swap(18, 24)
    swap(19, 23)
    swap(19, 25)
    swap(19, 21)
    
    swap(6, 27)
    swap(6, 47)
    swap(6, 17)
    swap(7, 30)
    swap(7, 46)
    swap(7, 14)
    swap(8, 33)
    swap(8, 45)
    swap(8, 11)

def u():
    global cube
    swap(0, 2)
    swap(0, 8)
    swap(0, 6)
    swap(1, 5)
    swap(1, 7)
    swap(1, 3)
    
    swap(9, 36)
    swap(9, 27)
    swap(9, 18)
    swap(10, 37)
    swap(10, 28)
    swap(10, 19)
    swap(11, 38)
    swap(11, 29)
    swap(11, 20)

def r():
    global cube
    swap(27, 29)
    swap(27, 35)
    swap(27, 33)
    swap(28, 32)
    swap(28, 34)
    swap(28, 30)

    swap(2, 42)
    swap(2, 47)
    swap(2, 20)
    swap(5, 39)
    swap(5, 50)
    swap(5, 23)
    swap(8, 36)
    swap(8, 53)
    swap(8, 26)
    
def b():
    global cube
    swap(36, 38)
    swap(36, 44)
    swap(36, 42)
    swap(37, 41)
    swap(37, 43)
    swap(37, 39)
    
    swap(0, 15)
    swap(0, 53)
    swap(0, 29)
    swap(1, 12)
    swap(1, 52)
    swap(1, 32)
    swap(2, 9)
    swap(2, 51)
    swap(2, 35)

def l():
    global cube
    swap(9, 11)
    swap(9, 17)
    swap(9, 15)
    swap(10, 14)
    swap(10, 16)
    swap(10, 12)
    
    swap(0, 18)
    swap(0, 45)
    swap(0, 44)
    swap(3, 21)
    swap(3, 48)
    swap(3, 41)
    swap(6, 24)
    swap(6, 51)
    swap(6, 38)

def d():
    global cube
    swap(45, 47)
    swap(45, 53)
    swap(45, 51)
    swap(46, 50)
    swap(46, 52)
    swap(46, 48)
    
    swap(15, 24)
    swap(15, 33)
    swap(15, 42)
    swap(16, 25)
    swap(16, 34)
    swap(16, 43)
    swap(17, 26)
    swap(17, 35)
    swap(17, 44)
#####################################################################
def scramble_cube():
    scr = scramble.scramb()
    #print(scr)
    for i in scr:
        x = i
        if(x == "W"):
            d()
            #print("d")
        elif(x == "W'"):
            d()
            d()
            d()
            #print("d'")
        elif(x == "W2"):
            d()
            d()
            #print("d2")
        elif(x == "G"):
            r()
            #print("r")
        elif(x == "G'"):
            r()
            r()
            r()
            #print("r'")
        elif(x == "G2"):
            r()
            r()
            #print("r2")
        elif(x == "B"):
            b()
            #print("l")
        elif(x == "B'"):
            b()
            b()
            b()
            #print("l'")
        elif(x == "B2"):
            b()
            b()
            #print("l2")
        elif(x == "O"):
            b()
            #print("b")
        elif(x == "O'"):
            b()
            b()
            b()
            #print("b'")
        elif(x == "O2"):
            b()
            b()
            #print("b2")
        elif(x == "R"):
            f()
            #print("f")
        elif(x == "R'"):
            f()
            f()
            f()
            #print("f'")
        elif(x == "R2"):
            f()
            f()
            #print("f2")
        elif(x == "Y"):
            u()
            #print("u")
        elif(x == "Y'"):
            u()
            u()
            u()
            #print("u'")
        elif(x == "Y2"):
            u()
            u()
            #print("u2")
        
#####################################################################
def get_cubestring():
    cubestring = str()
    for x in range(0,54):
        cubestring = cubestring + cube[x]
    return cubestring
#####################################################################
def solve_cube(cube):
    print('building solution')
    return utils.solve(cube, 'Kociemba')
#####################################################################
setup()
f()
r()
r()
b()
d()
d()
f()
u()
u()
f()
f()
d()
d()
f()
f()
f()
r()
r()
b()
b()
b()
l()#breaks on this line  start matches part in hhe positions
l()
l()
d()
d()
d()
l()
l()
u()
u()
u()
r()
b()
b()
u()
u()
u()
b()
u()
u()
print(get_cubestring())

            "R",
            "G2",
            "O",
            "W2",
            "R",
            "Y2",
            "R2",
            "W2",
            "R'",
            "G2",
            "O'",
            "B'",
            "W'",
            "B2",
            "Y'",
            "G",
            "O2",
            "Y'",
            "O",
            "Y2"
