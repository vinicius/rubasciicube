from cube import Cube

print("### RUBASCII CUBE v1.0 ###")
print("Press any key to start...")
raw_input()
newCube = Cube()
letsplay = "You gotta a new cube! Let's play..."
print(letsplay)
while True:
    comms = raw_input("Type move sequence (m for menu):")
    if comms == 'm':
        print
        m = raw_input("Menu: c_ontrols, s_huffle, p_rint, r_eset, l_oop, q_uit: ")
        if m == 'c':
            print
            print("-- Controls ----------------------------------------------------------------------")
            print("Choose 'r','l','u','d','f','b' for face")
            print("Faces: r=right, l=left, u=upper, d=down, f=front, b=back")
            print
            print("By default the face is rotated clockwise direction. Add 'i' for counter-clockwise")
            print
            print("Example: f li b d ui representes the following move sequence")
            print("   front, left counter-clockwise, back, down, upper counter-clockwise")
            print("----------------------------------------------------------------------------------")
            print
            continue
        if m == 'p':
            newCube.printCube()
            continue
        if m == 'r':
            newCube = Cube()
            print
            newCube.printCube() 
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
                    newCube.printCube()
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