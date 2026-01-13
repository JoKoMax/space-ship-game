# ======================
# IMPORT
# ======================
import pygame
import pygame_widgets
import random
import time
import math
from pygame_widgets.button import Button

pygame.init()

# ======================
# SETUP
# ======================
screen_w, screen_h = 1200, 800
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Space Ship Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 200, 50)
PURPLE = (128, 0, 128)
PINK = (255, 0, 255)
TURQUOISE = (0, 255, 200)
DARK_GREEN = (39, 81, 31)
PALE_GREEN = (225, 255, 225)



# ======================
# GAME STATES
# ======================
MENU = "menu"
PLAYING = "playing"
UPGRADES = "upgrades"

game_state = MENU

player_size = 70

player_color = GREEN
player_speed = 10
player_x = screen_w // 2
player_y = screen_h - player_size - 10
player_health = 10  # Spieler hat nur 1 Leben
player_new_health = 10

gun_count = 1

bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullet_count = 1
bullet_count_a = 1
bullets = []

enemy_bullet_width = 5
enemy_bullet_height = 10
enemy_bullets = []
healer_radius = 200
healer_cooldown = 0.05

boss_enemy_spawn_cooldown = 5
last_boss_shot_time = 0

bar_x = 0
bar_y = 0
bar_width = 0
bar_height = 0
hp_ratio = 0

# Lplayer_size = 70

player_color = GREEN
player_speed = 10
player_x = screen_w // 2
player_y = screen_h - player_size - 10
player_health = 10  # Spieler hat nur 1 Leben
player_new_health = 10

gun_count = 1
player_size = 70

player_color = GREEN
player_speed = 10
player_x = screen_w // 2
player_y = screen_h - player_size - 10
player_health = 10  # Spieler hat nur 1 Leben
player_new_health = 10

gun_count = 1

bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullet_count = 1
bullet_count_a = 1
bullets = []

enemy_bullet_width = 5
enemy_bullet_height = 10
enemy_bullets = []
healer_radius = 200
healer_cooldown = 0.05

bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullplayer_size = 70

player_color = GREEN
player_speed = 10
player_x = screen_w // 2
player_y = screen_h - player_size - 10
player_health = 10  # Spieler hat nur 1 Leben
player_new_health = 10

gun_count = 1

bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullet_count = 1
bullet_count_a = 1
bullets = []

enemy_bullet_width = 5
enemy_bullet_height = 10
enemy_bullets = []
healer_radius = 200
healer_cooldown = 0.05

boss_enemy_spawn_cooldown = 5
last_boss_shot_time = 0

bar_x = 0
bar_y = 0
bar_width = 0
bar_height = 0
hp_ratio = 0

# Lplayer_size = 70

player_color = GREEN
player_speed = 10
player_x = screen_w // 2
player_y = screen_h - player_size - 10
player_health = 10  # Spieler hat nur 1 Leben
player_new_health = 10

gun_count = 1
player_size = 70
et_count = 1
bullet_count_a = 1
bullets = []

enemy_bullet_width = 5
enemy_bullet_height = 10
enemy_bullets = []
healer_radius = 200
healer_cooldown = 0.05
#skaliere das Bild
enemy_1_img = pygame.image.load("enemy_1.png").convert_alpha()
enemy_1_size = 50
enemy_1_img = pygame.transform.scale(enemy_1_img, (enemy_1_size, enemy_1_size))

enemy_2_img = pygame.image.load("enemy_2.png").convert_alpha()
enemy_2_size = 30
enemy_2_img = pygame.transform.scale(enemy_2_img, (enemy_2_size, enemy_2_size))

