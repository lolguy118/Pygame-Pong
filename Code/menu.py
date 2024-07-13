import pygame
from button_class import Button


font_path = r"..\assets\Teko-VariableFont_wght.ttf"


board_path = r"..\assets\Board.png"
board_surf = pygame.image.load(board_path)


def title_screen(screen):
    title_screen_font = pygame.font.Font(font_path, 300)
    title_screen_text_surf = title_screen_font.render("PONG", False, "white")
    title_screen_text_rect = title_screen_text_surf.get_rect(center=(400, 150))
    play_button = Button("center", (400, 375), (500, 275), image_path=r"..\assets\play_button_dark.png")
    play_button.rectangle_get()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(board_surf, (0, 0))
        play_button.draw(screen)
        screen.blit(title_screen_text_surf, title_screen_text_rect)
        if play_button.was_clicked(): break
        pygame.display.update()


def game_mode_screen(screen) -> str:
    screen.fill("black")
    game_mode_screen_font = pygame.font.Font(font_path, 100)
    game_mode_screen_text_surf = game_mode_screen_font.render(
        "Choose Your Game Mode", False, "white"
    )
    game_mode_screen_text_rect = game_mode_screen_text_surf.get_rect(center=(400, 50))
    left_button = Button("topleft", (72, 200), (300, 100), 50, color=(77, 109, 243), text="Classic", text_color="white", text_position_used_to_place="center", text_xy=(222, 250))
    left_button.rectangle_get()
    left_button.text_rectangle_get()
    right_button = Button("topright", (728, 200), (300, 100), 50, color=(77, 109, 243), text="Flappy Pong (2P Only)", text_color="white", text_position_used_to_place="center", text_xy=(578, 250))
    right_button.rectangle_get()
    right_button.text_rectangle_get()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(board_surf, (0, 0))
        left_button.draw(screen)
        right_button.draw(screen)
        screen.blit(game_mode_screen_text_surf, game_mode_screen_text_rect)
        if left_button.was_clicked(): return "classic"
        if right_button.was_clicked(): return "flappy"
        pygame.display.update()


def two_player_or_not(screen) -> bool:
    screen.fill("black")
    left_button = Button("topleft", (72, 200), (300, 100), 50, color=(77, 109, 243), text="1P", text_color="white", text_position_used_to_place="center", text_xy=(222, 250))
    left_button.rectangle_get()
    left_button.text_rectangle_get()
    right_button = Button("topright", (728, 200), (300, 100), 50, color=(77, 109, 243), text="2P", text_color="white", text_position_used_to_place="center", text_xy=(578, 250))
    right_button.rectangle_get()
    right_button.text_rectangle_get()
    player_count_font = pygame.font.Font(font_path, 100)
    player_count_text_surf = player_count_font.render("Solo or Versus", False, "white")
    player_count_text_rect = player_count_text_surf.get_rect(center=(400, 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(board_surf, (0, 0))
        left_button.draw(screen)
        right_button.draw(screen)
        screen.blit(player_count_text_surf, player_count_text_rect)
        if left_button.was_clicked(): return False
        elif right_button.was_clicked(): return True
        pygame.display.update()


def end_screen(screen, result):
    play_again_button = Button("center", (400, 350), (500, 275), image_path=r"..\assets\play_again.png")
    play_again_button.rectangle_get()
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
        screen.blit(board_surf, (0, 0))
        play_again_button.draw(screen)
        screen.blit(text, text_rect)
        if play_again_button.was_clicked(): return None
        pygame.display.update()
    
    

