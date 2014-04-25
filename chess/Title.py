# coding=utf-8
import pyglet



class Title:
    def __init__(self, name, x, y):
        self.title = None
        self.__size = 12
        self.__color = [(255, 0, 0, 255), (0, 0, 0, 255)]
        self.__center_position = [x, y]
        self.__PrepareTitle(name)
    
    
    def __PrepareTitle(self, name):
        self.title = pyglet.text.Label(name, 
                                       font_name = 'msyh', 
                                       font_size = self.__size, 
                                       bold = True,
                                       color = self.__color[0],
                                       anchor_x = 'center',
                                       anchor_y = 'center',
                                       x=self.__center_position[0], 
                                       y=self.__center_position[1])
        
        
        
if __name__ == "__main__":
    window = pyglet.window.Window()
    t = Title("象", 100, 100)
    @window.event()
    def on_draw():
        t.title.draw()

        
    pyglet.app.run()