# Gegner-Daten
#{"color": , "speed": , "size": , "health": , "firerate":, "damage":, "":, "bulletsize":,"type": "","max_health":}
enemy_types = [
    {"enemy_img": enemy_1_img,"color": RED, "speed": 1, "size": 50, "health": 2, "firerate":0.02, "damage":2, "bulletcolor":BLUE, "bulletsize":5,"type": "standard","max_health":2},
    {"enemy_img": enemy_2_img,"color": BLACK, "speed": 2, "size": 30, "health": 1, "firerate":0.02, "damage":1, "bulletcolor":BLUE, "bulletsize":8,"type": "fast","max_health":1},
    {"enemy_img": enemy_1_img,"color": BLUE, "speed": 1, "size": 50, "health": 2, "firerate":0.02, "damage":2, "bulletcolor":BLUE, "bulletsize":10,"type": "aiming","max_health":2},
    {"enemy_img": enemy_1_img,"color": PURPLE, "speed": 0.5, "size": 70, "health": 12, "firerate":0.005, "damage":5, "bulletcolor":YELLOW, "bulletsize":15,"type": "Tank","max_health":12},
    {"enemy_img": enemy_1_img,"color": DARK_GREEN, "speed": 1, "size": 60, "health": 10, "firerate":0, "damage":0, "bulletcolor":DARK_GREEN, "bulletsize":0,"type": "healer","max_health":10}
]
boss_types = [
    {"enemy_img": enemy_1_img,"color": BLACK, "speed": 0, "size": 200, "health": 100, "firerate":0.01, "damage":10, "bulletcolor":RED, "bulletsize":20,"type": "Boss1","max_health":100},
    {"enemy_img": enemy_1_img,"color": BLACK, "speed": 0, "size": 200, "health": 200, "firerate":0.1, "damage":15, "bulletcolor":RED, "bulletsize":30,"type": "Boss2","max_health":200}
]

enemies = []

# Power-Up-Daten
power_up_size = 30
power_up_types = [
    {"color": RED, "type": "health"},
    {"color": BLUE, "type": "shotgun"},
    {"color": PURPLE, "type": "invincibility"},
    {"color": PINK, "type": "quikfire"} ,
    {"color": YELLOW, "type": "bigcoin"}
]
power_ups = []
power_up_spawn_chance = 1  # 1% Wahrscheinlichkeit, dass ein Power-Up spawnt

# Münzsystem
coins =10000
coin_size = 20
coin_color = YELLOW
coins_collected = []

# Game variables
level = 1
enemy_respawn_time = 1  # Sekunden bis der Gegner wieder erscheint

# Schuss-Cooldown (in Sekunden)
shoot_cooldown = 1  # 500 ms zwischen den Schüssen
last_shot_time = 0
shoot_cool = 0.6

# Power-Up-Effekte
shotgun_active = False
invincibility_active = False
quikfire_active = False
# Dauer der Power-Ups in Sekunden
power_up_shotgun_duration = 10
power_up_invincibility_duration = 7.5
power_up_quikfire_duration = 10

power_up_shotgun_end_time = 0
power_up_invincibility_end_time = 0
power_up_quikfire_end_time = 0

# Menü und Upgrade-Baum
menu_active = True
upgrades = {
    "speed": {"base_cost": 20, "level": 1, "max_level": 3},
    "health": {"base_cost": 30, "level": 1, "max_level": 25},
    "bullet_speed": {"base_cost": 40, "level": 1, "max_level": 5},
    "fire_rate": {"base_cost": 50, "level": 1, "max_level": 5},
    "bullet_size": {"base_cost": 60, "level": 1, "max_level": 6},
    "bullet_count": {"base_cost": 100, "level":1,"max_level":5}
}

# Setze die Framerate
clock = pygame.time.Clock()

# Font für Score oder andere Anzeigen
font = pygame.font.SysFont(None, 36)

# Spielerbild laden (einmal beim Start des Spiels)
player_nothing_img = pygame.image.load("player_ship_nothing.png").convert_alpha()
player_nothing_img = pygame.transform.scale(player_nothing_img, (player_size, player_size))

player_gun1_img = pygame.image.load("player_ship_gun1.png").convert_alpha()
player_gun1_img = pygame.transform.scale(player_gun1_img, (player_size, player_size))

