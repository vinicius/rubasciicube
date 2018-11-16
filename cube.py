import numpy as np
import random

class Cube:
    # The faces must be read in the sense: left-rigth, up-down
    def __init__(self):
        self.front = np.array([['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']])
        self.back = np.array([['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']])
        self.left = np.array([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']])
        self.right = np.array([['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']])
        self.upper = np.array([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']])
        self.botton = np.array([['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']])

    def printCube(self):
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

    def shuffle(self):
        moves = ['r','l','u','d','f','b','ri','li','ui','di','fi','bi']
        for i in xrange(0, 20):
            moveidx = random.randint(0, len(moves) - 1)
            self.rotate(moves[moveidx])
    
    def isDone(self):
        done = True
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.front[i, j] != 'W':
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.back[i, j] != 'Y':
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.left[i, j] != 'O':
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.right[i, j] != 'R':
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.upper[i, j] != 'B':
                    done = False
        for i in xrange(0, 2):
            for j in xrange(0, 2):
                if self.botton[i, j] != 'G':
                    done = False
        return done

    def rotate(self, comms):
        comms = comms.split(" ")
        for comm in comms:
            face = comm[0]
            clockwise = 'y'
            if len(comm) == 2 and comm[1] == 'i':
                clockwise = 'n'
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