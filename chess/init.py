# coding=utf-8
import pyglet
import Board
import Piece



if __name__ == "__main__":
    window = pyglet.window.Window()

    bgcolor = (255, 255, 255, 255)
    pyglet.gl.glClearColor(*bgcolor)
    
    board = Board.Board()
    piece = Piece.Piece(u"象", 100, 100)
    
    
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
    