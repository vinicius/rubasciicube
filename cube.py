import numpy as np
import random
from termcolor import colored

class Cube:
    # The faces must be read in the sense: left-rigth, up-down
    def __init__(self):
        #self.front = np.array([['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']])
        #self.back = np.array([['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']])
        #self.left = np.array([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']])
        #self.right = np.array([['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']])
        #self.upper = np.array([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']])
        #self.botton = np.array([['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']])
        self.W = colored(' W ', 'white', 'on_white')
        self.Y = colored(' Y ', 'yellow', 'on_yellow')
        self.O = colored(' O ', 'magenta', 'on_magenta')
        self.R = colored(' R ', 'red', 'on_red')
        self.B = colored(' B ', 'blue', 'on_blue')
        self.G = colored(' G ', 'green', 'on_green')
        W = self.W
        Y = self.Y
        O = self.O
        R = self.R
        B = self.B
        G = self.G
        self.front = np.array([[W, W, W], [W, W, W], [W, W, W]])
        self.back = np.array([[Y, Y, Y], [Y, Y, Y], [Y, Y, Y]])
        self.left = np.array([[O, O, O], [O, O, O], [O, O, O]])
        self.right = np.array([[R, R, R], [R, R, R], [R, R, R]])
        self.upper = np.array([[B, B, B], [B, B, B], [B, B, B]])
        self.botton = np.array([[G, G, G], [G, G, G], [G, G, G]])
    
    def printFaces(self):
        print("front:")
        print(self.front)
        print("back:")
        print(self.back)
        print("left:")
        print(self.left)
        print("right:")
        print(self.right)
        print("upper:")
        print(self.upper)
        print("bottom:")
        print(self.botton)
        print

    def printCube(self):
        u = self.upper
        l = self.left
        f = self.front
        r = self.right
        d = self.botton
        b = self.back
        print
        print("Actual position:")
        print
        print("            |"+u[0][0]+"|"+u[0][1]+"|"+u[0][2]+"|")
        print
        print("            |"+u[1][0]+"|"+u[1][1]+"|"+u[1][2]+"|")
        print
        print("            |"+u[2][0]+"|"+u[2][1]+"|"+u[2][2]+"|")
        print("             --- --- ---")
        print("|"+l[0][0]+"|"+l[0][1]+"|"+l[0][2]+"|"+f[0][0]+"|"+f[0][1]+"|"+f[0][2]+"|"+r[0][0]+"|"+r[0][1]+"|"+r[0][2]+"|")
        print
        print("|"+l[1][0]+"|"+l[1][1]+"|"+l[1][2]+"|"+f[1][0]+"|"+f[1][1]+"|"+f[1][2]+"|"+r[1][0]+"|"+r[1][1]+"|"+r[1][2]+"|")
        print
        print("|"+l[2][0]+"|"+l[2][1]+"|"+l[2][2]+"|"+f[2][0]+"|"+f[2][1]+"|"+f[2][2]+"|"+r[2][0]+"|"+r[2][1]+"|"+r[2][2]+"|")
        print("             --- --- ---")
        print("            |"+d[0][0]+"|"+d[0][1]+"|"+d[0][2]+"|")
        print
        print("            |"+d[1][0]+"|"+d[1][1]+"|"+d[1][2]+"|")
        print
        print("            |"+d[2][0]+"|"+d[2][1]+"|"+d[2][2]+"|")
        print("             --- --- ---")
        print("            |"+b[2][2]+"|"+b[2][1]+"|"+b[2][0]+"|")
        print
        print("            |"+b[1][2]+"|"+b[1][1]+"|"+b[1][0]+"|")
        print
        print("            |"+b[0][2]+"|"+b[0][1]+"|"+b[0][0]+"|")
        print
 

    def shuffle(self):
        moves = ['r','l','u','d','f','b','ri','li','ui','di','fi','bi']
        for i in xrange(0, 20):
            moveidx = random.randint(0, len(moves) - 1)
            self.rotate(moves[moveidx])
    
    def isDone(self):
        done = True
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.front[i, j] != self.W:
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.back[i, j] != self.Y:
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.left[i, j] != self.O:
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.right[i, j] != self.R:
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.upper[i, j] != self.B:
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.botton[i, j] != self.G:
                    done = False
        return done

    def rotate(self, comms):
        comms = comms.split(" ")
        for comm in comms:
            face = comm[0]
            clockwise = 'y'
            if len(comm) == 2 and comm[1] == 'i':
                clockwise = 'n'
            if face == 'u':
                aux0 = self.left[0][0]
                aux1 = self.left[0][1]
                aux2 = self.left[0][2]
                auxc = self.upper[0][0]
                auxb = self.upper[0][1]
                #print('ROTATE FRONT'),
                if clockwise == 'y':
                    #print('CLOCKWISE')
                    # face corners
                    self.upper[0][0] = self.upper[2][0]
                    self.upper[2][0] = self.upper[2][2]
                    self.upper[2][2] = self.upper[0][2]
                    self.upper[0][2] = auxc
                    # face borders
                    self.upper[0][1] = self.upper[1][0]
                    self.upper[1][0] = self.upper[2][1]
                    self.upper[2][1] = self.upper[1][2]
                    self.upper[1][2] = auxb

                    self.left[0][0] = self.front[0][0]
                    self.left[0][1] = self.front[0][1]
                    self.left[0][2] = self.front[0][2]
                    self.front[0][0] = self.right[0][0]
                    self.front[0][1] = self.right[0][1]
                    self.front[0][2] = self.right[0][2]
                    self.right[0][0] = self.back[0][0]
                    self.right[0][1] = self.back[0][1]
                    self.right[0][2] = self.back[0][2]
                    self.back[0][0] = aux0
                    self.back[0][1] = aux1
                    self.back[0][2] = aux2
                else:
                    #print('COUNTER-CLOCKWISE')
                    # face corners
                    self.upper[0][0] = self.upper[0][2]
                    self.upper[0][2] = self.upper[2][2]
                    self.upper[2][2] = self.upper[2][0]
                    self.upper[2][0] = auxc
                    # face borders
                    self.upper[0][1] = self.upper[1][2]
                    self.upper[1][2] = self.upper[2][1]
                    self.upper[2][1] = self.upper[1][0]
                    self.upper[1][0] = auxb

                    self.left[0][0] = self.back[0][0]
                    self.left[0][1] = self.back[0][1]
                    self.left[0][2] = self.back[0][2]
                    self.back[0][0] = self.right[0][0]
                    self.back[0][1] = self.right[0][1]
                    self.back[0][2] = self.right[0][2]
                    self.right[0][0] = self.front[0][0]
                    self.right[0][1] = self.front[0][1]
                    self.right[0][2] = self.front[0][2]
                    self.front[0][0] = aux0
                    self.front[0][1] = aux1
                    self.front[0][2] = aux2
            if face == 'f':
                aux0 = self.left[0][2]
                aux1 = self.left[1][2]
                aux2 = self.left[2][2]
                auxc = self.front[0][0]
                auxb = self.front[0][1]
                #print('ROTATE FRONT'),
                if clockwise == 'y':
                    #print('CLOCKWISE')
                    # face corners
                    self.front[0][0] = self.front[2][0]
                    self.front[2][0] = self.front[2][2]
                    self.front[2][2] = self.front[0][2]
                    self.front[0][2] = auxc
                    # face borders
                    self.front[0][1] = self.front[1][0]
                    self.front[1][0] = self.front[2][1]
                    self.front[2][1] = self.front[1][2]
                    self.front[1][2] = auxb

                    self.left[0][2] = self.botton[0][0]
                    self.left[1][2] = self.botton[0][1]
                    self.left[2][2] = self.botton[0][2]
                    self.botton[0][0] = self.right[2][0]
                    self.botton[0][1] = self.right[1][0]
                    self.botton[0][2] = self.right[0][0]
                    self.right[0][0] = self.upper[2][0]
                    self.right[1][0] = self.upper[2][1]
                    self.right[2][0] = self.upper[2][2]
                    self.upper[2][0] = aux2
                    self.upper[2][1] = aux1
                    self.upper[2][2] = aux0
                else:
                    #print('COUNTER-CLOCKWISE')
                    # face corners
                    self.front[0][0] = self.front[0][2]
                    self.front[0][2] = self.front[2][2]
                    self.front[2][2] = self.front[2][0]
                    self.front[2][0] = auxc
                    # face borders
                    self.front[0][1] = self.front[1][2]
                    self.front[1][2] = self.front[2][1]
                    self.front[2][1] = self.front[1][0]
                    self.front[1][0] = auxb

                    self.left[0][2] = self.upper[2][2]
                    self.left[1][2] = self.upper[2][1]
                    self.left[2][2] = self.upper[2][0]
                    self.upper[2][0] = self.right[0][0]
                    self.upper[2][1] = self.right[1][0]
                    self.upper[2][2] = self.right[2][0]
                    self.right[0][0] = self.botton[0][2]
                    self.right[1][0] = self.botton[0][1]
                    self.right[2][0] = self.botton[0][0]
                    self.botton[0][0] = aux0
                    self.botton[0][1] = aux1
                    self.botton[0][2] = aux2
            if face == 'l':
                aux0 = self.back[0][2]
                aux1 = self.back[1][2]
                aux2 = self.back[2][2]
                auxc = self.left[0][0]
                auxb = self.left[0][1]
                #print('ROTATE LEFT'),
                if clockwise == 'y':
                    #print('CLOCKWISE')
                    # face corners
                    self.left[0][0] = self.left[2][0]
                    self.left[2][0] = self.left[2][2]
                    self.left[2][2] = self.left[0][2]
                    self.left[0][2] = auxc
                    # face borders
                    self.left[0][1] = self.left[1][0]
                    self.left[1][0] = self.left[2][1]
                    self.left[2][1] = self.left[1][2]
                    self.left[1][2] = auxb

                    self.back[0][2] = self.botton[2][0]
                    self.back[1][2] = self.botton[1][0]
                    self.back[2][2] = self.botton[0][0]
                    self.botton[0][0] = self.front[0][0]
                    self.botton[1][0] = self.front[1][0]
                    self.botton[2][0] = self.front[2][0]
                    self.front[0][0] = self.upper[0][0]
                    self.front[1][0] = self.upper[1][0]
                    self.front[2][0] = self.upper[2][0]
                    self.upper[0][0] = aux2
                    self.upper[1][0] = aux1
                    self.upper[2][0] = aux0
                else:
                    #print('COUNTER-CLOCKWISE')
                    # face corners
                    self.left[0][0] = self.left[0][2]
                    self.left[0][2] = self.left[2][2]
                    self.left[2][2] = self.left[2][0]
                    self.left[2][0] = auxc
                    # face borders
                    self.left[0][1] = self.left[1][2]
                    self.left[1][2] = self.left[2][1]
                    self.left[2][1] = self.left[1][0]
                    self.left[1][0] = auxb

                    self.back[0][2] = self.upper[2][0]
                    self.back[1][2] = self.upper[1][0]
                    self.back[2][2] = self.upper[0][0]
                    self.upper[0][0] = self.front[0][0]
                    self.upper[1][0] = self.front[1][0]
                    self.upper[2][0] = self.front[2][0]
                    self.front[0][0] = self.botton[0][0]
                    self.front[1][0] = self.botton[1][0]
                    self.front[2][0] = self.botton[2][0]
                    self.botton[0][0] = aux2
                    self.botton[1][0] = aux1
                    self.botton[2][0] = aux0
            if face == 'r':
                aux0 = self.front[0][2]
                aux1 = self.front[1][2]
                aux2 = self.front[2][2]
                auxc = self.right[0][0]
                auxb = self.right[0][1]
                #print('ROTATE RIGHT'),
                if clockwise == 'y':
                    #print('CLOCKWISE')
                    # face corners
                    self.right[0][0] = self.right[2][0]
                    self.right[2][0] = self.right[2][2]
                    self.right[2][2] = self.right[0][2]
                    self.right[0][2] = auxc
                    # face borders
                    self.right[0][1] = self.right[1][0]
                    self.right[1][0] = self.right[2][1]
                    self.right[2][1] = self.right[1][2]
                    self.right[1][2] = auxb

                    self.front[0][2] = self.botton[0][2]
                    self.front[1][2] = self.botton[1][2]
                    self.front[2][2] = self.botton[2][2]
                    self.botton[0][2] = self.back[2][0]
                    self.botton[1][2] = self.back[1][0]
                    self.botton[2][2] = self.back[0][0]
                    self.back[0][0] = self.upper[2][2]
                    self.back[1][0] = self.upper[1][2]
                    self.back[2][0] = self.upper[0][2]
                    self.upper[0][2] = aux0
                    self.upper[1][2] = aux1
                    self.upper[2][2] = aux2
                else:
                    #print('COUNTER-CLOCKWISE')
                    # face corners
                    self.right[0][0] = self.right[0][2]
                    self.right[0][2] = self.right[2][2]
                    self.right[2][2] = self.right[2][0]
                    self.right[2][0] = auxc
                    # face borders
                    self.right[0][1] = self.right[1][2]
                    self.right[1][2] = self.right[2][1]
                    self.right[2][1] = self.right[1][0]
                    self.right[1][0] = auxb

                    self.front[0][2] = self.upper[0][2]
                    self.front[1][2] = self.upper[1][2]
                    self.front[2][2] = self.upper[2][2]
                    self.upper[0][2] = self.back[2][0]
                    self.upper[1][2] = self.back[1][0]
                    self.upper[2][2] = self.back[0][0]
                    self.back[0][0] = self.botton[2][2]
                    self.back[1][0] = self.botton[1][2]
                    self.back[2][0] = self.botton[0][2]
                    self.botton[0][2] = aux0
                    self.botton[1][2] = aux1
                    self.botton[2][2] = aux2
            if face == 'd':
                aux0 = self.left[2][0]
                aux1 = self.left[2][1]
                aux2 = self.left[2][2]
                auxc = self.botton[0][0]
                auxb = self.botton[0][1]
                #print('ROTATE FRONT'),
                if clockwise == 'y':
                    #print('CLOCKWISE')
                    # face corners
                    self.botton[0][0] = self.botton[2][0]
                    self.botton[2][0] = self.botton[2][2]
                    self.botton[2][2] = self.botton[0][2]
                    self.botton[0][2] = auxc
                    # face borders
                    self.botton[0][1] = self.botton[1][0]
                    self.botton[1][0] = self.botton[2][1]
                    self.botton[2][1] = self.botton[1][2]
                    self.botton[1][2] = auxb

                    self.left[2][0] = self.back[2][0]
                    self.left[2][1] = self.back[2][1]
                    self.left[2][2] = self.back[2][2]
                    self.back[2][0] = self.right[2][0]
                    self.back[2][1] = self.right[2][1]
                    self.back[2][2] = self.right[2][2]
                    self.right[2][0] = self.front[2][0]
                    self.right[2][1] = self.front[2][1]
                    self.right[2][2] = self.front[2][2]
                    self.front[2][0] = aux0
                    self.front[2][1] = aux1
                    self.front[2][2] = aux2
                else:
                    #print('COUNTER-CLOCKWISE')
                    # face corners
                    self.botton[0][0] = self.botton[0][2]
                    self.botton[0][2] = self.botton[2][2]
                    self.botton[2][2] = self.botton[2][0]
                    self.botton[2][0] = auxc
                    # face borders
                    self.botton[0][1] = self.botton[1][2]
                    self.botton[1][2] = self.botton[2][1]
                    self.botton[2][1] = self.botton[1][0]
                    self.botton[1][0] = auxb

                    self.left[2][0] = self.front[2][0]
                    self.left[2][1] = self.front[2][1]
                    self.left[2][2] = self.front[2][2]
                    self.front[2][0] = self.right[2][0]
                    self.front[2][1] = self.right[2][1]
                    self.front[2][2] = self.right[2][2]
                    self.right[2][0] = self.back[2][0]
                    self.right[2][1] = self.back[2][1]
                    self.right[2][2] = self.back[2][2]
                    self.back[2][0] = aux0
                    self.back[2][1] = aux1
                    self.back[2][2] = aux2
            if face == 'b':
                aux0 = self.left[0][0]
                aux1 = self.left[1][0]
                aux2 = self.left[2][0]
                auxc = self.back[0][0]
                auxb = self.back[0][1]
                #print('ROTATE FRONT'),
                if clockwise == 'y':
                    #print('CLOCKWISE')
                    # face corners
                    self.back[0][0] = self.back[2][0]
                    self.back[2][0] = self.back[2][2]
                    self.back[2][2] = self.back[0][2]
                    self.back[0][2] = auxc
                    # face borders
                    self.back[0][1] = self.back[1][0]
                    self.back[1][0] = self.back[2][1]
                    self.back[2][1] = self.back[1][2]
                    self.back[1][2] = auxb

                    self.left[0][0] = self.upper[0][2]
                    self.left[1][0] = self.upper[0][1]
                    self.left[2][0] = self.upper[0][0]
                    self.upper[0][0] = self.right[0][2]
                    self.upper[0][1] = self.right[1][2]
                    self.upper[0][2] = self.right[2][2]
                    self.right[0][2] = self.botton[2][2]
                    self.right[1][2] = self.botton[2][1]
                    self.right[2][2] = self.botton[2][0]
                    self.botton[2][0] = aux0
                    self.botton[2][1] = aux1
                    self.botton[2][2] = aux2
                else:
                    #print('COUNTER-CLOCKWISE')
                    # face corners
                    self.back[0][0] = self.back[0][2]
                    self.back[0][2] = self.back[2][2]
                    self.back[2][2] = self.back[2][0]
                    self.back[2][0] = auxc
                    # face borders
                    self.back[0][1] = self.back[1][2]
                    self.back[1][2] = self.back[2][1]
                    self.back[2][1] = self.back[1][0]
                    self.back[1][0] = auxb

                    self.left[0][0] = self.botton[2][0]
                    self.left[1][0] = self.botton[2][1]
                    self.left[2][0] = self.botton[2][2]
                    self.botton[2][0] = self.right[2][2]
                    self.botton[2][1] = self.right[1][2]
                    self.botton[2][2] = self.right[0][2]
                    self.right[0][2] = self.upper[0][0]
                    self.right[1][2] = self.upper[0][1]
                    self.right[2][2] = self.upper[0][2]
                    self.upper[0][0] = aux2
                    self.upper[0][1] = aux1
                    self.upper[0][2] = aux0