player_gun2_3_img = pygame.image.load("player_ship_gun2_3.png").convert_alpha()
player_gun2_3_img = pygame.transform.scale(player_gun2_3_img, (player_size, player_size))

player_gun4_5_img = pygame.image.load("player_ship_gun4_5.png").convert_alpha()
player_gun4_5_img = pygame.transform.scale(player_gun4_5_img, (player_size, player_size))

player_shield1_img = pygame.image.load("player_ship_shield1.png").convert_alpha()
player_shield1_img = pygame.transform.scale(player_shield1_img, (player_size, player_size))


# Soundeffekte initialisieren
pygame.mixer.init()
#shoot_sound = pygame.mixer.Sound("shoot.wav")
#hit_sound = pygame.mixer.Sound("hit.wav")

# ======================
# BUTTON STATE
# ======================
start_clicked = False

def start_game():
    global start_clicked
    start_clicked = True

start_button = Button(
    screen,
    screen_w//2 - 150, screen_h//2,
    300, 120,
    text="START",
    fontSize=50,
    inactiveColour=RED,
    pressedColour=GREEN,
    onClick=start_game
)

# ======================
# RESET GAME
# ======================
def reset_game():
    print("Spiel gestartet / zurückgesetzt")
    global player_x, player_y, player_health, bullets, enemies, level, enemy_speed, shotgun_active, invincibility_active, coins_collected
    player_x = screen_w // 2
    player_y = screen_h - player_size - 10
    player_health = player_new_health
    bullets.clear()
    enemies.clear()
    power_ups.clear()
    coins_collected.clear()
    level = 1
    enemy_speed = 1  # Geschwindigkeit der Gegner zu Beginn
    shotgun_active = False
    invincibility_active = False
    quikfire_active = False
    spawn_enemy()

# ======================
# MENU
# ======================
def menu_loop(events):
    global game_state, start_clicked

    screen.fill(WHITE)

    title = font.render("SPACE SHIP GAME", True, BLACK)
    screen.blit(title, (screen_w//2 - title.get_width()//2, 200))

    start_button.draw()
    pygame_widgets.update(events)

    if start_clicked:
        start_clicked = False
        reset_game()
        game_state = PLAYING
# ======================
# GAME DEFs
# ======================

# Gegner spawnen
def spawn_enemy():
    global enemies
    enemy_count = 1
    if(level == 2):
        enemy_count =(0)
        enemy_type = enemy_types[0]
        enemy_x = random.randint(0, screen_width - enemy_type["size"])
        enemy_y = random.randint(0, screen_height // 2-10)
        enemies.append({"enemy_img": enemy_type["enemy_img"],"x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})
    elif(level == 6):
        enemy_count =(0)
        enemy_type = enemy_types[1]
        enemy_x = random.randint(0, screen_width - enemy_type["size"])
        enemy_y = random.randint(0, screen_height // 2-10)
        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})
    elif(level == 11):
        enemy_count =(0)
        enemy_type = enemy_types[3]
        enemy_x = random.randint(0, screen_width - enemy_type["size"])
        enemy_y = random.randint(0, screen_height // 2-10)
        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})
    elif(level == 16):
        enemy_count =(0)
        enemy_type = enemy_types[4]
        enemy_x = random.randint(0, screen_width - enemy_type["size"])
        enemy_y = random.randint(0, screen_height // 2-10)
        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})
    elif(level == 26):
        enemy_count =(0)
        enemy_type = boss_types[0]
        enemy_x = screen_width / 2-10#random.randint(0, screen_width - enemy_type["size"])
        enemy_y = 75#random.randint(0, screen_height // 2)
        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})
    elif(level == 51):
        enemy_count =(0)
        enemy_type = boss_types[1]
        enemy_x = screen_width / 2-10#random.randint(0, screen_width - enemy_type["size"])
        enemy_y = 75#random.randint(0, screen_height // 2)
        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})

    elif(level<6):
        enemy_count =(level -2)
    elif(level<11):
        enemy_count =(level - 6)
    elif(level<16):
        enemy_count =(level - 11)
    elif(level<26):
        enemy_count =(level - 16)
    elif(level<51):
        enemy_count =(level - 16)
    elif(level>51):
        enemy_count =(level - 16)
                
    #enemy_count =(level - 1)
    for _ in range(enemy_count):  # Anfangs nur 3 Gegner
        #enemy_type = random.choice(enemy_types)
        if(level<6):
            enemy_type = enemy_types[0]
        elif(level<11):
            enemy_type = enemy_types[random.randint(0, 1)]#random.choice(enemy_types1)
        elif(level<16):
            enemy_type = enemy_types[random.randint(0, 2)]#random.choice(enemy_types2)
        else:
            enemy_type = enemy_types[random.randint(0,4)]
        enemy_x = random.randint(0, screen_width - enemy_type["size"])
        enemy_y = random.randint(0, screen_height // 2)
        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})

