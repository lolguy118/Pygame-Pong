import pygame
from _types import EventInfo
class Button:
    def __init__(self, position_used_to_place : str, xy : tuple, width_and_height : tuple, font_size=None, image_path=None, color=None, text=None, text_color=None, text_position_used_to_place=None, text_xy=None) -> None:
        self.position_used_to_place = position_used_to_place
        self.xy = xy
        self.dimensions = width_and_height
        if image_path != None: 
            self.surf = pygame.image.load(image_path)
            self.surf = pygame.transform.scale(self.surf, self.dimensions)
            self.rect = self.surf.get_rect()
        else:
            self.surf = pygame.Surface(self.dimensions)
            self.surf.fill(color)
            self.rect = self.surf.get_rect()
        if text != None:
            button_font = pygame.font.Font(r"..\assets\Teko-VariableFont_wght.ttf", font_size)
            self.text_surf = button_font.render(str(text), False, text_color)
            self.text_rect = self.text_surf.get_rect()
            self.text_position_used_to_place = text_position_used_to_place
            self.text_xy = text_xy
    def rectangle_get(self):
        match self.position_used_to_place:
            case "center":
                self.rect.center = self.xy
            case "topleft":
                self.rect.topleft = self.xy
            case "topright":
                self.rect.topright = self.xy
            case "midright":
                self.rect.midright = self.xy
            case "bottomright":
                self.rect.bottomright = self.xy
            case "midbottom":
                self.rect.midbottom = self.xy
            case "bottomleft":
                self.rect.bottomleft = self.xy
            case "midleft":
                self.rect.midleft = self.xy
    def text_rectangle_get(self):
        match self.text_position_used_to_place:
            case "center":
                self.text_rect.center = self.text_xy
            case "topleft":
                self.text_rect.topleft = self.text_xy
            case "topright":
                self.text_rect.topright = self.text_xy
            case "midright":
                self.text_rect.midright = self.text_xy
            case "bottomright":
                self.text_rect.bottomright = self.text_xy
            case "midbottom":
                self.text_rect.midbottom = self.text_xy
            case "bottomleft":
                self.text_rect.bottomleft = self.text_xy
            case "midleft":
                self.text_rect.midleft = self.text_xy
    def draw(self, screen : pygame.Surface):
        self.rectangle_get()
        screen.blit(self.surf, self.rect)
        if hasattr(self, 'text_surf'):
            self.text_rectangle_get()
            screen.blit(self.text_surf, self.text_rect)
    def was_clicked(self, event_info : EventInfo):
        self.clicked = False
        self.is_hovering_over_button = self.rect.collidepoint(event_info["mouse_pos"])
        self.events = event_info["events"]
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovering_over_button:
                self.clicked = True
