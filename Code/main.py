import flappy_pong
import menu
import pong
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 450))
    pygame.display.set_caption("Pong")
    menu.title_screen(screen)
    while True:
        mode = menu.game_mode_screen(screen)
        if mode == "flappy":
            result = flappy_pong.flappy_pong(screen)
        if mode == "classic":
            result = pong.classic_pong(screen, menu.two_player_or_not(screen))
        menu.end_screen(screen, result)


if __name__ == "__main__":
    main()
