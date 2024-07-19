from ball_class import Ball
from paddle_class import Paddle
from flappy_paddle_class import Flappy_Paddle
from abc import ABC, abstractmethod
from typing import Any
from os import getcwd
import pygame
from button import Button
from _types import EventInfo


class GameState(ABC):
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.is_over = False
        self.board_surf = pygame.image.load("..\\assets\\Board.png")

    @abstractmethod
    def update(self, event_info: EventInfo) -> None:
        pass

    @abstractmethod
    def next_game_state(self) -> Any:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


class Title_Screen(GameState):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.title_screen_font = pygame.font.Font(
            "..\\assets\\Teko-VariableFont_wght.ttf", 300
        )
        self.title_screen_text_surf = self.title_screen_font.render(
            "PONG", False, "white"
        )
        self.title_screen_text_rect = self.title_screen_text_surf.get_rect(
            center=(400, 150)
        )
        self.play_button = Button(
            "center",
            (400, 375),
            (500, 275),
            image_path=r"..\assets\play_button_dark.png",
        )

    def update(self, event_info: EventInfo) -> None:
        self.play_button.was_clicked(event_info)
        if self.play_button.clicked:
            self.is_over = True

    def next_game_state(self) -> Any:
        return Game_Mode_Screen(self.screen)

    def draw(self) -> None:
        self.screen.blit(self.board_surf, (0, 0))
        self.play_button.draw(self.screen)
        self.screen.blit(self.title_screen_text_surf, self.title_screen_text_rect)


class Game_Mode_Screen(GameState):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.game_mode_screen_font = pygame.font.Font(
            "..\\assets\\Teko-VariableFont_wght.ttf", 100
        )
        self.game_mode_screen_text_surf = self.game_mode_screen_font.render(
            "Choose Your Game Mode", False, "white"
        )
        self.game_mode_screen_text_rect = self.game_mode_screen_text_surf.get_rect(
            center=(400, 50)
        )
        self.left_button = Button(
            "topleft",
            (72, 200),
            (300, 100),
            50,
            color=(77, 109, 243),
            text="Classic",
            text_color="white",
            text_position_used_to_place="center",
            text_xy=(222, 250),
        )
        self.right_button = Button(
            "topright",
            (728, 200),
            (300, 100),
            50,
            color=(77, 109, 243),
            text="Flappy Pong (2P Only)",
            text_color="white",
            text_position_used_to_place="center",
            text_xy=(578, 250),
        )

    def update(self, event_info: EventInfo) -> None:
        self.left_button.was_clicked(event_info)
        if self.left_button.clicked:
            self.game_mode = "classic"
            self.is_over = True
        self.right_button.was_clicked(event_info)
        if self.right_button.clicked:
            self.game_mode = "flappy"
            self.is_over = True

    def next_game_state(self) -> Any:
        if self.game_mode == "classic":
            return Two_Player_Screen(self.screen)
        elif self.game_mode == "flappy":
            return Flappy_Pong_Game(self.screen)

    def draw(self) -> None:
        self.left_button.draw(self.screen)
        self.right_button.draw(self.screen)
        self.screen.blit(
            self.game_mode_screen_text_surf, self.game_mode_screen_text_rect
        )


class Two_Player_Screen(GameState):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.left_button = Button(
            "topleft",
            (72, 200),
            (300, 100),
            50,
            color=(77, 109, 243),
            text="1P",
            text_color="white",
            text_position_used_to_place="center",
            text_xy=(222, 250),
        )
        self.right_button = Button(
            "topright",
            (728, 200),
            (300, 100),
            50,
            color=(77, 109, 243),
            text="2P",
            text_color="white",
            text_position_used_to_place="center",
            text_xy=(578, 250),
        )
        self.player_count_font = pygame.font.Font(
            "..\\assets\\Teko-VariableFont_wght.ttf", 100
        )
        self.player_count_text_surf = self.player_count_font.render(
            "Solo or Versus", False, "white"
        )
        self.player_count_text_rect = self.player_count_text_surf.get_rect(
            center=(400, 50)
        )

    def update(self, event_info: EventInfo):
        if self.left_button.was_clicked(event_info):
            self.is_two_player = False
            self.is_over = True
        if self.right_button.was_clicked(event_info):
            self.is_two_player = True
            self.is_over = True

    def next_game_state(self) -> Any:
        return Classic_Pong_Game(self.screen, self.is_two_player)

    def draw(self) -> None:
        self.screen.blit(self.board_surf, (0, 0))
        self.left_button.draw(self.screen)
        self.right_button.draw(self.screen)
        self.screen.blit(self.player_count_text_surf, self.player_count_text_rect)


