import pygame
import random

class Level:
    def __init__(self, difficulty):
        self.difficulty = difficulty
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    def new_level(self, player):
        global walls, win_rect
        walls = []

        if self.difficulty == "E":
            walls_to_add = 3
        elif self.difficulty == "M":
            walls_to_add = 5
        elif self.difficulty == "H":
            walls_to_add = 10
        for i in range(walls_to_add):
            walls.append(self.wallgen(player))
        win_rect = self.wallgen(player)
        player.reset()

    def wallgen(self,player):
        while True:
            amountx = random.randint(0,WIDTH)
            amounty = random.randint(0,HEIGHT)
            amountw = random.randint(50,100)
            amounth = random.randint(50,100)
            rect = pygame.Rect(amountx, amounty, amountw, amounth)
            if not player.colliding_with_rect(rect):
                return pygame.Rect(amountx, amounty, amountw, amounth)



class Player(Level,object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(30, 30, 60, 60)

    def die(self):
        print("You died")
        Level.set_difficulty(self,difficulty)
        Level.new_level(self,player)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 5
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 5
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= 5
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += 5
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.die()

    def colliding_with_rect(self, rect):
        return self.rect.colliderect(rect)

    def end_goal(self, win_rect):
        if self.colliding_with_rect(win_rect):
            print("You win")
            Level.set_difficulty(self,difficulty)
            Level.new_level(self,player)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

pygame.init()
vec = pygame.math.Vector2 

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 120
walls = []
win_rect = None
difficulty = "E"

player = Player()



clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")


print("Enter difficulty, E/M/H")
difficulty = input().upper()
level = Level(difficulty)
level.new_level(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_keys()
    for wall in walls:
        if player.colliding_with_rect(wall):
            player.die()
    player.end_goal(win_rect)


    displaysurface.fill((0,0,0))
    for wall in walls:
      pygame.draw.rect(displaysurface, (255, 255, 255), wall)
    pygame.draw.rect(displaysurface, (0, 255, 0), win_rect)

    player.draw(displaysurface) 

    pygame.display.flip()         
    clock.tick(60)                
