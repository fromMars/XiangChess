import pyglet
import Board
import Piece



if __name__ == "__main__":
    window = pyglet.window.Window()
    #背景色
    bgcolor = (255, 255, 255, 255)
    pyglet.gl.glClearColor(*bgcolor)
    #创建棋盘
    board = Board.Board()
    #创建棋子
    piece = Piece.Piece("象", 100, 100)
    
    @window.event()
    def on_mouse_press(x, y, button, modifiers):
        if x in range(piece.current_position[0] - 12, piece.current_position[0] + 12) \
        and y in range(piece.current_position[1] - 12, piece.current_position[1] + 12):
            piece.Select(window)
            window.clear()
        else:
            piece.Move(x, y, window)
    
    @window.event()
    def on_draw():
        window.clear()
        board.ShowBoard()
        piece.ShowPiece()
        
        
    pyglet.app.run()
    