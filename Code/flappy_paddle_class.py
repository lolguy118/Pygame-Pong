from typing import Any
from _types import EventInfo
import pygame

class Flappy_Paddle(pygame.sprite.Sprite):
    def __init__(self, is_player_1 : bool, is_player_2 : bool) -> None:
        super().__init__()
        self.is_player_1 = is_player_1
        self.is_player_2 = is_player_2
        if self.is_player_1:
            self.image = pygame.image.load("..\\assets\\Player.png")
            self.rect = self.image.get_rect(midleft=(0, 225))
        elif self.is_player_2:
            self.image = pygame.image.load("..\\assets\\Computer.png")
            self.rect = self.image.get_rect(midright=(800, 225))
        self.gravity = 0
        self.damping_factor = 0.7
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 450:
            self.rect.bottom = 450
            self.gravity = -self.gravity * self.damping_factor
        elif self.rect.top <= 47:
            self.rect.top = 47
            self.gravity = self.gravity * self.damping_factor
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.is_player_2:
            self.gravity = -10
        if keys[pygame.K_w] and self.is_player_1:
            self.gravity = -10
    def update(self) -> None:
        self.apply_gravity()
        self.handle_input()