import solver

#NOW BROKEN, SOLVER.PY REMOVED


#front = red
#top = yellow
#right = green
#back = orange
#left = blue
#bottom = white

#top -> left -> front -> right -> back -> bottom

#example = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
#superflip = 'yoybygyrybybobrbwbryrbrgrwrgygrgogwgoyogobowowrwbwgwow'
#checkerboard = 'ywywywywybgbgbgbgbrororororgbgbgbgbgororororowywywywyw'
cube = 'rbbyyryyrwrowbbwrgbbgrrgyywygrygogwwyobwobrobooowwgogg'
solution = solver.solve(cube)
length = len(solution)
for x in range(length):
    print(solution[x])
