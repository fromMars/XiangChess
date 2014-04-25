# coding=utf-8
import pyglet
import Circle
import Title



class BasePiece:
    def __init__(self, name, x, y):
        self.current_position = [x, y]
        self.PreparePiece(name)
    
    
    def PreparePiece(self, name):
        self.circle = Circle.Circle(self.current_position[0], 
                                    self.current_position[1])
        self.title = Title.Title(name, 
                                 self.current_position[0], 
                                 self.current_position[1])
        
    def ShowPiece(self):
        self.circle.circle_batch.draw()
        self.title.title.draw()
        
    
    def ChangeColor(self):
        self.circle.ChangeColor()
        
    
    
if __name__ == "__main__":
    window = pyglet.window.Window()
    p = BasePiece(u"象", 100, 100)
    
    @window.event()
    def on_draw():
        p.ShowPiece()
    
    pyglet.app.run()