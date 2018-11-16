from cube import Cube

print("### RUBASCII CUBE v0.1 ###")
print("Press any key to start...")
raw_input()
newCube = Cube()
letsplay = "You gotta a new cube! Let's play..."
print(letsplay)
while True:
    comms = raw_input("Type move sequence ('r','l','u','d','f','b' for faces + 'i' for counter-clockwise) or m to menu: ")
    if comms == 'm':
        print
        m = raw_input("Menu: s_huffle, p_rint, r_eset, l_oop, q_uit: ")
        if m == 'p':
            newCube.printCube()
            continue
        if m == 'r':
            newCube = Cube()
            print
            print(letsplay)
            continue
        if m == 'l':
            count = 0
            seq = raw_input("Type loop sequence:" )
            cmds = seq.split(" ")
            print 'Performing loop sequence...'
            while not newCube.isDone() or count == 0:
                for cmd in cmds:
                    newCube.rotate(cmd)
                    count = count + 1
            if newCube.isDone():
                print 'Rubascii Cube was done in ' + str(count) + ' movements'
                print
                break
        if m == 's':
            newCube.shuffle()
        if m == 'q':
            break
    #direction = raw_input("Clockwise (y or n): ")
    newCube.rotate(comms)
    newCube.printCube()
    if newCube.isDone():
        print 'Congratulations! The Rubascii Cube is done!'
        print