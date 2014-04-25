# coding=utf-8
import pyglet
import BaseBoard



class Board:
    def __init__(self):
        self.origin_position = [240, 110]
        self.board = BaseBoard.BaseBoard(self.origin_position)
        
        
    def ShowBoard(self):
        self.board.DrawBoard()
    
    

if __name__ == "__main__":
    window = pyglet.window.Window()
    board = Board()
    
    @window.event()
    def on_draw():
        board.ShowBoard()
    
    pyglet.app.run()