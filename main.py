import random
import pygame
import sys
import time

class Element:
    def __init__(self):
        self.val = 0
    def setVal(self, val):
        self.val = val
    def delVal(self):
        self.val = 0
    def getVal(self):
        return self.val

class Board:
    def __init__(self):
        self.board = [[],[],[],[]]
        self.prevBoard = [[],[],[],[]]
        for x in range(0,4):
            for y in range(0, 4):
                self.board[y].append(Element())
                self.prevBoard.append(Element())
    def randomizeElement(self):
        #losowanie nowego elementu
        x = random.randint(0,3)
        y = random.randint(0,3)
        while self.board[y][x].getVal() != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.board[y][x].setVal(random.randint(1,2)*2)
    def right(self):
        self.copyTable()
        for z in range(0,3):
            for x in range(0,3):
                for y in range(0,4):
                    x = 2-x
                    if self.board[y][x+1].getVal()==0:
                        self.board[y][x+1].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board [y][x].getVal() == self.board[y][x+1].getVal():
                        self.board[y][x+1].setVal(self.board[y][x].getVal()*2)
                        self.board[y][x].delVal()
        for x in range(0,4):
            for y in range(0,4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True
        return False
    def left(self):
        self.copyTable()
        for z in range (0,3):
            for x in range (1,4):
                for y in range (0,4):
                    if self.board[y][x-1].getVal() ==0:
                        self.board[y][x-1].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() ==self.board[y][x-1].getVal():
                        self.board[y][x].setVal(self.board[y][x].getVal()*2)
                        self.board[y][x].delVal()
        for x in range(0,4):
            for y in range (0,4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True
        return False
    def up(self):
        self.copyTable()
        for z in range(0,3):
            for x in range(0,4):
                for y in range(1,4):
                    if self.board[y-1][x].getVal()== 0:
                        self.board[y-1][x].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal()==self.board[y-1][x].getVal():
                        self.board[y-1][x].setVal(self.board[y][x].getVal()*2)
                        self.board[y][x].delVal()

    def down(self):
    def getTable(self):
        return self.board
    def copyTable(self):
        for x in range(0,4):
            for y in range(0,4):
                self.prevBoard[y][x].setVal(self.board[y][x].getVal())

class Game:
    def __init__(self):
    def draw(self, table):
    def run(self, board):