# Power-Up spawnen
def spawn_power_up():
    if random.random() < power_up_spawn_chance:
        power_up_type = random.choice(power_up_types)
        power_up_x = random.randint(0, screen_width - power_up_size)
        power_up_y = random.randint(0, screen_height - power_up_size)
        power_ups.append({"x": power_up_x, "y": power_up_y, "color": power_up_type["color"], "type": power_up_type["type"]})

# Münzen spawnen
def spawn_coin():
    coin_x = random.randint(0, screen_width - coin_size)
    coin_y = random.randint(0, screen_height - coin_size)
    coins_collected.append({"x": coin_x, "y": coin_y})
    
# Münzen einsammeln
def collect_coin(player_x, player_y):
    global coins
    for coin in coins_collected[:]:
        if (player_x < coin["x"] + coin_size and
            player_x + player_size > coin["x"] and
            player_y < coin["y"] + coin_size and
            player_y + player_size > coin["y"]):
            coins_collected.remove(coin)
            coins += 1

def collect_power_up(player_x, player_y):
    global player_health, shotgun_active, invincibility_active, quikfire_active, power_up_end_time, coins
    global power_up_shotgun_end_time, power_up_invincibility_end_time, power_up_quikfire_end_time

    current_time = time.time()
    for power_up in power_ups[:]:
        if (player_x < power_up["x"] + power_up_size and
            player_x + player_size > power_up["x"] and
            player_y < power_up["y"] + power_up_size and
            player_y + player_size > power_up["y"]):
            power_ups.remove(power_up)
            if power_up["type"] == "health":
                player_health += 5
                print("powerup_health")
            elif power_up["type"] == "shotgun":
                shotgun_active = True
                power_up_shotgun_end_time = current_time + power_up_shotgun_duration
                print("powerup_shotgun")
            elif power_up["type"] == "invincibility":
                invincibility_active = True
                power_up_invincibility_end_time = current_time + power_up_invincibility_duration
                print("powerup_invincibility")
            elif power_up["type"] == "quikfire":
                quikfire_active = True
                power_up_quikfire_end_time = current_time + power_up_quikfire_duration
                print("powerup_quikfire")
            elif power_up["type"] == "bigcoin":
                coins += 5
                print("powerup_bigcoin")








