import pygame

pygame.init()

screen = pygame.display.set_mode((800, 450))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

font_path = r"..\assets\Teko-VariableFont_wght.ttf"

play_button_path = (
    r"..\assets\play_button_dark.png"
)
play_button_surf = pygame.image.load(play_button_path)
play_button_surf = pygame.transform.scale(play_button_surf, (500, 275))
play_button_rect = play_button_surf.get_rect(center=(400, 375))

board_path = r"..\assets\Board.png"
board_surf = pygame.image.load(board_path)


def title_screen(screen):
    title_screen_font = pygame.font.Font(font_path, 300)
    title_screen_text_surf = title_screen_font.render("PONG", False, "white")
    title_screen_text_rect = title_screen_text_surf.get_rect(center=(400, 150))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return None
        screen.blit(board_surf, (0, 0))
        screen.blit(play_button_surf, play_button_rect)
        screen.blit(title_screen_text_surf, title_screen_text_rect)
        pygame.display.update()


def game_mode_screen(screen) -> str:
    screen.fill("black")
    game_mode_screen_font = pygame.font.Font(font_path, 100)
    game_mode_screen_text_surf = game_mode_screen_font.render(
        "Choose Your Game Mode", False, "white"
    )
    game_mode_screen_text_rect = game_mode_screen_text_surf.get_rect(center=(400, 50))
    option_text_font = pygame.font.Font(font_path, 50)
    option_text_surf_1 = option_text_font.render("Classic", False, "white")
    option_text_rect_1 = option_text_surf_1.get_rect(center=(222, 250))
    option_text_surf_2 = option_text_font.render("Flappy (2P Only)", False, "white")
    option_text_rect_2 = option_text_surf_2.get_rect(center=(578, 250))
    left_button = pygame.Surface((300, 100))
    left_button.fill((77, 109, 243))
    left_button_rect = left_button.get_rect(topleft=(72, 200))
    right_button = pygame.Surface((300, 100))
    right_button.fill((77, 109, 243))
    right_button_rect = right_button.get_rect(topright=(728, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return "classic"
                if right_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return "flappy"

        screen.blit(board_surf, (0, 0))
        screen.blit(left_button, left_button_rect)
        screen.blit(right_button, right_button_rect)
        screen.blit(game_mode_screen_text_surf, game_mode_screen_text_rect)
        screen.blit(option_text_surf_1, option_text_rect_1)
        screen.blit(option_text_surf_2, option_text_rect_2)
        pygame.display.update()


def two_player_or_not(screen) -> bool:
    screen.fill("black")
    left_button = pygame.Surface((300, 100))
    left_button.fill((77, 109, 243))
    left_button_rect = left_button.get_rect(topleft=(72, 200))
    right_button = pygame.Surface((300, 100))
    right_button.fill((77, 109, 243))
    right_button_rect = right_button.get_rect(topright=(728, 200))
    option_text_font = pygame.font.Font(font_path, 50)
    option_text_surf_1 = option_text_font.render("1P", False, "white")
    option_text_rect_1 = option_text_surf_1.get_rect(center=(222, 250))
    option_text_surf_2 = option_text_font.render("2P", False, "white")
    option_text_rect_2 = option_text_surf_2.get_rect(center=(578, 250))
    player_count_font = pygame.font.Font(font_path, 100)
    player_count_text_surf = player_count_font.render("Solo or Versus", False, "white")
    player_count_text_rect = player_count_text_surf.get_rect(center=(400, 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option_text_rect_1.collidepoint(pygame.mouse.get_pos()):
                    return False
                if option_text_rect_2.collidepoint(pygame.mouse.get_pos()):
                    return True
        screen.blit(board_surf, (0, 0))
        screen.blit(left_button, left_button_rect)
        screen.blit(right_button, right_button_rect)
        screen.blit(option_text_surf_1, option_text_rect_1)
        screen.blit(option_text_surf_2, option_text_rect_2)
        screen.blit(player_count_text_surf, player_count_text_rect)
        pygame.display.update()


def end_screen(screen, result):
    play_again_button_path = r"C:\Everything\Tech Stuff\learn_pygame\Pong_Files\assets\play_again.png"
    play_again_button_surf = pygame.image.load(play_again_button_path)
    play_again_button_surf = pygame.transform.scale(play_again_button_surf, (500, 275))
    play_again_button_rect = play_again_button_surf.get_rect(center=(400, 350))
    match result:
        case "player 1 won":
            text_to_be_displayed = "P1 Wins"
        case "player 2 won":
            text_to_be_displayed = "P2 Wins"
        case "computer won":
            text_to_be_displayed = "Comp Wins"
        case _:
            text_to_be_displayed = "IDK"
    font = pygame.font.Font(font_path, 275)
    text = font.render(text_to_be_displayed, False, "white")
    text_rect = text.get_rect(center=(400, 150))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return None
        screen.blit(board_surf, (0, 0))
        screen.blit(play_again_button_surf, play_again_button_rect)
        screen.blit(text, text_rect)
        pygame.display.update()
    
    
