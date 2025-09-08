from __future__ import division
import os
import pygame
import random
import time
import csv
import button
from pypresence import Presence

discord_richpicture = False
music_on_off = False

if discord_richpicture == True:
    start = int(time.time())
    client_id = "1067913122469400626"
    RPC = Presence(client_id)
    RPC.connect()

Icon = pygame.image.load("assets/img/Icons/Game Icon 60x.png")

pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode([1280, 720], pygame.SCALED)
pygame.display.set_caption("Hubba Bubba")
pygame.display.set_icon(Icon)

if music_on_off == True:
    pygame.mixer.music.load("assets/sound/Title Theme.wav")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1, 0.0, 3000)
jump_fx = pygame.mixer.Sound("assets/sound/sounds/Jump 1.wav")
jump_fx.set_volume(0.3)
shot_fx = pygame.mixer.Sound("assets/sound/sounds/Text 1.wav")
shot_fx.set_volume(0.3)
winning_fx = pygame.mixer.Sound("assets/sound/sounds/Success 1.wav")
winning_fx.set_volume(0.3)

# Adding Game Font
font = pygame.font.Font("assets/Fonts/Quinquefive-K7qep.ttf", 15)
font2 = pygame.font.Font("assets/Fonts/Quinquefive-K7qep.ttf", 30)
font3 = pygame.font.Font("assets/Fonts/Quinquefive-K7qep.ttf", 25)
font4 = pygame.font.Font("assets/Fonts/Quinquefive-K7qep.ttf", 40)

# set Framerate
clock = pygame.time.Clock()
FPS = 60

# game variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ROWS = 16
COLS = 150
GRAVITY = 0.60
gravity_text = 6
SCROLL_THRESH = 250
MAX_LEVELS = 10
screen_scroll = 0
bg_scroll = 0
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 25
level = 1
world_number = 1
lifes = 3
coins = 0
start_game = False
pause_game = False
settings_menu = False

# Adding Pictures
Background_Picture = pygame.image.load("assets/img/Background/Background.png")
Background_Picture = pygame.transform.scale(Background_Picture, (1280, 720))
Cloud = pygame.image.load("assets/img/Background/Clouds.png")
Clouds2 = pygame.image.load("assets/img/Background/Clouds2.png")
Clouds3 = pygame.image.load("assets/img/Background/Clouds3.png")
Cloud1 = pygame.transform.scale(Cloud, (int(Cloud.get_width() * 5), int(Cloud.get_height() * 5)))
Cloud2 = pygame.transform.scale(Clouds2, (int(Clouds2.get_width() * 5), int(Clouds2.get_height() * 5)))
Cloud3 = pygame.transform.scale(Clouds3, (int(Clouds3.get_width() * 4), int(Clouds3.get_height() * 4)))
Sun = pygame.image.load("assets/img/Background/Sun.png")
Sun = pygame.transform.scale(Sun, (int(Sun.get_width() * 5), int(Sun.get_height() * 5)))

pause_BG = pygame.image.load("assets/img/Menu/Pause BG.png")
Pause_Square = pygame.image.load("assets/img/Menu/White Square.png")
Settings_Square = pygame.image.load("assets/img/Menu/Settings_Square.png")
Square_level = pygame.image.load("assets/img/Menu/White level sqare.png")
Ammo_etc_bg = pygame.image.load("assets/img/Menu/Ammo_etc_bg.png")

