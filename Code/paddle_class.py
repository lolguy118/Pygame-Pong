import pygame
from _types import EventInfo
class Paddle(pygame.sprite.Sprite):
    def __init__(self, is_player1 : bool, is_player2 : bool) -> None:
        super().__init__()
        if is_player1: 
            self.image = pygame.image.load("..\\assets\\Player.png").convert_alpha()
            self.rect = self.image.get_rect(midleft=(0, 225))
        else:
            self.image = pygame.image.load("..\\assets\\Computer.png").convert_alpha()
            self.rect = self.image.get_rect(midright=(800, 225))
        self.is_player1 = is_player1
        self.is_player2 = is_player2
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.is_player1:
            self.rect.y -= 5
        elif keys[pygame.K_s] and self.is_player1:
            self.rect.y += 5
        elif keys[pygame.K_UP] and self.is_player2:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN] and self.is_player2:
            self.rect.y += 5
    def computer_move(self, ball_y_pos):
        if ball_y_pos > self.rect.y:
            self.rect.y += 5
        elif ball_y_pos < self.rect.y:
            self.rect.y -= 5
    def update(self):
        if self.is_player1 or self.is_player2: self.handle_input()
