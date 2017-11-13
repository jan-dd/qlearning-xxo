from __future__ import print_function
import numpy as np
from qlearning4k.games.game import Game

class xxoboard(Game):
    def __init__(self,opponent,drawmode=False):
        self.opponent=opponent
        self.drawmode=drawmode
        self.reset()

    def reset(self):
        self.state=[0,0,0,0,0,0,0,0,0]
        self.winner=0
        self.forbidden=False
        self.over=False
        if self.drawmode:
            print("********************************************")

    def __getitem__(self,tup):
        i,j=tup
        return self.state[3*i+j]

    def __setitem__(self,tup,val):
        i,j=tup
        self.state[3*i+j]=val

    @property
    def nb_actions(self):
        return 9

    def play(self, action):
        if self.state[action]!=0:
            print("Tried a forbidden move. Game over.")
            self.forbidden=True
        else:
            self.state[action]=1
            if self.drawmode:
                self.draw()
            if not self.is_over():
                self.opponent(self)
        if self.drawmode:
            self.draw()


    def draw(self):
        print("-------------")
        for i in range(0,3):
            print("| ", end='')
            for j in range(0,3):
                if self[i,j]==1:
                    print("x | ", end='')
                elif self[i,j]==-1:
                    print("o | ", end='')
                else:
                    print("  | ", end='')
            print("")
            print("-------------")

    def is_over(self):
        if self.over:
            return True



        if self.forbidden:
            return True

        for i in range(0,3):
            if self[i,0]!=0:
                if self[i,0]==self[i,1] and self[i,1]==self[i,2]:
                    self.winner=self[i,0]
            if self[0,i]!=0:
                if self[0,i]==self[1,i] and self[1,i]==self[2,i]:
                    self.winner=self[0,i]
        if self[1,1] != 0:
            if self[0,0]==self[1,1] and self[1,1]==self[2,2]:
                self.winner=self[1,1]
            if self[0,2]==self[1,1] and self[1,1]==self[2,0]:
                self.winner=self[1,1]

        if 0 not in self.state:
            self.over=True
            return True

        if self.winner!=0:
            self.over=True
            if self.drawmode:
                if self.winner==1:
                    print("*** ---> x wins! <--- ***")
                elif self.winner==-1:
                    print("*** ---> o wins! <--- ***")
            return True
        else:
            return False

    def get_score(self):
        if self.forbidden:
            return -5
        if self.is_over():
            if self.winner==1:
                return 5
            elif self.winner==-1:
                return -5
            else:
                return 1
        return 0

    def get_state(self):
        return np.array([s==1 for s in self.state]+[s==-1 for s in self.state]+[s==0 for s in self.state])


    def is_won(self):
        return self.winner==1


def int_opponent(b):
    player=-1
    while True:
        move=int(raw_input("Type number (1-9) for a move: "))-1
        if b.state[move]!=0:
            print("Bad move, repeat.")
        else:
            b.state[move]=player
            return

def rand_opponent(b):
    player=-1
    retry=True
    while retry:
        x=np.random.randint(3)
        y=np.random.randint(3)
        if b[x,y]==0:
            b[x,y]=player
            retry=False

def mod_opponent(b):
    player=-1
    for i in range(0,3):
        s=0
        for j in range(0,3):
            s+=b[i,j]
        if abs(s) > 1:
            for j in range(0,3):
                if b[i,j]==0:
                    b[i,j]=-1
                    return

    for i in range(0,3):
        s=0
        for j in range(0,3):
            s+=b[j,i]
        if abs(s) > 1:
            for j in range(0,3):
                if b[j,i]==0:
                    b[j,i]=-1
                    return

    s=0
    for i in range(0,3):
        s+=b[i,i]
    if abs(s) > 1:
        for i in range(0,3):
            if b[i,i]==0:
                b[i,i]=-1
                return

    rand_opponent(b)

def smart_opponent(b):
    player=-1
    # try to win
    for i in range(0,3):
        s=0
        for j in range(0,3):
            s+=b[i,j]
        if (s) > 1:
            for j in range(0,3):
                if b[i,j]==0:
                    b[i,j]=-1
                    return

    for i in range(0,3):
        s=0
        for j in range(0,3):
            s+=b[j,i]
        if (s) > 1:
            for j in range(0,3):
                if b[j,i]==0:
                    b[j,i]=-1
                    return

    s=0
    for i in range(0,3):
        s+=b[i,i]
    if (s) > 1:
        for i in range(0,3):
            if b[i,i]==0:
                b[i,i]=-1
                return

    # now try to avoid opponent winning
    mod_opponent(b)
