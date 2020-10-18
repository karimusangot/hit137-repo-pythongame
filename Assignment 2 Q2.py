"""
import pygame
pygame.init()

win = pygame.display.set_mode((600,400))

pygame.display.set_caption ("Space invaders")

bg=pygame.image.load('bg.png')
Alien=[pygame.image.load('OIP.jpg')]
Hero=[pygame.image.load('spaceship1.png')]

class Game:
    screen = win
    aliens = []
    rockets = []
    lost = False
 
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None

        #while not done:
        running=True    
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                       
          

            if len(self.aliens) == 0:
                self.displayText("VICTORY")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                hero.x -= 2 if hero.x > 20 else 0  
            elif pressed[pygame.K_RIGHT]: 
                hero.x += 2 if hero.x < width - 20 else 0 
            
            
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE : #and not self.lost:
                self.rockets.append(Rocket(self, hero.x, hero.y))

            #pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60) #refresh rate
            self.screen.blit(bg,(0,0))
            
            #self.screen.fill((10, 30, 10))

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)
                if (alien.y > height):
                    self.lost = True
                    self.displayText("DEFEAT")

            for rocket in self.rockets:
                rocket.draw()

            if not self.lost: hero.draw()

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
      
class Alien: #new alien class was created
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 10

    def draw(self):
        pygame.draw.rect(self.game.screen,  
                         (104, 185, 70), 
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05 # pixel per frame
        return Alien

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)


class Hero: # The hero is the character that controlled by the player
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (210, 250, 251),
                         pygame.Rect(self.x, self.y, 8, 5))
        return Hero


class Generator: # This class will be able to create more enemies
    def __init__(self, game):
        margin = 30  
        width = 50  
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

        # game.aliens.append(Alien(game, 280, 50))


class Rocket: # This is the weapon of the hero
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,  
                         (200, 20, 110),  
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2  


if __name__ == '__main__':
    game = Game(600, 400)
pygame.quit()
quit()"""

import pygame
from pygame import mixer

import math
import random

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((600, 600))

# Background image
background = pygame.image.load('bg.png')

# background sound
mixer.music.load("music_zapsplat_game_music_action_fast_paced_elelctro_sonic_011.mp3")
mixer.music.play(-5)

# Caption 
pygame.display.set_caption("Space Invader")

# Hero
heroImage = pygame.image.load('spaceship1.png')
heroX = 300
heroY = 530
heroX_change = 0

# Alien creation
alienImage = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 8
# Creation of more aliens with alien attributes
for i in range(num_of_aliens):
    alienImage.append(pygame.image.load('UFO.gif'))
    alienX.append(random.randint(0,580))
    alienY.append(random.randint(50, 150))
    alienX_change.append(2)
    alienY_change.append(30)

# Rocket creation 
rocketImage = pygame.image.load('bullet_1.png')
rocketX = 0
rocketY = 430
rocketX_change = 0
rocketY_change = 10
rocket_state = "ready"

# Score initialisation and its font and size
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
testY = 10

# Game over font
over_font = pygame.font.Font('freesansbold.ttf', 30)  

# Function to show score on the screen and its attributes
def show_score(x, y): 
    score = font.render("Score : " + str(score_value), True, (255, 200, 210))
    screen.blit(score, (x, y))

# Function to display game over on the screen with its attributes
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (200, 220, 240))
    screen.blit(over_text, (200, 250))

# Function to place player on the screen
def hero(x, y):
    screen.blit(heroImage, (x, y))

# Function to place the enermies on the screen
def alien(x, y, i):
    screen.blit(alienImage[i], (x, y))

# Function to fire artillery
def fire_rocket(x, y):
    global rocket_state
    rocket_state = "fire"
    screen.blit(rocketImage, (x + 16, y + 10))

# Function to check or determine collision
def isCollision(alienX, alienY, rocketX, rocketY):
    distance = math.sqrt(math.pow(alienX - rocketX, 2) + (math.pow(alienY - rocketY, 2)))
    if distance < 20:
        return True
    else:
        return False 


# Main loop for game controls
running = True
while running:
    hero(heroX, heroY)
    show_score(textX, testY)
    pygame.display.update()

    # Place background image on the screen
    screen.blit(background, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check whether key pressed is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                heroX_change = -5
            if event.key == pygame.K_RIGHT:
                heroX_change = 5
            if event.key == pygame.K_SPACE:
                if rocket_state is "ready":
                    bulletSound = mixer.Sound("Artillery+2.wav")
                    bulletSound.play()

                    # Current x cordinate of the spaceship and the bullet
                    rocketX = heroX
                    fire_rocket(rocketX, rocketY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                heroX_change = 0

    heroX += heroX_change
    if heroX <= 0:
        heroX = 0
    elif heroX >= 560:
        heroX = 535

    # Movement of the aliens on the screen
    for i in range(num_of_aliens):

        # Game over conditions detection and actions to be taken
        if alienY[i] > 460:
            for j in range(num_of_aliens):
                alienY[j] = 10000
            game_over_text()
            break

        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 1
            alienY[i] +=alienY_change[i]
        elif alienX[i] >=560:
            alienX_change[i] = -1
            alienY[i] +=alienY_change[i]

        # Collision event detection and action to be taken 
        collision = isCollision(alienX[i], alienY[i], rocketX, rocketY)
        if collision:
            explosionSound = mixer.Sound("Explosion+3.wav")
            explosionSound.play()
            rocketY = 460
            rocket_state = "ready"
            score_value += 1
            alienX[i] = random.randint(0,570)
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)

    # Bullet Movement
    if rocketY <= 0:
        rocketY = 460
        rocket_state = "ready"

    if rocket_state is "fire":
        fire_rocket(rocketX, rocketY)
        rocketY -= rocketY_change

pygame.quit()  