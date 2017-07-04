import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Инициализация корабля и постановка начальной позиции"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения и создание hurtbox'а в виде прямоугольника.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется внизу экрана по центру.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Десятичное значения для центра корабля.
        self.center = float(self.rect.centerx)

        # Активация\деактивация движения.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
    def blitme(self):
        """Отрисовка корабля в его текущей локации."""
        self.screen.blit(self.image, self.rect)