# button images
start_img = pygame.image.load("assets/img/Buttons/start_btn.png").convert_alpha()
exit_img = pygame.image.load("assets/img/Buttons/exit_btn.png").convert_alpha()
restart_img = pygame.image.load("assets/img/Buttons/restart_btn.png").convert_alpha()
play_img = pygame.image.load("assets/img/Buttons/Resume.png").convert_alpha()
pause_img = pygame.image.load("assets/img/Buttons/pause_btn.png").convert_alpha()
exit_small_img = pygame.image.load("assets/img/Buttons/exit_small_btn.png").convert_alpha()
restart_small_img = pygame.image.load("assets/img/Buttons/Restart.png").convert_alpha()
yes_img = pygame.image.load("assets/img/Buttons/yes_btn.png").convert_alpha()
no_img = pygame.image.load("assets/img/Buttons/exit_small_btn.png").convert_alpha()
settings_small_img = pygame.image.load("assets/img/Buttons/settings_small_btn.png").convert_alpha()
plus_small_img = pygame.image.load("assets/img/Buttons/plus_Small_btn.png").convert_alpha()
minus_small_img = pygame.image.load("assets/img/Buttons/minus_small_btn.png").convert_alpha()
back_btn = pygame.image.load("assets/img/Buttons/back_btn.png").convert_alpha()
settings_biggo_img = pygame.image.load("assets/img/Buttons/Options btn biggo.png").convert_alpha()

# store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"assets/img/tile/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

bullet_img = pygame.image.load("assets/img/Bullets/Bullet.png").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (int(bullet_img.get_width() * 4), int(bullet_img.get_height() * 4)))
grenade_img = pygame.image.load("assets/img/Projectiles/Grenades/Grenade1.png").convert_alpha()
grenade_img = pygame.transform.scale(grenade_img, (int(grenade_img.get_width() * 4), int(grenade_img.get_height() * 4)))
heart_img = pygame.image.load("assets/img/Other Icons/Heart.png").convert_alpha()
heart_img = pygame.transform.scale(heart_img, (int(heart_img.get_width() * 3), int(heart_img.get_height() * 3)))
health_gui_img = pygame.image.load("assets/img/Other Icons/Health.png").convert_alpha()
health_gui_img = pygame.transform.scale(health_gui_img,
                                        (int(health_gui_img.get_width() * 4), int(health_gui_img.get_height() * 4)))
bullet_gui_img = pygame.image.load("assets/img/Bullets/Bullet.png").convert_alpha()
bullet_gui_img = pygame.transform.scale(bullet_gui_img,
                                        (int(bullet_gui_img.get_width() * 5), int(bullet_gui_img.get_height() * 5)))
coins_img = pygame.image.load("assets/img/Other Icons/coin.png").convert_alpha()
coins_img = pygame.transform.scale(coins_img,
                                   (int(coins_img.get_width() * 2), int(coins_img.get_height() * 2)))

# Boxen
Random_Block = pygame.image.load("assets/img/Blocks/Random Block.png").convert_alpha()
Random_Block = pygame.transform.scale(Random_Block,
                                      (int(Random_Block.get_width() * 3), int(Random_Block.get_height() * 3)))
Ammo_Block = pygame.image.load("assets/img/Blocks/Ammo Block.png").convert_alpha()
Ammo_Block = pygame.transform.scale(Ammo_Block, (int(Ammo_Block.get_width() * 3), int(Ammo_Block.get_height() * 3)))
Grenades_Block = pygame.image.load("assets/img/Blocks/Grenades Block.png").convert_alpha()
Grenades_Block = pygame.transform.scale(Grenades_Block,
                                        (int(Grenades_Block.get_width() * 3), int(Grenades_Block.get_height() * 3)))
Heil_Block = pygame.image.load("assets/img/Blocks/Heil Block.png").convert_alpha()
Heil_Block = pygame.transform.scale(Heil_Block, (int(Heil_Block.get_width() * 3), int(Heil_Block.get_height() * 3)))
Ausrufezeichen_Block = pygame.image.load("assets/img/Blocks/Ausrufezeichen Block.png").convert_alpha()
Ausrufezeichen_Block = pygame.transform.scale(Ausrufezeichen_Block, (
    int(Ausrufezeichen_Block.get_width() * 3), int(Ausrufezeichen_Block.get_height() * 3)))
item_boxes = {
    "Ammo": Ammo_Block,
    "Grenade": Grenades_Block,
    "Health": Heil_Block,
}

# define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

