# -*- coding: utf-8 -*-
import pyglet
import BasePiece



class Piece(BasePiece.BasePiece):
    def __init__(self, name, x, y):
        self.__name = name
        self.current_position = [x, y]
        self.__target_position = []
        self.isKilled = False
        self.__position_history = []
        self.PreparePiece(name)
        
        
    def Kill(self):
        pass
    
    
    def Killed(self):
        self.isKilled = True
    
    
    def Move(self, x, y, window):
        window.clear()
        self.__target_position = [x, y]
        self.current_position = self.__target_position
        self.target_position = []
        self.PreparePiece(self.__name)
        self.ShowPiece()
    
    

if __name__ == "__main__":
    window = pyglet.window.Window()
    p = Piece("象", 100, 100)
    
    @window.event()
    def on_mouse_press(x, y, button, modifiers):
        p.Move(x, y, window)
    
    @window.event()
    def on_draw():
        p.ShowPiece()

    
    pyglet.app.run()