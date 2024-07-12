import pygame
from random import choice

pygame.init()

screen = pygame.display.set_mode((800, 450))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

font_path = r"..\assets\Teko-VariableFont_wght.ttf"
font = pygame.font.Font(font_path, 50)
player_score = 0
comp_score = 0

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

comp_path = r"..\assets\Computer.png"
comp_surf = pygame.image.load(comp_path)
comp_rect = comp_surf.get_rect(midright=(800, 225))

ball_path = r"..\assets\Ball.png"
ball_surf = pygame.image.load(ball_path)
ball_rect = ball_surf.get_rect(center=(400, 225))
ball_y_velocity, ball_x_velocity = 5, 5


def classic_pong(screen, two_player) -> str:
    player_score = 0
    comp_score = 0
    global ball_x_velocity
    global ball_y_velocity
    global player_rect
    global comp_rect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mouse_pos = pygame.mouse.get_pos()
        player_text_surface = font.render(str(player_score), False, "white")
        player_text_rect = player_text_surface.get_rect(
            center=left_scorebar_rect.center
        )
        comp_text_surface = font.render(str(comp_score), False, "white")
        comp_text_rect = comp_text_surface.get_rect(center=right_scorebar_rect.center)

        screen.blit(board_surf, (0, 0))
        screen.blit(player_surf, player_rect)
        screen.blit(comp_surf, comp_rect)
        ball_rect.x += ball_x_velocity * 2
        ball_rect.y += ball_y_velocity * 2
        screen.blit(ball_surf, ball_rect)
        screen.blit(scorebar_surf, left_scorebar_rect)
        screen.blit(right_scorebar_surf, right_scorebar_rect)
        pygame.draw.line(screen, (32, 24, 38), (0, 47), (800, 47), 2)
        pygame.draw.rect(screen, "black", (left_scorebar_rect.right, 0, 118, 47))
        screen.blit(player_text_surface, player_text_rect)
        screen.blit(comp_text_surface, comp_text_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and comp_rect.top >= 47 and two_player:
            comp_rect.y -= 5

        if keys[pygame.K_DOWN] and comp_rect.bottom <= 450 and two_player:
            comp_rect.y += 5

        if keys[pygame.K_w] and player_rect.top >= 47:
            player_rect.y -= 5

        if keys[pygame.K_s] and player_rect.bottom <= 450:
            player_rect.y += 5

        if ball_rect.bottom >= 450 or ball_rect.top <= 47:
            ball_y_velocity = -ball_y_velocity

        if not two_player:
            if ball_rect.y < comp_rect.y:
                comp_rect.y -= 5

            if ball_rect.y > comp_rect.y and comp_rect.bottom <= 450:
                comp_rect.y += 5

        if ball_rect.colliderect(player_rect) or ball_rect.colliderect(comp_rect):
            ball_x_velocity = -ball_x_velocity

        if ball_rect.left <= 0 or ball_rect.right >= 800:
            if ball_rect.left <= 0:
                comp_score += 1
                ball_rect.center = (400, 225)
                ball_x_velocity, ball_y_velocity = choice([-5, 5]), choice((-5, 5))
                if comp_score == 10 and two_player:
                    return "player 2 won"
                if comp_score == 10 and not two_player:
                    return "computer won"
            else:
                player_score += 1
                ball_rect.center = (400, 225)
                ball_x_velocity, ball_y_velocity = choice([-5, 5]), choice((-5, 5))
                if player_score == 10:
                    return "player 1 won"

        pygame.display.update()
        clock.tick(60)



