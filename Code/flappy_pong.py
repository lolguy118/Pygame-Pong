# Create a blank screen 800 x 450
# Allow the user to exit without error
# Make the maximum FPS to 60
# Import all pong assets and convert them
# Make the paddles move and switch direction
# Make the ball move. Have it switch directions if the player clicks or it hits a paddle
#   If it misses a paddle, just have it loop back around
# Draw a line or smthng idk

import pygame
from random import choice

pygame.init()

screen = pygame.display.set_mode((800, 450))
clock = pygame.time.Clock()
game_running = True
pygame.display.set_caption("Pong")

font_path = r"..\assets\Teko-VariableFont_wght.ttf"
font = pygame.font.Font(font_path, 50)


board_path = r"..\assets\Board.png"
board_surf = pygame.image.load(board_path)

scorebar_path = r"..\assets\ScoreBar.png"
scorebar_surf = pygame.image.load(scorebar_path).convert_alpha()
right_scorebar_surf = pygame.transform.flip(scorebar_surf, True, False)
left_scorebar_rect = scorebar_surf.get_rect(topleft=(0, 0))
right_scorebar_rect = right_scorebar_surf.get_rect(topright=(800, 0))

player_path = r"..\assets\Player.png"
player_surf = pygame.image.load(player_path)
player_rect = player_surf.get_rect(midleft=(0, 225))
player_gravity = 0
player_damping_factor = 0.7
player_score = 0

player2_path = r"..\assets\Computer.png"
player2_surf = pygame.image.load(player2_path)
player2_rect = player2_surf.get_rect(midright=(800, 225))
player2_gravity = 0
player2_score = 0

ball_path = r"..\assets\Ball.png"
ball_surf = pygame.image.load(ball_path)
ball_rect = ball_surf.get_rect(center=(400, 225))
ball_x_velocity, ball_y_velocity = [5, 5]


def flappy_pong(screen) -> str:
    global player_score
    global player2_score
    global ball_x_velocity
    global ball_y_velocity
    global player_gravity
    global player2_gravity
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_gravity = -10
                elif event.key == pygame.K_UP:
                    player2_gravity = -10

        mouse_pos = pygame.mouse.get_pos()
        player_text_surface = font.render(str(player_score), False, "white")
        player_text_rect = player_text_surface.get_rect(
            center=left_scorebar_rect.center
        )
        player2_text_surface = font.render(str(player2_score), False, "white")
        player2_text_rect = player2_text_surface.get_rect(
            center=right_scorebar_rect.center
        )

        screen.blit(board_surf, (0, 0))

        player_gravity += 0.5
        player_rect.y += player_gravity

        player2_gravity += 0.5
        player2_rect.y += player2_gravity

        if player_rect.bottom > 450:
            player_rect.bottom = 450
            player_gravity = -player_gravity * player_damping_factor

        if player_rect.top < 47:
            player_rect.top = 47
            player_gravity = player_gravity * player_damping_factor

        if player2_rect.bottom > 450:
            player2_rect.bottom = 450
            player2_gravity = -player2_gravity * player_damping_factor

        if player2_rect.top < 47:
            player2_rect.top = 47
            player2_gravity = player2_gravity * player_damping_factor

        screen.blit(player_surf, player_rect)
        screen.blit(player2_surf, player2_rect)
        ball_rect.x += ball_x_velocity
        ball_rect.y += ball_y_velocity
        screen.blit(scorebar_surf, left_scorebar_rect)
        screen.blit(right_scorebar_surf, right_scorebar_rect)
        screen.blit(ball_surf, ball_rect)
        screen.blit(player_text_surface, player_text_rect)
        screen.blit(player2_text_surface, player2_text_rect)

        if ball_rect.top <= 47 or ball_rect.bottom >= 450:
            ball_y_velocity = -ball_y_velocity

        if ball_rect.colliderect(player_rect) or ball_rect.colliderect(player2_rect):
            ball_x_velocity = -ball_x_velocity

        if ball_rect.left <= 0:
            player2_score += 1
            ball_x_velocity, ball_y_velocity = choice([-5, 5]), choice([-5, 5])
            ball_rect.center = (400, 225)
            if player2_score == 10:
                return "player 2 won"

        if ball_rect.right >= 800:
            player_score += 1
            ball_x_velocity, ball_y_velocity = choice([-5, 5]), choice([-5, 5])
            ball_rect.center = (400, 225)
            if player_score == 10:
                return "player 1 won"

        pygame.display.update()
        clock.tick(60)



