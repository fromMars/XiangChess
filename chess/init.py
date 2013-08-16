import pyglet
import Board
import Piece


if __name__ == "__main__":
    window = pyglet.window.Window()
    #����ɫ
    bgcolor = (255, 255, 255, 255)
    pyglet.gl.glClearColor(*bgcolor)
    #��������
    board = Board.Board()
    #��������
    piece = Piece.Piece("��", 100, 100)
    
    @window.event()
    def on_mouse_press(x, y, button, modifiers):
        piece.Move(x, y, window)
    
    @window.event()
    def on_draw():
        window.clear()
        board.ShowBoard()
        piece.ShowPiece()
        
        
    pyglet.app.run()
    