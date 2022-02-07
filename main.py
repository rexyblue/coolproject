import time, random, asyncio, json
import pygame, math


# dog dog dog dog dog doge dog dog dog dog dog dog dog dog cat ~/.bashrc
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1046, 704
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.init()
pygame.display.set_caption("Testing")

clock = pygame.time.Clock()

arm_img = pygame.image.load('mitchellArm.png').convert_alpha()

policetape_img = pygame.image.load('police_tape.png').convert_alpha()

deadant_img = pygame.image.load('deadant.png').convert_alpha()

deadroach_img = pygame.image.load('sleepingroach.png').convert_alpha()

picnic_img = pygame.image.load('picnic_img.png').convert_alpha()

ant_img = pygame.image.load('ant_img').convert_alpha()

cockroach_img = pygame.image.load('cockroach_img.png').convert_alpha()

rat_img = pygame.image.load('rat.png').convert_alpha()
injuredrat_img = pygame.image.load('injuredrat.png').convert_alpha()
deadrat_img = pygame.image.load('deadrat.png').convert_alpha()

wolf_img = pygame.image.load('wolf.png').convert_alpha()
wolfheart4_img = pygame.image.load('wolfhealth4.png').convert_alpha()
wolfheart3_img = pygame.image.load('wolfhealth3.png').convert_alpha()
wolfheart2_img = pygame.image.load('wolfheart2.png').convert_alpha()
wolfheart1_img = pygame.image.load('wolfheart1.png').convert_alpha()
deadwolf_img = pygame.image.load('deadwolf.png').convert_alpha()


def draw_text(text, font, colour, x, y, pos="center"):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    setattr(text_rect, pos, (x, y))
    WINDOW.blit(text_obj, text_rect)

font_press_s = pygame.font.Font('Exan-Regular.ttf', 20)

