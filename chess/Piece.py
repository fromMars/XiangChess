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
        self.__selected = False
        
        
    def Kill(self):
        pass
    
    
    def Killed(self):
        self.isKilled = True
    
    
    def Select(self, window):
        #window.clear()
        if self.__selected == False:
            self.__selected = True
            self.ChangeColor()
            self.ShowPiece()
        else:
            self.__selected = False
            self.ChangeColor()
            self.ShowPiece()
    
    
    def Move(self, x, y, window):
        window.clear()
        if self.__selected == False:
            pass
        else:
            self.__target_position = [x, y]
            self.current_position = self.__target_position
            self.target_position = []
            self.PreparePiece(self.__name)
            self.ShowPiece()
            self.__selected = False
    
    

if __name__ == "__main__":
    window = pyglet.window.Window()
    p = Piece("象", 100, 100)
    
    @window.event()
    def on_mouse_press(x, y, button, modifiers):
        if x in range(p.current_position[0] - 12, p.current_position[0] + 12) \
        and y in range(p.current_position[1] - 12, p.current_position[1] + 12):
            p.Select(window)
            window.clear()
        else:
            p.Move(x, y, window)

    
    @window.event()
    def on_draw():
        p.ShowPiece()

    
    pyglet.app.run()