# define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    screen.fill(WHITE)
    for x in range(5):
        screen.blit(Background_Picture, (0, 0))
        screen.blit(Sun, (0, 0))
        screen.blit(Cloud1, (150, 80))
        screen.blit(Cloud2, (500, 120))
        screen.blit(Cloud3, (1000, 100))


# Function to reset level
def reset_level():
    enemy_group.empty()
    bullet_group.empty()
    grenade_group.empty()
    explosion_group.empty()
    item_box_group.empty()
    decoration_group.empty()
    water_group.empty()
    exit_group.empty()

    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COLS
        data.append(r)

    return data


# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.grenades = grenades
        self.health = 100
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0

        # load all images for the players
        animation_types = ['idle', 'run', 'jump', 'death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f"assets/img/{self.char_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"assets/img/{self.char_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the AI has hit a wall then make it turn around
                if self.char_type == "Enemy Character":
                    self.direction *= 1
                    self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 1
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with water
        if pygame.sprite.spritecollide(self, water_group, False):
            self.health = 0

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if fallen of the map
        if self.rect.bottom > SCREEN_HEIGHT + 20:
            self.health = 0

        # check if going of the screen
        if self.char_type == 'Game Character':
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # update scroll based on player position
        if self.char_type == 'Game Character':
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < (
                    world.level_length * TILE_SIZE) - SCREEN_WIDTH) \
                    or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
                self.rect.x -= dx
                screen_scroll = -dx

        return screen_scroll, level_complete

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0 and pause_game == False:
            self.shoot_cooldown = 15
            bullet = Bullet(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1

    def ai(self):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.idling = True
                self.idling_counter = 50
            # check if the AI in near the player
            if self.vision.colliderect(player.rect):
                # stop running and face the player
                self.update_action(0)  # 0: idle
                # shoot
                self.shoot()
            else:
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update AI vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scrolling
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 75
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class World:
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data):
        self.level_length = len(data[0])

        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x * TILE_SIZE, y * TILE_SIZE)
                        water_group.add(water)
                    elif tile >= 11 and tile <= 14:
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_group.add(decoration)
                    elif tile == 15:  # create player
                        player = Player("Game Character", x * TILE_SIZE, y * TILE_SIZE, 2.95, 5, 30, 3)
                        health_bar = HealthBar(975, 5, player.health, player.health)
                    elif tile == 16:  # create enemy
                        enemy = Player("Enemy Character", x * TILE_SIZE, y * TILE_SIZE, 2.95, 2, 15, 0)
                        enemy_group.add(enemy)
                    elif tile == 17:  # create ammo box
                        item_box = ItemBox("Ammo", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 18:  # create grenade box
                        item_box = ItemBox("Grenade", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 19:  # create health box
                        item_box = ItemBox("Health", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 20:  # create exit
                        exit = Exit(img, x * TILE_SIZE, y * TILE_SIZE)
                        exit_group.add(exit)
                    elif tile >= 21 and tile <= 24:
                        self.obstacle_list.append(tile_data)

        return player, health_bar

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])


class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll
        # check if the player has picked up the box
        if pygame.sprite.collide_rect(self, player):
            # check what kind of box it was
            if self.item_type == 'Health':
                player.health += 25
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.item_type == 'Ammo':
                player.ammo += 15
            elif self.item_type == 'Grenade':
                player.grenades += 3
            # delete the item box
            self.kill()


class HealthBar:
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        # update with new health
        self.health = health
        # calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 304, 24))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 300, 20))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 300 * ratio, 20))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        # check for collision with level
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    self.kill()


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # check for collision with level
        for tile in world.obstacle_list:
            # check if grenade has gone off-screen
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * self.speed

        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                # check if below the ground, i.e. thrown up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. thrown down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom

        # update grenade position
        self.rect.x += dx + screen_scroll
        self.rect.y += dy

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 0.5)
            explosion_group.add(explosion)
            # do damage to anyone that is nearby
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and \
                        abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
                    enemy.health -= 50
                    print(enemy.health)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 3):
            img = pygame.image.load(f"assets/img/Explosions/{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * 5), int(img.get_height() * 5)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.x += screen_scroll
        EXPLOSION_SPEED = 4
        # update explosion animation
        self.counter += 1

        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]


