"""
Задача:
Необходимо написать программу, которая реализует игру арканоид
Это просто пример для того, чтобы вы вспомнили, что это за игра.
Ваша реализация может выглядеть по-другому.
Сущности:
• Класс для мяча
• Класс для платформы
• Класс для блоков
• Класс для самой игры
Требования:
Мяч должен отскакивать от стенок (боковых и верхней), блоков и платформы. Если
мы не успеваем поймать мяч платформой, т.е. он касается нижней стенки, то игра
заканчивается.
Платформу двигаем с помощью клавиш стрелок (вправо и влево).
Блоки имеют разное hp, одни бьются с одного удара, другие с двух, третьи с трех и
так далее (до 5 максимум). Можно сделать эту классификацию по цветам блоков,
например: красный – 1 hp, зеленый – 2 hp и т.д. В игре должны присутствовать
разные блоки. Блоки распределяются рандомно в игре, не должно быть, что один
ряд – красных, второй ряд – зеленый, блоки должны стоять в случайном порядке.
Ряд блоков не должен выглядеть монолитом, между блоками должно быть
небольшое расстояние или какая-то окантовка, чтобы различать блоки.
Складываем баллы в общий зачет, т.е. один удар мячика о блок = +1 балл к общему
числу. Если разрушили все блоки, то +10 баллов и игра завершается.
При завершении игры выводить набранное количество баллов за игру.
Данная часть предполагает в сумме 10 баллов.
Можно реализовать ещё бонусы, за это ещё +10 баллов (класс для бонусов):
Бонусы ловим только платформой. Если бонус коснулся нижней стенки окна, то он
больше не действителен. Бонус пропадает при касании с платформой
(поглощение) и при касании с нижней стенкой окна (исчезает).
Бонусы распределяются по блокам рандомно, они имеют разные типы и есть не во
всех блоках.
Соответственно, бонусы выпадают из каких-то блоков, когда шарик разрушает их
окончательно. Бонус может и не выпасть. Наличие бонуса не зависит от вида
блока. Падают бонусы вниз по прямой, без отклонений. Шарик не можем сбивать
или поглощать бонусы.
Типы бонусов:
• Бонус 1 – увеличение размера шарика
• Бонус 2 – уменьшение размера шарика
• Бонус 3 – увеличение размера платформы
• Бонус 4 – уменьшение размера платформы
• Бонус 5 – увеличение скорости шарика
• Бонус 6 – уменьшение скорости шарика
Время действия бонуса неограниченно. Например, если поймали бонус с
увеличением размера шарика, то он будет таким пока вы не поймаете уменьшение
размера шарика (вернется к прежнему размеру) или еще раз увеличение шарика
(тогда он станет ещё больше).
"""

import pygame
import random
import sys
from pygame.locals import *

# Инициализация pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 15
BALL_RADIUS = 10
BLOCK_WIDTH = 75
BLOCK_HEIGHT = 30
BLOCK_GAP = 5
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Цвета блоков в зависимости от HP
BLOCK_COLORS = {
    1: RED,
    2: GREEN,
    3: BLUE,
    4: YELLOW,
    5: ORANGE
}

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Арканоид')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BALL_RADIUS
        self.dx = 5
        self.dy = -5
        self.color = WHITE
        self.base_speed = 5
        self.size_multiplier = 1
        self.speed_multiplier = 1  # Добавлен недостающий атрибут
        
    def move(self):
        self.x += self.dx * self.speed_multiplier
        self.y += self.dy * self.speed_multiplier
        
        # Отскок от стен
        if self.x <= self.radius * self.size_multiplier or self.x >= SCREEN_WIDTH - self.radius * self.size_multiplier:
            self.dx = -self.dx
        if self.y <= self.radius * self.size_multiplier:
            self.dy = -self.dy
            
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius * self.size_multiplier))
        
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-5, 5])
        self.dy = -5
        self.size_multiplier = 1
        self.speed_multiplier = 1
        
    def get_rect(self):
        return pygame.Rect(self.x - self.radius * self.size_multiplier, 
                          self.y - self.radius * self.size_multiplier, 
                          self.radius * 2 * self.size_multiplier, 
                          self.radius * 2 * self.size_multiplier)

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT
        self.color = WHITE
        self.speed = 10
        self.size_multiplier = 1
        
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < SCREEN_WIDTH - self.width * self.size_multiplier:
            self.x += self.speed
            
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                         (self.x, self.y, 
                          self.width * self.size_multiplier, 
                          self.height))
                          
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 
                           self.width * self.size_multiplier, 
                           self.height)

