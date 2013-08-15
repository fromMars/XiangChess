# -*- coding: utf-8 -*-  
import pyglet



class BaseBoard:
    def __init__(self, orig_pos):
        self.__board_batch = pyglet.graphics.Batch()
        #棋盘背景色及线条颜色、左下角坐标、格子间距
        self.__bgcolor = (255, 255, 255)
        self.__linecolor = (0, 0, 0, 0, 0, 0)
        self.__origin_position = orig_pos
        self.__vertical_spacing = 30
        self.__horizontal_spacing = 30
        #坐标对照表
        self.pos_table = []
        
        #填充棋盘batch
        self.__create_board(self.__origin_position[0], self.__origin_position[1])
        self.__create_board(self.__origin_position[0],
                            self.__vertical_spacing * 5 + self.__origin_position[1])
        self.__create_crosslines(self.__origin_position[0], self.__origin_position[1])
        self.__create_gap(self.__origin_position[0], self.__origin_position[1],
                          8 * self.__horizontal_spacing + self.__origin_position[0],
                          self.__vertical_spacing)
        self.__create_text(self.__origin_position[0], 4 * self.__vertical_spacing)
        
    
    def __create_board(self, x_orig=200, y_orig=50):
        x_enl = self.__horizontal_spacing
        y_enl = self.__vertical_spacing
        x_right = 8 * x_enl + x_orig
        y_top = 4 * y_enl + y_orig

        for i in range(0, 9):
            x = i * x_enl + x_orig
            self.__board_batch.add(2, pyglet.gl.GL_LINES, None,
                                 ('v2i', (x, y_orig, x, y_top)),
                                 ('c3B', self.__linecolor))
            for j in range(0, 5):
                y = j * y_enl + y_orig
                self.__board_batch.add(2, pyglet.gl.GL_LINES, None,
                                     ('v2i', (x_orig, y, x_right, y)),
                                     ('c3B', self.__linecolor))
    
    
    def __create_text(self, x, y):
        color = [0, 0, 0, 255]
        self.__chuhe = pyglet.text.Label('楚河', font_name='msyh',
                                      font_size=12, bold=True,
                                      color=color,
                                      anchor_x='center',
                                      anchor_y='center',
                                      x = x + 2 * self.__horizontal_spacing,
                                      y = y + self.__origin_position[1] + self.__vertical_spacing / 2)
        self.__hanjie = pyglet.text.Label('漢界', font_name='msyh',
                                      font_size=12, bold=True,
                                      color=color,
                                      anchor_x='center',
                                      anchor_y='center',
                                      x = x + 6 * self.__horizontal_spacing,
                                      y = y + self.__origin_position[1] + self.__vertical_spacing / 2)
                   
                                     
    def __create_gap(self, x_orig, y_orig, x_right, y_enl):
        vertex_edge = (x_orig, 5 * y_enl + y_orig,
                       x_orig, 4 * y_enl + y_orig,
                       x_right, 4 * y_enl + y_orig,
                       x_right, 5 * y_enl + y_orig)
        vertex_edge_color = (0, 0, 0, 0,
                             0, 0, 0, 0,
                             0, 0, 0, 0,
                             0, 0, 0, 0)
        self.__board_batch.add(4, pyglet.gl.GL_LINE_LOOP, None,
                             ('v2i', vertex_edge), ('c4B', vertex_edge_color))
    
    
    def __create_crosslines(self, x_orig=200, y_orig=50):
        left0   =   3 * self.__horizontal_spacing + x_orig
        right0  =   5 * self.__horizontal_spacing + x_orig
        bottom0 =   y_orig
        top0    =   2 * self.__vertical_spacing + y_orig
        
        left1   =   3 * self.__horizontal_spacing + x_orig
        right1  =   5 * self.__horizontal_spacing + x_orig
        bottom1 =   y_orig + 7 * self.__vertical_spacing
        top1    =   2 * self.__vertical_spacing + y_orig + 7 * self.__vertical_spacing
         
        self.__board_batch.add(2, pyglet.gl.GL_LINES, None,
                                 ('v2i', (left0, bottom0, right0, top0)),
                                 ('c3B', self.__linecolor))
        self.__board_batch.add(2, pyglet.gl.GL_LINES, None,
                                 ('v2i', (left0, top0, right0, bottom0)),
                                 ('c3B', self.__linecolor))
        self.__board_batch.add(2, pyglet.gl.GL_LINES, None,
                                 ('v2i', (left1, bottom1, right1, top1)),
                                 ('c3B', self.__linecolor))
        self.__board_batch.add(2, pyglet.gl.GL_LINES, None,
                                 ('v2i', (left1, top1, right1, bottom1)),
                                 ('c3B', self.__linecolor))
        
        
    def __fill_pos_table(self):
        pass
        
        
    def DrawBoard(self):
        self.__board_batch.draw()
        self.__chuhe.draw()
        self.__hanjie.draw()



def main():
    window = pyglet.window.Window()
    board = BaseBoard()
    
    @window.event()
    def on_draw():
        board.DrawBoard()
        
    pyglet.app.run()
    

if __name__ == "__main__":
    main()
