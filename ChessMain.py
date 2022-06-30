import pygame as p
WIDTH = HEIGHT = 512
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}
'''
board is an 8x8 2d list, each element of the list has 2 characters,
The 1st character represents the color of the piece, 'b' or 'w'
The 2nd character represents the type of the piece, 'K', 'Q', 'R', 'B', 'N', 'P' 
'--' represents an empty space with no piece
'''
board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
         ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_board(screen, board)
        p.display.flip()

'''
 Draw board and peices on top of the board'''
def draw_board(screen, board):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()