class Classic_Pong_Game(GameState):
    def __init__(self, screen: pygame.Surface, is_two_player: bool) -> None:
        super().__init__(screen)
        self.ball = Ball()
        self.ball_group = pygame.sprite.GroupSingle(self.ball)
        self.player_1 = Paddle(True, False)
        if is_two_player:
            self.computer_or_player_2 = Paddle(False, True)
        else:
            self.computer_or_player_2 = Paddle(False, False)
        self.paddles = pygame.sprite.Group(self.player_1, self.computer_or_player_2)
        self.player_1_score = 0
        self.computer_or_player_2_score = 0
        self.score_font = pygame.font.Font("..\\assets\\Teko-VariableFont_wght.ttf", 50)
        self.player_1_score_board_surf = pygame.image.load("..\\assets\\ScoreBar.png")
        self.player_1_score_board_rect = self.player_1_score_board.get_rect(
            topleft=(0, 0)
        )
        self.computer_or_player_2_score_board_surf = pygame.transform.flip(
            self.player_1_score_board_surf, True, False
        )
        self.computer_or_player_2_score_board_rect = (
            self.computer_or_player_2_score_board_surf.get_rect(topright=(800, 0))
        )

    def update(self, event_info: EventInfo) -> None:
        if self.player_1_score >= 10 or self.computer_or_player_2_score >= 10:
            self.is_over = True
        else:
            self.paddles.update()
            if not self.computer_or_player_2.is_player2:
                self.computer_or_player_2.computer_move(self.ball.rect.y)
            if pygame.sprite.spritecollideany(self.ball, self.paddles) != None:
                self.ball.x_velocity = -self.ball.x_velocity
            self.player_1_score, self.computer_or_player_2_score = (
                self.ball.update_score(
                    self.player_1_score, self.computer_or_player_2_score
                )
            )
            self.ball_group.update()
    def draw(self) -> None:
        self.player_1_score_text = self.score_font.render(str(self.player_1_score), False, "white")
        self.player_1_score_text_rect = self.player_1_score_text.get_rect(center=self.player_1_score_board_rect.center)
        self.computer_or_player_2_text = self.score_font.render(str(self.computer_or_player_2_score), False, "white")
        self.computer_or_player_2_text_rect = self.computer_or_player_2_text.get_rect(center=self.computer_or_player_2_score_board_rect.center)
        self.screen.blit(self.board_surf, (0, 0))
        self.screen.blit(self.player_1_score_board_surf, self.player_1_score_board_rect)
        self.screen.blit(self.computer_or_player_2_score_board_surf, self.computer_or_player_2_score_board_rect)
        self.ball_group.draw(self.screen)
        self.paddles.draw(self.screen)
        self.screen.blit(self.player_1_score_text, self.player_1_score_text_rect)
        self.screen.blit(self.computer_or_player_2_text, self.computer_or_player_2_text_rect)

    def next_game_state(self) -> Any:
        if self.player_1_score >= 10:
            return Result_Screen(self.screen, "P1")
        elif (
            self.computer_or_player_2_score >= 10
            and self.computer_or_player_2.is_player2
        ):
            return Result_Screen(self.screen, "P2")
        else:
            return Result_Screen(self.screen, "Computer")


class Flappy_Pong_Game(GameState):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.ball = Ball()
        self.ball_group = pygame.sprite.GroupSingle(self.ball)
        self.player_1 = Flappy_Paddle(True, False)
        self.player_2 = Flappy_Paddle(False, True)
        self.paddles = pygame.sprite.Group(self.player_1, self.player_2)
        self.score_font = pygame.font.Font("..\\assets\\Teko-VariableFont_wght.ttf", 50)
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_1_score_bar_surf = pygame.image.load("..\\assets\\ScoreBar.png")
        self.player_1_score_bar_rect = self.player_1_score_bar_surf.get_rect(topleft=(0, 0))
        self.player_2_score_bar_surf = pygame.transform.flip(self.player_1_score_bar_surf, True, False)
        self.player_2_score_bar_rect = self.player_2_score_bar_surf.get_rect(topright=(800, 0))
    def update(self, event_info: EventInfo) -> None:
        if self.player_1_score >= 10 or self.player_2_score >= 10:
            self.is_over = True
        else:
            self.paddles.update()
            if pygame.sprite.spritecollideany(self.ball, self.paddles) != None:
                self.ball.x_velocity = -self.ball.x_velocity
            self.player_1_score, self.player_2_score = self.ball.update_score(self.player_1_score, self.player_2_score)
            self.ball_group.update()
    def draw(self) -> None:
        self.player_1_score_text = self.score_font.render(str(self.player_1_score), False, "white")
        self.player_1_score_text_rect = self.player_1_score_text.get_rect(center=self.player_1_score_bar_rect.center)
        self.player_2_score_text = self.score_font.render(str(self.player_2_score), False, "white")
        self.player_2_score_text_rect = self.player_2_score_text.get_rect(center=self.player_2_score_bar_rect.center)

        self.screen.blit(self.board_surf, (0, 0))
        self.screen.blit(self.player_1_score_bar_surf, self.player_1_score_bar_rect)
        self.screen.blit(self.player_2_score_bar_surf, self.player_2_score_bar_rect)
        self.paddles.draw(self.screen)
        self.ball_group.draw(self.screen)
        self.screen.blit(self.player_1_score_text, self.player_1_score_text_rect)
        self.screen.blit(self.player_2_score_text, self.player_2_score_text_rect)
    def next_game_state(self) -> Any:
        if self.player_1_score >= 10:
            return Result_Screen(self.screen, "P1")
        elif self.player_2_score >= 10:
            return Result_Screen(self.screen, "P2")





class Result_Screen(GameState):
    def __init__(self, screen: pygame.Surface, winner : str) -> None:
        super().__init__(screen)
        self.result_font = pygame.font.Font("..\\assets\\Teko-VariableFont_wght.ttf", 275)
        self.result_text = self.result_font.render(f"{winner} Wins", False, "white")
        self.result_text_rect = self.result_text.get_rect(center=(400, 150))
        self.play_again_button = Button("center", (400, 350), (500, 275), image_path="..\\assets\\play_again.png")
    def update(self, event_info: EventInfo) -> None:
        if self.play_again_button.was_clicked(event_info):
            self.is_over = True
    def next_game_state(self) -> Any:
        return Game_Mode_Screen(self.screen)
    def draw(self) -> None:
        self.screen.blit(self.board_surf, (0, 0))
        self.play_again_button.draw(self.screen)
        self.screen.blit(self.result_text, self.result_text_rect)