# ======================
# GAME
# ======================
def game_loop(events):
    global game_state

    screen.fill((180, 230, 180))

    text = font.render("SPIEL LÄUFT", True, BLACK)
    screen.blit(text, (50, 50))

    info = font.render("U = Upgrades | ESC = Menü", True, BLACK)
    screen.blit(info, (50, 120))

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                game_state = UPGRADES
            if event.key == pygame.K_ESCAPE:
                game_state = MENU

            # Ereignisbehandlung
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        show_upgrades = not show_upgrades;
                    if event.key == pygame.K_1:
                        buy_upgrade("speed")
                    if event.key == pygame.K_2:
                        buy_upgrade("health")
                    if event.key == pygame.K_3:
                        buy_upgrade("bullet_speed")
                    if event.key == pygame.K_4:
                        buy_upgrade("fire_rate")
                    if event.key == pygame.K_5:
                        buy_upgrade("bullet_size")
                    if event.key == pygame.K_6:
                        buy_upgrade("bullet_count")

            # Bewegung des Spielers
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
            if keys[pygame.K_UP]:
                player_y -= player_speed
            if keys[pygame.K_DOWN]:
                player_y += player_speed

            # Begrenzung der Bewegung innerhalb des Fensters
            player_x = max(0, min(screen_width - player_size, player_x))
            player_y = max(0, min(screen_height - player_size, player_y))
            
            
            #shotgun_active = True
            # Schießen (mit Cooldown)
            #quikfire_active = True
            if quikfire_active:
                shoot_cool = shoot_cooldown / 2
            else:
                shoot_cool = shoot_cooldown
            current_time = time.time()
            if keys[pygame.K_SPACE] and current_time - last_shot_time >= shoot_cool:
                bullet_x = player_x + player_size // 2 - bullet_width // 2
                bullet_y = player_y
                #bullets.append([bullet_x, bullet_y])
                if shotgun_active == True:
                    bullet_count_a = bullet_count*3
                else:
                    bullet_count_a = bullet_count

                bullet_spacing = 20 # oder ein anderer sinnvoller Wert

                if bullet_count_a == 1:
                    bullets.append([bullet_x, bullet_y])
                elif bullet_count_a % 2 == 0:
                    for i in range(bullet_count_a // 2):
                        offset = (i + 1) * (bullet_spacing/2)
                        bullets.append([bullet_x - offset, bullet_y])
                        bullets.append([bullet_x + offset, bullet_y])
                else:
                    bullets.append([bullet_x, bullet_y])
                    for i in range((bullet_count_a - 1) // 2):
                        offset = (i + 1) * bullet_spacing
                        bullets.append([bullet_x - offset, bullet_y])
                        bullets.append([bullet_x + offset, bullet_y])
           #shoot_sound.play()  # Soundeffekt abspielen
                print(bullets)
                last_shot_time = current_time  # Update die Zeit des letzten Schusses

            # Bullet-Bewegung
            for bullet in bullets[:]:
                bullet[1] -= bullet_speed
                if bullet[1] < 0:
                    bullets.remove(bullet)
            
            
            
            # Gegnerbewegung und Schießen
            for enemy in enemies[:]:
                enemy["x"] += enemy["direction"] * enemy["speed"]
                if enemy["x"] <= 0 or enemy["x"] >= screen_width - enemy["size"]:
                    enemy["direction"] *= -1  # Richtungswechsel bei Bildschirmrand
            
                # Gegner schießen
                if enemy["type"] == "aiming" or enemy["type"] == "Boss1":
                    if random.random() < enemy["firerate"]:  # 2% Wahrscheinlichkeit, dass der Gegner schießt
                        enemy_bullet_x = enemy["x"] + enemy["size"] // 2 - enemy["bulletsize"]/2 // 2
                        enemy_bullet_y = enemy["y"] + enemy["size"]
                        # Zielen auf den Spieler
                        bullet_dx = (player_x + player_size // 2 - enemy_bullet_x) / 50
                        bullet_dy = (player_y - enemy_bullet_y) / 50
                        enemy_bullets.append([enemy_bullet_x, enemy_bullet_y, bullet_dx, bullet_dy, enemy["damage"], enemy["bulletcolor"], enemy["bulletsize"]])
                else:
                    if random.random() < enemy["firerate"]:  # 2% Wahrscheinlichkeit, dass der Gegner schießt
                        enemy_bullet_x = enemy["x"] + enemy["size"] // 2 - enemy["bulletsize"]/2 // 2
                        enemy_bullet_y = enemy["y"] + enemy["size"]
                        enemy_bullets.append([enemy_bullet_x, enemy_bullet_y, 0, 5, enemy["damage"], enemy["bulletcolor"], enemy["bulletsize"]])

            # Gegner-Bullet-Bewegung
            for enemy_bullet in enemy_bullets[:]:
                enemy_bullet[0] += enemy_bullet[2]  # Bewegung in x-Richtung
                enemy_bullet[1] += enemy_bullet[3]  # Bewegung in y-Richtung
                if enemy_bullet[1] > screen_height or enemy_bullet[0] < 0 or enemy_bullet[0] > screen_width:
                    enemy_bullets.remove(enemy_bullet)

            # Kollision zwischen Spielerschüssen und Gegner
            for enemy in enemies[:]:
                for bullet in bullets[:]:
                    if (bullet[0] > enemy["x"] and bullet[0] < enemy["x"] + enemy["size"] and
                        bullet[1] > enemy["y"] and bullet[1] < enemy["y"] + enemy["size"]):
                        bullets.remove(bullet)
                        enemy["health"] = enemy["health"]-1
                        if enemy["health"] <= 0:
                            enemies.remove(enemy)
                            spawn_coin()# Gegner wird zerstört
                        #enemies.remove(enemy)  # Gegner wird zerstört
                        #hit_sound.play()  # Soundeffekt abspielen
                          # Münze spawnen
                        break

            # Kollision zwischen Gegner-Schüssen und Spieler
            for enemy_bullet in enemy_bullets[:]:
                if (enemy_bullet[0] > player_x and enemy_bullet[0] < player_x + player_size and
                    enemy_bullet[1] > player_y and enemy_bullet[1] < player_y + player_size):
                    enemy_bullets.remove(enemy_bullet)
                    if not invincibility_active:
                        player_health -= enemy_bullet[4]  # Spieler verliert Leben bei Treffer
                        if player_health <= 0:
                            menu_active = True  # Zurück zum Menü
                            reset_game()  # Spieler verliert, zurück zum Anfang
                            
                            
            for enemy in enemies[:]:
                if enemy["type"] == "Boss1":
                    current_time = time.time()
                    if current_time - last_boss_shot_time >= boss_enemy_spawn_cooldown:
                        last_boss_shot_time = current_time
                        enemy_type = enemy_types[random.randint(0,4)]
                        enemy_x = random.randint(0, screen_width - enemy_type["size"])
                        enemy_y = random.randint(0, screen_height // 2)
                        enemies.append({"enemy_img": enemy_type["enemy_img"], "x": enemy_x, "y": enemy_y, "direction": random.choice([-1, 1]), "speed": enemy_type["speed"], "color": enemy_type["color"], "size": enemy_type["size"], "health": enemy_type["health"], "firerate": enemy_type["firerate"], "damage": enemy_type["damage"], "bulletcolor": enemy_type["bulletcolor"], "bulletsize": enemy_type["bulletsize"], "type": enemy_type["type"], "max_health": enemy_type["max_health"], "healer_cooldown": healer_cooldown})
           
           #gegner heilen
            for enemy in enemies:
                if enemy["type"] != "healer":
                    for other in enemies:
                        if other["type"] == "healer":
                            enemy_x = enemy["x"] + enemy["size"] // 2
                            enemy_y = enemy["y"] + enemy["size"] // 2
                            healer_x = other["x"] + other["size"] // 2
                            healer_y = other["y"] + other["size"] // 2

                            distance = math.hypot(enemy_x - healer_x, enemy_y - healer_y)

                            if distance <= healer_radius:
                                #print("Heiler in der Nähe für:", enemy)
                                if enemy["health"] < enemy["max_health"]:
                                    if random.random() < enemy["healer_cooldown"]:
                                        enemy["health"] += 1
                                break

                        
                        
            # Power-Up einsammeln
            collect_power_up(player_x, player_y)

            # Münzen einsammeln
            collect_coin(player_x, player_y)

            # Power-Up-Effekte beenden
            #if current_time > power_up_shotgun_end_time:
                #shotgun_active = False
                
            #if current_time > power_up_invincibility_end_time:
                #invincibility_active = False
                
            #if current_time > power_up_quikfire_end_time:
                #quikfire_active = False
            
            current_time = time.time()

            if shotgun_active and current_time > power_up_shotgun_end_time:
                shotgun_active = False
                print("Shotgun deaktiviert")

            if invincibility_active and current_time > power_up_invincibility_end_time:
                invincibility_active = False
                print("Unverwundbarkeit deaktiviert")

            if quikfire_active and current_time > power_up_quikfire_end_time:
                quikfire_active = False
                print("Schnellfeuer deaktiviert")

                
            # Level-Steigerung
            if len(enemies) == 0:
                level += 1
                enemy_speed += 1  # Gegner werden schneller
                spawn_enemy()  # Neue Gegner erscheinen
                spawn_power_up()  # Neues Power-Up erscheint
            if invincibility_active == True:
                player_color = TURQUOISE
            else:
                player_color = GREEN
                
                
                
                
                
             
            #zeichen von healer aura    
            for enemy in enemies:
               if enemy["type"] == "healer":
                   pygame.draw.circle(screen, PALE_GREEN, (enemy["x"]+(enemy["size"]/2),enemy["y"]+(enemy["size"]/2)), 200, 0)

            # Zeichnen des Spielers (im Haupt-Zeichenbereich)
            screen.blit(player_nothing_img, (player_x, player_y))
            if gun_count == 1:
                screen.blit(player_gun1_img, (player_x, player_y))
            elif gun_count == 2:
                screen.blit(player_gun2_3_img, (player_x, player_y))
            elif gun_count == 3:
                screen.blit(player_gun2_3_img, (player_x, player_y))
                screen.blit(player_gun1_img, (player_x, player_y))
            elif gun_count == 4:
                screen.blit(player_gun2_3_img, (player_x, player_y))
                screen.blit(player_gun4_5_img, (player_x, player_y))
            elif gun_count == 5:
                screen.blit(player_gun1_img, (player_x, player_y))
                screen.blit(player_gun2_3_img, (player_x, player_y))
                screen.blit(player_gun4_5_img, (player_x, player_y))
            else:
                print("error_gun")
            # Zeichnen der Bullets
            for bullet in bullets:
                pygame.draw.rect(screen, RED, pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height))
            
            #zeichen der gegener
            for enemy in enemies:
                screen.blit(enemy["enemy_img"], (enemy["x"], enemy["y"]))

            for enemy in enemies:
                pygame.draw.rect(screen, enemy["color"], (enemy["x"], enemy["y"]-10, enemy["size"]*(enemy["health"]/enemy["max_health"]), 5))
            
            
            # Zeichnen der Gegner-Schüsse
            for enemy_bullet in enemy_bullets:
                pygame.draw.rect(screen, enemy_bullet[5], pygame.Rect(enemy_bullet[0], enemy_bullet[1], enemy_bullet[6], enemy_bullet[6]*2))

            # Zeichnen der Power-Ups
            for power_up in power_ups:
                pygame.draw.rect(screen, power_up["color"], pygame.Rect(power_up["x"], power_up["y"], power_up_size, power_up_size))
            
            # Zeichnen der Power-Ups Balken
            if shotgun_active == True:
                #print(int(screen_width / 2 - (power_up_shotgun_end_time - current_time) * 25))#debug
                #print(int((power_up_shotgun_end_time - current_time)*50))#debug
                rect_x = int(screen_width / 2 - (power_up_shotgun_end_time - current_time) * 25)
                rect_y = 0
                rect_width = int((power_up_shotgun_end_time - current_time) * 50)
                rect_height = 7
                pygame.draw.rect(screen, BLUE, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

            if invincibility_active == True:
                #print(int(screen_width / 2 - (power_up_invincibility_end_time - current_time) * 25))#debug
                #print(int((power_up_shotgun_end_time - current_time)*50))#debug
                rect_x = int(screen_width / 2 - (power_up_invincibility_end_time - current_time) * 25)
                rect_y = 8
                rect_width = int((power_up_invincibility_end_time - current_time) * 50)
                rect_height = 7
                pygame.draw.rect(screen, PURPLE, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

            if quikfire_active == True:
                #print(int(screen_width / 2 - (power_up_quikfire_end_time - current_time) * 25))#debug
                #print(int((power_up_quikfire_end_time - current_time)*50))#debug
                rect_x = int(screen_width / 2 - (power_up_quikfire_end_time - current_time) * 25)
                rect_y = 16
                rect_width = int((power_up_quikfire_end_time - current_time) * 50)
                rect_height = 7
                pygame.draw.rect(screen, PINK, pygame.Rect(rect_x, rect_y, rect_width, rect_height))


            for enemy in enemies:
                if enemy["type"] == "dgsgdbgdgbv":
                    # Boss zeichnen (z. B. als Rechteck)
                    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(enemy["x"], enemy["y"], enemy["size"], enemy["size"]))

                    # Boss-Text über dem Boss anzeigen
                    font = pygame.font.SysFont(None, 24)
                    text = font.render("BOSS", True, (255, 255, 255))
                    text_x = (enemy["x"] + enemy["size"] // 2 - text.get_width() // 2)
                    text_y = (enemy["y"] - 20)
                    screen.blit(text, (text_x, text_y))
                    hp_ratio = enemy["health"] / enemy["max_health"]
                    bar_width = enemy["size"]
                    bar_height = 6
                    bar_x = enemy["x"]
                    bar_y = enemy["y"] - 10

                pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(bar_x, bar_y, bar_width, bar_height))
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(bar_x, bar_y, int(bar_width * hp_ratio), bar_height))


                
            # Zeichnen der Münzen
            for coin in coins_collected:
                pygame.draw.rect(screen, coin_color, pygame.Rect(coin["x"], coin["y"], coin_size, coin_size))

            # Gesundheitsanzeige für den Spieler
            health_text = font.render(f"Health: {player_health}", True, BLACK)
            screen.blit(health_text, (10, 10))

            # Münzenanzeige
            coin_text = font.render(f"Coins: {coins}", True, BLACK)
            screen.blit(coin_text, (10, 50))

            # Level-Anzeige
            level_text = font.render(f"Level: {level-1}", True, BLACK)
            screen.blit(level_text, (screen_width - 100, 10))

            # Wenn der Spieler verloren hat, zeige einen Verlust-Bildschirm
            if player_health <= 0:
                game_over_text = font.render("Game Over! Drücke R, um neu zu starten", True, BLACK)
                screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2))
            
            owner_text = font.render("by max", True, BLACK)
            screen.blit(owner_text,(screen_width - 100, screen_height - 27))
            # Aktualisieren des Bildschirms
            
            #Debug
            #if shotgun_active == True:
                #print(power_up_shotgun_end_time - current_time)
            #print(shotgun_active)
            
            
            
            #pygame_widgets.update(events)
            pygame.display.update()

            # Framerate steuern
            clock.tick(60)


# ======================
# UPGRADES
# ======================
def upgrade_loop(events):
    global game_state

    screen.fill(WHITE)

    text = font.render("UPGRADES", True, BLACK)
    screen.blit(text, (SCREEN_W//2 - text.get_width()//2, 200))

    info = font.render("ESC = zurück", True, BLACK)
    screen.blit(info, (SCREEN_W//2 - info.get_width()//2, 300))

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = PLAYING

# ======================
# MAIN LOOP
# ======================
running = True
while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_state == MENU:
        menu_loop(events)
    elif game_state == PLAYING:
        game_loop(events)
    elif game_state == UPGRADES:
        upgrade_loop(events)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
