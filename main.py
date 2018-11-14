from cube import Cube

print("### RUBASCII CUBE v0.1 ###")
print("Press any key to start...")
raw_input()
newCube = Cube()
letsplay = "You gotta a new cube! Let's play..."
print(letsplay)
while True:
    face = raw_input("Choose face (f,b,l,r,u,b) or m to menu: ")
    if face == 'm':
        print
        m = raw_input("Menu: p to print, r to resets, s to sequence, q to quit: ")
        if m == 'p':
            newCube.printCube()
            continue
        if m == 'r':
            newCube = Cube()
            print
            print(letsplay)
            continue
        if m == 's':
            count = 0
            seq = raw_input("Type sequence:" )
            cmds = seq.split(",")
            while not newCube.isDone() or count == 0:
                newCube.rotate(cmds[0], cmds[1])
                count = count + 1
                newCube.rotate(cmds[2], cmds[3])
                count = count + 1
            if newCube.isDone():
                print 'Cube was done in ' + str(count) + ' movements'
                break
        if m == 'q':
            break
    direction = raw_input("Clockwise (y or n): ")
    newCube.rotate(face, direction)
    newCube.printCube()
    if newCube.isDone():
        print 'is done!'