draw_text("Press s to Start", font_press_s, (0, 0, 0), WIDTH // 2, HEIGHT // 2 + 100)git


original_ant_img = ant_img.copy()
ant_rect = ant_img.get_rect()
ant_rect.topright = (1000, 0)
left_click = False
ant_disappear = False

ant_img = pygame.transform.scale(ant_img, (120, 70))

cockroach_img = pygame.transform.scale(cockroach_img, (200, 120))
cockroach_img = pygame.transform.flip(cockroach_img, True, False)

deadant_img = pygame.transform.scale(deadant_img, (150, 105))
deadant_img = pygame.transform.flip(deadant_img, True, False)

deadroach_img = pygame.transform.scale(deadroach_img, (175, 110))

picnic_img = pygame.transform.scale(picnic_img, (700, 1046))
picnic_img = pygame.transform.rotate(picnic_img, 90)

policetape_img = pygame.transform.scale(policetape_img, (704, 200))
policetape_img = pygame.transform.rotate(policetape_img, 75)

arm_img = pygame.transform.scale(arm_img, (200, 1000))

rat_img = pygame.transform.scale(rat_img, (225, 150))
injuredrat_img = pygame.transform.scale(injuredrat_img, (225, 150))
deadrat_img = pygame.transform.scale(deadrat_img, (225, 150))

wolf_img = pygame.transform.flip(wolf_img, True, False)
wolf_img = pygame.transform.scale(wolf_img, (250, 150))
wolfheart4_img = pygame.transform.flip(wolfheart4_img, True, False)
wolfheart4_img = pygame.transform.scale(wolfheart4_img, (250, 150))
wolfheart3_img = pygame.transform.flip(wolfheart3_img, True, False)
wolfheart3_img = pygame.transform.scale(wolfheart3_img, (250, 150))
wolfheart2_img = pygame.transform.flip(wolfheart2_img, True, False)
wolfheart2_img = pygame.transform.scale(wolfheart2_img, (250, 150))
wolfheart1_img = pygame.transform.flip(wolfheart1_img, True, False)
wolfheart1_img = pygame.transform.scale(wolfheart1_img, (250, 150))


with open('./rounds.json') as f:
    rounds = json.load(f)

game_running = True

money = 0
round_num = 0

# async def spawn_round(round_number):




class MitchellArm(pygame.sprite.Sprite):
    def __init__(self, starting_pos):
        self.pos = [starting_pos[0] - 100, starting_pos[1] - 300]
        self.image = arm_img
        self.speed = 20

    def update(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            print("Remove arm")
            mitchell_arms.remove(self)

class AntClass(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.pos = pos
        self.image = ant_img
        self.speed = random.randint(4, 7)
        self.original_img = ant_img.copy()
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0
        self.worth = 1
        # self.health increases health

    def update(self):
        self.pos[0] -= self.speed

        self.rect.centerx = self.pos[0]


class CockroachClass(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.pos = pos
        self.image = cockroach_img
        self.speed = random.randint(4, 7)
        self.original_img = cockroach_img.copy()
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0
        self.health = 1

    def update(self):
        self.pos[0] -= self.speed

        self.rect.centerx = self.pos[0]

class RatClass(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.pos = pos
        self.image = rat_img
        self.speed = random.randint(6, 7)
        self.original_img = rat_img.copy()
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0
        self.health = 2

    def update_image(self):
        if self.health == 2:
            self.image = rat_img.copy()
        elif self.health == 1:
            self.image = injuredrat_img.copy()

        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.pos[0] -= self.speed
        self.rect.centerx = self.pos[0]

class WolfClass(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.pos = pos
        self.image = wolf_img
        self.speed = random.randint(3, 4)
        self.original_img = wolf_img.copy()
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0
        self.health = 5
        self.worth = 5

    def update_image(self):
        if self.health == 5:
            self.image = wolf_img.copy()
        elif self.health == 4:
            self.image = wolfheart4_img.copy()
        elif self.health == 3:
            self.image = wolfheart3_img.copy()
        elif self.health == 2:
            self.image = wolfheart2_img.copy()
        elif self.health == 1:
            self.image = wolfheart1_img.copy()

        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.pos[0] -= self.speed
        self.rect.centerx = self.pos[0]


spawn_ant = True
ant_spawn_timer = 0

spawn_cockroach = True
cockroach_spawn_timer = 0

spawn_rat = True
rat_spawn_timer = 0

spawn_wolf = True
wolf_spawn_timer = 0

cockroach_spawn_timer_start = 600
rat_spawn_timer_start = 1200
wolf_spawn_timer_start = 1800

mitchell_arms = []

cockroaches = []
deadroach_effects = []

rats = []
wolves = []

ants = []
deadrat_effects = []
deadant_effects = []
deadwolf_effects = []




while game_running:
    clock.tick(60)
    WINDOW.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    WINDOW.blit(picnic_img, (0, 0))
    WINDOW.blit(policetape_img, (0, 0))



    if spawn_ant:
        ant_spawn_timer = random.randint(100, 150)
        new_ant = AntClass([random.randint(1000, WIDTH), random.randint(0, HEIGHT)])
        ants.append(new_ant)  # List of all ants to track stuff
        spawn_ant = False
    else:
        ant_spawn_timer -= 1
        if ant_spawn_timer < 0:
            spawn_ant = True

    if spawn_rat and rat_spawn_timer_start <=0:
        rat_spawn_timer = random.randint(100, 150)
        new_rat = RatClass([random.randint(1000, WIDTH), random.randint(0, HEIGHT)])
        rats.append(new_rat)  # List of all ants to track stuff
        spawn_rat = False
    else:
        rat_spawn_timer -= 1
        if rat_spawn_timer < 0:
            spawn_rat = True

    if spawn_wolf and wolf_spawn_timer_start <= 0:
        wolf_spawn_timer = random.randint(100, 150)
        new_wolf = WolfClass([random.randint(1000, WIDTH), random.randint(0, HEIGHT)])
        wolves.append(new_wolf)  # List of all ants to track stuff
        spawn_wolf = False
    else:
        wolf_spawn_timer -= 1
        if wolf_spawn_timer < 0:
            spawn_wolf = True

    if spawn_cockroach and cockroach_spawn_timer_start <= 0:
        cockroach_spawn_timer = random.randint(100, 150)
        new_cockroach = CockroachClass([random.randint(1000, WIDTH), random.randint(0, HEIGHT)])
        cockroaches.append(new_cockroach)  # List of all ants to track stuff
        spawn_cockroach = False
    else:
        cockroach_spawn_timer -= 1
        if cockroach_spawn_timer < 0:
            spawn_cockroach = True

    for effect in deadant_effects:
        WINDOW.blit(deadant_img, (effect[0][0] - deadant_img.get_width() // 2, effect[0][1] - deadant_img.get_height() // 2))
        effect[1] -= 1
        if effect[1] <= 0:
            deadant_effects.remove(effect)

    for effect in deadrat_effects:
        WINDOW.blit(deadrat_img, (effect[0][0] - deadrat_img.get_width() // 2, effect[0][1] - deadrat_img.get_height() // 2))
        effect[1] -= 1
        if effect[1] <= 0:
            deadrat_effects.remove(effect)

    for effect in deadroach_effects:
        WINDOW.blit(deadroach_img, (effect[0][0] - deadroach_img.get_width() // 2, effect[0][1] - deadroach_img.get_height() // 2))
        effect[1] -= 1
        if effect[1] <= 0:
            deadroach_effects.remove(effect)

    for effect in deadwolf_effects:
        WINDOW.blit(deadwolf_img, (effect[0][0] - deadwolf_img.get_width() // 2, effect[0][1] - deadwolf_img.get_height() // 2))
        effect[1] -= 1
        if effect[1] <= 0:
            deadwolf_effects.remove(effect)

    for arm in mitchell_arms:
        arm.update()
        WINDOW.blit(arm.image, (arm.pos[0], arm.pos[1]))

    if left_click:
        new_arm = MitchellArm((mouse_x, mouse_y))
        mitchell_arms.append(new_arm)


    for ant in ants:
        WINDOW.blit(ant.image, ant.rect)
        ant.update()

        if ant.pos[0] < 160:
            # WINDOW.blit(endingscreen_img)
            pass

        if left_click:
            if ant.rect.collidepoint((mouse_x, mouse_y)):
                ants.remove(ant)
                deadant_effects.append([ant.pos, 255])
                money += ant.worth


    for rat in rats:
        WINDOW.blit(rat.image, rat.rect)
        rat.update()

        if rat.pos[0] < 160:
            pygame.quit()
            exit()

        if left_click:
            if rat.rect.collidepoint((mouse_x, mouse_y)):
                rat.health -= 1
                if rat.health <= 0:
                    rats.remove(rat)
                    money += 2
                    deadrat_effects.append([rat.pos, 255])
                else:
                    rat.update_image()

    for wolf in wolves:
        WINDOW.blit(wolf.image, wolf.rect)
        wolf.update()

        if wolf.pos[0] < 160:
            pygame.quit()
            exit()

        if left_click:
            if wolf.rect.collidepoint((mouse_x, mouse_y)):
                wolf.health -= 1
                if wolf.health <= 0:
                    wolves.remove(wolf)
                    deadwolf_effects.append([wolf.pos, 255])
                else:
                    wolf.update_image()


    for cockroach in cockroaches:
        WINDOW.blit(cockroach.image, cockroach.rect)
        cockroach.update()

        if cockroach.pos[0] < 160:
            pygame.quit()
            exit()

        if left_click:
            if cockroach.rect.collidepoint((mouse_x, mouse_y)):
                cockroach.health -= 1
                if cockroach.health <= 0:
                    cockroaches.remove(cockroach)
                    deadroach_effects.append([cockroach.pos, 255])
                else:
                    cockroach.update_image()


    left_click = False
    cockroach_spawn_timer_start -= 1
    rat_spawn_timer_start -= 1
    wolf_spawn_timer_start -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True

    pygame.display.update()