# create Buttons
start_Button = button.Button(50, 604, start_img, 2)
exit_Button = button.Button(1082, 604, exit_img, 2)
restart_Button = button.Button(SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 25, restart_img, 2)

pause_Button = button.Button(1229, 30, pause_img, 3)
play_Button = button.Button(540, 324, play_img, 5)
exit_small_Button = button.Button(640, 324, exit_small_img, 5)
restart_small_Button = button.Button(640, 420, restart_small_img, 5)
settings_button = button.Button(540, 420, settings_small_img, 5)
settings_button2 = button.Button(620, 606, settings_small_img, 4)
exit_small_Button2 = button.Button(620, 606, exit_small_img, 4)

plus_1_Button = button.Button(800, 75, plus_small_img, 3)
minus_1_Button = button.Button(850, 75, minus_small_img, 3)
plus_2_Button = button.Button(800, 140, plus_small_img, 3)
minus_2_Button = button.Button(850, 140, minus_small_img, 3)
settings_back_btn = button.Button(548, 600, back_btn, 2)

Game_Icon_btn = button.Button(520, 200, Icon, 4)

# create sprite groups
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
# load in level data and create world
with open(f"level{level}_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)
world = World()
player, health_bar = world.process_data(world_data)

run = True
while run:

    if start_game == False:
        # draw menu
        screen.fill(WHITE)
        # add buttons
        Game_Icon_btn.draw(screen)
        if start_Button.draw(screen):
            start_game = True
        if exit_Button.draw(screen):
            run = False
        if settings_button2.draw(screen) and settings_menu == False:
            settings_menu = True
        draw_text("HUBBA BUBBA", font4, BLACK, 380, 100)

        if settings_menu == True:
            if pause_game == False:
                screen.blit(pause_BG, (0, 0))
            screen.blit(Settings_Square, (340, 20))
            draw_text(f'Gravity: {gravity_text}', font3, BLACK, 400, 83)

            if minus_1_Button.draw(screen):
                if GRAVITY >= 0.20:
                    GRAVITY -= 0.10
                    gravity_text -= 1
            if plus_1_Button.draw(screen):
                if GRAVITY <= 1.00:
                    GRAVITY += 0.10
                    gravity_text += 1
            if exit_small_Button2.draw(screen):
                settings_menu = False

            draw_text("Placeholder", font3, BLACK, 400, 150)
            if minus_2_Button.draw(screen):
                pass
            if plus_2_Button.draw(screen):
                pass

    else:
        # update background
        draw_bg()
        # draw world map
        world.draw()
        # show player health
        health_bar.draw(player.health)

        screen.blit(Ammo_etc_bg, (973, 33))
        # show lifes
        screen.blit(heart_img, (985, 45))
        draw_text(f": {lifes}", font, BLACK, 1010, 45)
        # show coins
        screen.blit(coins_img, (982.5, 69))
        draw_text(f": {coins}", font, BLACK, 1010, 75)
        # show ammo
        screen.blit(bullet_gui_img, (1150, 45))
        draw_text(f": {player.ammo}", font, BLACK, 1170, 45)
        # show grenades
        screen.blit(grenade_img, (1150, 75))
        draw_text(f": {player.grenades}", font, BLACK, 1170, 75)

        player.update()
        player.draw()

        for enemy in enemy_group:
            enemy.ai()
            enemy.update()
            enemy.draw()

        # update and draw groups
        bullet_group.update()
        grenade_group.update()
        explosion_group.update()
        item_box_group.update()
        decoration_group.update()
        water_group.update()
        exit_group.update()

        bullet_group.draw(screen)
        grenade_group.draw(screen)
        explosion_group.draw(screen)
        item_box_group.draw(screen)
        decoration_group.draw(screen)
        water_group.draw(screen)
        exit_group.draw(screen)

        # update player actions
        if player.alive and pause_game == False:
            # shoot bullets
            if shoot:
                player.shoot()
            # grenades
            elif grenade and grenade_thrown == False and player.grenades > 0:
                grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction), \
                                  player.rect.top, player.direction)
                grenade_group.add(grenade)
                # reduce grenades
                player.grenades -= 1
                grenade_thrown = True
            if player.in_air:
                player.update_action(2)  # 2 means jump
            elif moving_left or moving_right:
                player.update_action(1)  # 1 means run
            else:
                player.update_action(0)  # 0 means idle
            screen_scroll, level_complete = player.move(moving_left, moving_right)
            bg_scroll -= screen_scroll
            # check if player has completed the level
            if level_complete:
                level += 1
                bg_scroll = 0
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    with open(f"level{level}_data.csv", newline="") as csvfile:
                        reader = csv.reader(csvfile, delimiter=",")
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)

        else:
            screen_scroll = 0
            screen.blit(pause_BG, (0, 0))
            if pause_game == False:
                if restart_Button.draw(screen):
                    bg_scroll = 0
                    world_data = reset_level()
                    # load level
                    with open(f"level{level}_data.csv", newline="") as csvfile:
                        reader = csv.reader(csvfile, delimiter=",")
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)

        if pause_game == True and player.alive:
            screen.blit(pause_BG, (0, 0))
            screen.blit(Pause_Square, (475, 180))
            for enemy in enemy_group:
                enemy.speed = 0
            player.speed = 0
            draw_text('Paused', font2, BLACK, 533, 240)
            if play_Button.draw(screen) and settings_menu == False:
                pause_game = False
                player.speed = 5
                for enemy in enemy_group:
                    enemy.speed = 2
                grenade_group
                explosion_group

            if exit_small_Button.draw(screen) and settings_menu == False:
                start_game = False
                pause_game = False

            if settings_button.draw(screen) and settings_menu == False:
                settings_menu = True

            if restart_small_Button.draw(screen) and settings_menu == False:
                bg_scroll = 0
                world_data = reset_level()
                # load level
                with open(f"level{level}_data.csv", newline="") as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)
                world = World()
                player, health_bar = world.process_data(world_data)

                pause_game = False

        if settings_menu == True:
            if pause_game == False:
                screen.blit(pause_BG, (0, 0))
            screen.blit(Settings_Square, (340, 20))
            draw_text(f'Gravity: {gravity_text}', font3, BLACK, 400, 83)

            if minus_1_Button.draw(screen):
                if GRAVITY >= 0.20:
                    GRAVITY -= 0.10
                    gravity_text -= 1
            if plus_1_Button.draw(screen):
                if GRAVITY <= 1.00:
                    GRAVITY += 0.10
                    gravity_text += 1
            if exit_small_Button2.draw(screen):
                settings_menu = False

        if level == 11:
            world_number = 2
        elif level == 21:
            world_number = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True
                jump_fx.play()

            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP and player.alive:
                player.jump = True

            if event.key == pygame.K_e:
                shoot = True
                shot_fx.play()
            if event.key == pygame.K_q:
                grenade = True
            if event.key == pygame.K_ESCAPE and start_game == True:
                pause_game = True
            if event.key == pygame.K_F10 and pause_game == True:
                pause_game = False
                player.speed = 5
                for enemy in enemy_group:
                    enemy.speed = 2
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        # Keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_e:
                shoot = False

            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_e:
                shoot = False

            if event.key == pygame.K_q:
                grenade = False
                grenade_thrown = False

        if discord_richpicture == True:
            RPC.update(
                large_image="game_icon",  # name of your asset
                large_text="Hubba Bubba",
                details=f"Level {level} ",
                state="Playing",
                start=start,
                buttons=[{"label": "Twitter", "url": "https://twitter.com/dasvegy"},
                         {"label": "Twitch", "url": "https://twitch.tv/dasvegy"}]
            )

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
