class Settings():
    """Класс, в котором хранятся все настройки для игры."""

    def __init__(self):
        """Инициализация настроек"""
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 1.5

        # Настройки снаряда
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
