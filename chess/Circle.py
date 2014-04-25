# coding=utf-8
import pyglet
import math


class Circle:
    def __init__(self, x, y):
        self.circle_batch = pyglet.graphics.Batch()
        self.__center_position = [x, y]
        self.__radius = 12
        self.__color = 235, 229, 209
        self.__n = 100
        self.__vertex_circle = []
        self.__PrepareCircle()
        
        
    def __PrepareCircle(self):
        tmp_color = []
        for i in range(self.__n):
            self.__vertex_circle.append(self.__center_position[0] + self.__radius * 
                                        math.cos(2 * math.pi / self.__n * i))
            self.__vertex_circle.append(self.__center_position[1] + self.__radius * 
                                        math.sin(2 * math.pi / self.__n * i))
            tmp_color.append(self.__color[0])
            tmp_color.append(self.__color[1])
            tmp_color.append(self.__color[2])
        self.circle_batch.add(100, pyglet.gl.GL_TRIANGLE_FAN, None, 
                              ('v2f', self.__vertex_circle), ('c3B', tmp_color))


    def ChangeColor(self):
        if self.__color == (235, 229, 209):
            self.__color = (100, 100, 100)
        else:
            self.__color = (235, 229, 209)
        self.circle_batch = pyglet.graphics.Batch()
        self.__vertex_circle = []
        self.__PrepareCircle()
        
        
        
if __name__ == "__main__":
    window = pyglet.window.Window()
    c = Circle(100, 100)
    
    @window.event()
    def on_draw():
        window.clear()
        c.circle_batch.draw()
        
    pyglet.app.run()