class Block:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.hp = hp
        self.max_hp = hp
        self.color = BLOCK_COLORS[hp]
        self.has_bonus = random.random() < 0.2  # 20% chance for bonus
        
    def hit(self):
        self.hp -= 1
        if self.hp > 0:
            self.color = BLOCK_COLORS[self.hp]
        return self.hp <= 0
        
    def draw(self, surface):
        # Рисуем блок с окантовкой
        pygame.draw.rect(surface, BLACK, 
                         (self.x - 2, self.y - 2, 
                          self.width + 4, self.height + 4))
        pygame.draw.rect(surface, self.color, 
                         (self.x, self.y, 
                          self.width, self.height))
        
        # Если есть бонус - рисуем маркер
        if self.has_bonus:
            pygame.draw.circle(surface, WHITE, 
                               (self.x + self.width // 2, 
                                self.y + self.height // 2), 
                               5)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Bonus:
    def __init__(self, x, y, bonus_type):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.type = bonus_type
        self.speed = 3
        self.active = True
        self.colors = {
            1: RED,    # Увеличение шара
            2: GREEN,  # Уменьшение шара
            3: BLUE,   # Увеличение платформы
            4: YELLOW, # Уменьшение платформы
            5: ORANGE, # Увеличение скорости
            6: PURPLE  # Уменьшение скорости
        }
        self.color = self.colors[bonus_type]
        
    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.active = False
            
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                         (self.x, self.y, 
                          self.width, self.height))
        # Рисуем номер бонуса
        text = font.render(str(self.type), True, BLACK)
        surface.blit(text, (self.x + 5, self.y + 2))
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def apply(self, game):
        if self.type == 1:
            game.ball.size_multiplier += 0.2
        elif self.type == 2:
            game.ball.size_multiplier = max(0.5, game.ball.size_multiplier - 0.2)
        elif self.type == 3:
            game.platform.size_multiplier += 0.2
        elif self.type == 4:
            game.platform.size_multiplier = max(0.5, game.platform.size_multiplier - 0.2)
        elif self.type == 5:
            game.ball.speed_multiplier += 0.2
        elif self.type == 6:
            game.ball.speed_multiplier = max(0.5, game.ball.speed_multiplier - 0.2)

class Game:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.platform = Platform(SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2, 
                                SCREEN_HEIGHT - 50)
        self.blocks = []
        self.bonuses = []
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.create_blocks()
        
    def create_blocks(self):
        rows = 5
        cols = SCREEN_WIDTH // (BLOCK_WIDTH + BLOCK_GAP)
        start_x = (SCREEN_WIDTH - cols * (BLOCK_WIDTH + BLOCK_GAP) + BLOCK_GAP) // 2
        
        for row in range(rows):
            for col in range(cols):
                hp = random.randint(1, 5)
                x = start_x + col * (BLOCK_WIDTH + BLOCK_GAP)
                y = 50 + row * (BLOCK_HEIGHT + BLOCK_GAP)
                self.blocks.append(Block(x, y, hp))
                
    def handle_collisions(self):
        # Столкновение мяча с платформой
        if self.ball.get_rect().colliderect(self.platform.get_rect()):
            # Определяем, в какую часть платформы попал мяч
            hit_pos = (self.ball.x - self.platform.x) / (self.platform.width * self.platform.size_multiplier)
            
            # Угол отскока зависит от места удара
            self.ball.dx = (hit_pos - 0.5) * 10
            self.ball.dy = -abs(self.ball.dy)
            
        # Столкновение мяча с блоками
        for block in self.blocks[:]:
            if self.ball.get_rect().colliderect(block.get_rect()):
                self.score += 1
                
                # Определяем сторону столкновения
                if (self.ball.x < block.x or self.ball.x > block.x + block.width):
                    self.ball.dx = -self.ball.dx
                else:
                    self.ball.dy = -self.ball.dy
                
                # Уменьшаем HP блока
                if block.hit():
                    # Если блок разрушен, проверяем бонус
                    if block.has_bonus:
                        bonus_type = random.randint(1, 6)
                        self.bonuses.append(Bonus(
                            block.x + block.width // 2 - 10,
                            block.y + block.height // 2,
                            bonus_type
                        ))
                    self.blocks.remove(block)
                    
                # Проверяем, остались ли блоки
                if not self.blocks:
                    self.score += 10
                    self.game_won = True
                    self.game_over = True
                
                break
                
        # Столкновение бонусов с платформой
        for bonus in self.bonuses[:]:
            if bonus.get_rect().colliderect(self.platform.get_rect()):
                bonus.apply(self)
                self.bonuses.remove(bonus)
                
        # Проверка проигрыша (мяч упал вниз)
        if self.ball.y > SCREEN_HEIGHT:
            self.game_over = True
            
    def update(self):
        if not self.game_over:
            self.ball.move()
            
            for bonus in self.bonuses[:]:
                bonus.move()
                if not bonus.active:
                    self.bonuses.remove(bonus)
                    
            self.handle_collisions()
            
    def draw(self, surface):
        surface.fill(BLACK)
        
        # Рисуем счет
        score_text = font.render(f"Счет: {self.score}", True, WHITE)
        surface.blit(score_text, (10, 10))
        
        # Рисуем игровые объекты
        self.ball.draw(surface)
        self.platform.draw(surface)
        
        for block in self.blocks:
            block.draw(surface)
            
        for bonus in self.bonuses:
            bonus.draw(surface)
            
        # Сообщение о конце игры
        if self.game_over:
            if self.game_won:
                message = "Поздравляем! Вы выиграли!"
            else:
                message = "Игра окончена. Попробуйте еще раз!"
                
            text = font.render(message, True, WHITE)
            restart_text = font.render("Нажмите R для рестарта", True, WHITE)
            
            surface.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 
                               SCREEN_HEIGHT // 2 - text.get_height() // 2))
            surface.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 
                                       SCREEN_HEIGHT // 2 + 30))
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_r and self.game_over:
                    self.reset()
                    
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.platform.move("left")
        if keys[K_RIGHT]:
            self.platform.move("right")

# Основной игровой цикл
def main():
    game = Game()
    
    while True:
        game.handle_events()
        game.update()
        game.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
