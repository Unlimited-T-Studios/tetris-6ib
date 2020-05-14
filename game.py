import pygame
pygame.font.init()
import random





def main():
    global grid
    
    locked_positions = {}  # (x,y):(255,0,0)
    #grid = create_grid(locked_positions)

    change_piece = False
    run = True
    #current_piece = get_shape()
    #next_piece = get_shape()
    #clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #current_piece.x -= 1
                    #if not valid_space(current_piece, grid):
                    #    current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    #current_piece.x += 1
                    #if not valid_space(current_piece, grid):
                    #    current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    #current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    #if not valid_space(current_piece, grid):
                    #    current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    # move shape down
                    #current_piece.y += 1
                    #if not valid_space(current_piece, grid):
                    #    current_piece.y -= 1

        draw_window(win)
        



