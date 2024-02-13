import pygame
import random
import os
import sys


class Egg:
    def __init__(self, egg_speed=0, speed_up=0) -> None:
        self.egg_width = 30
        self.egg_height = 30
        self.egg_x = random.randint(0, 400 - self.egg_width)
        self.egg_y = -60
        self.egg_speed = egg_speed
        self.speed_up = speed_up

    def move(self):
        self.egg_y += self.egg_speed

    def speed(self):
        self.egg_speed += self.speed_up


class Poo:
    def __init__(self, poo_speed) -> None:
        self.poo_width = 30
        self.poo_height = 30
        self.poo_x = random.randint(0, 400 - self.poo_width)
        self.poo_y = -60
        self.poo_speed = poo_speed

    def move(self):
        self.poo_y += self.poo_speed


def main(egg_speed: float,
         player_speed: float,
         poo_speed: float,
         purpose: int,
         lifes: int,
         level: int,
         speed_up: float) -> tuple[bool, int]:
    pygame.init()
    score = 0
    timer = 0
    win = False
    screen_width = 400
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("НУ, ПОГОДИ!")
    bg_image = pygame.image.load('фон.jpg')
    texture_egg = pygame.image.load('egg.png')
    texture_egg = pygame.transform.scale(texture_egg, (50, 43))
    texture_poo = pygame.image.load('i.png')
    texture_poo = pygame.transform.scale(texture_poo, (50, 43))
    texture_player = pygame.image.load('wolf.png')
    texture_player = pygame.transform.scale(texture_player, (55, 70))
    texture_player_r = pygame.image.load('wolf_reverse.png')
    texture_player_r = pygame.transform.scale(texture_player_r, (55, 70))
    player = texture_player
    clock = pygame.time.Clock()
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (221, 255, 127)
    brown = (204, 52, 6)
    player_width = 55
    player_height = 70
    player_x = screen_width / 2 - player_width / 2
    player_y = screen_height - player_height
    player_speed = player_speed
    f_e = Egg(egg_speed=egg_speed, speed_up=speed_up)
    eggs = list()
    poes = list()
    eggs.append(f_e)
    font = pygame.font.SysFont("Comic Sans MS", 18)

    # Игровой цикл
    running = True
    while running:
        timer += 1
        number = random.randint(1, level)
        if number in [1, 2, 3]:
            egg = Egg(egg_speed=egg_speed, speed_up=speed_up)
            eggs.append(egg)
        elif number in [1, 2, 3]:
            poo = Poo(poo_speed=poo_speed)
            poes.append(poo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if purpose == score or lifes == 0:
            running = False
            win = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
            player = texture_player_r
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
            player = texture_player
        for ind, egg in enumerate(eggs):
            egg.move()
            if egg.egg_y + 30 > player_y and egg.egg_x + 30 > player_x and egg.egg_x < player_x + player_width:
                egg.egg_x = random.randint(0, screen_width - 30)
                egg.egg_y = -60
                score += 1
                egg.speed()
            if egg.egg_y > screen_height:
                if len(eggs) > 1:
                    eggs.pop(ind)
                else:
                    egg.egg_x = random.randint(0, screen_width - 30)
                    egg.egg_y = -60
                lifes -= 1
        for ind, poo in enumerate(poes):
            poo.move()
            if poo.poo_y + 30 > player_y and poo.poo_x + 30 > player_x and poo.poo_x < player_x + player_width:
                poes.pop(ind)
                lifes -= 1
            if poo.poo_y > screen_height:
                poes.pop(ind)
        screen.blit(bg_image, (0, 0))
        screen.blit(player,
                    (player_x, player_y, player_width, player_height))
        # pygame.draw.rect(screen, black, (player_x, player_y,
        #                                 player_width, player_height))
        for egg in eggs:
            screen.blit(texture_egg, (egg.egg_x, egg.egg_y, 30, 30))
            # pygame.draw.ellipse(screen, red, (egg.egg_x, egg.egg_y, 30, 30))
        for poo in poes:
            screen.blit(texture_poo, (poo.poo_x, poo.poo_y, 30, 30))
            # pygame.draw.ellipse(screen, brown, (poo.poo_x, poo.poo_y, 30, 30))
        score_text = font.render(f"Поймано: {score}", True, black)
        purpose_text = font.render(f"Цель: {purpose}", True, black)
        lifes_text = font.render(f"Жизни: {lifes}", True, black)
        timer_text = font.render(f"Прошло: {timer // 60}", True, black)
        screen.blit(score_text, (10, 30))
        screen.blit(purpose_text, (10, 10))
        screen.blit(lifes_text, (280, 30))
        screen.blit(timer_text, (280, 10))
        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    return (win, score)
