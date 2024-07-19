import pygame
from random import choice

class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("..\\assets\\Ball.png").convert_alpha()
        self.rect = self.image.get_rect(center=(400, 225))
        self.x_velocity = choice([-5, 5])
        self.y_velocity = choice([-5, 5])
    def move(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        if self.rect.top <= 47 or self.rect.bottom >= 450:
            self.y_velocity = -self.y_velocity
    def update_score(self, player_score : int, computer_score : int):
        if self.rect.left <= 0:
            computer_score += 1
            self.rect.center = (400, 225)
            self.x_velocity, self. y_velocity = choice([-5, 5]), choice([-5, 5])
        if self.rect.right >= 800:
            player_score += 1
            self.rect.center = (400, 225)
            self.x_velocity, self. y_velocity = choice([-5, 5]), choice([-5, 5])
        return player_score, computer_score
    def update(self):
        self.move()
