class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки пули
        self.bullet_width = 8
        self.bullet_height = 23
        self.bullet_color = 214, 158, 15
        self.bullets_allowed = 3

        # настройки пришельцев
        self.fleet_drop_speed = 30

        # Темп ускорения игры
        self.speedup_scale = 1.1

        # Темп роста стоймости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 0.1

        # fleet_direction = 1 обозначает движение вправо; a -1 - влево
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоймость пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
