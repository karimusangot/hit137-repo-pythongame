import pygame


class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None

        while not done:
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y))

            pygame.display.flip()
            self.clock.tick(60) #refresh rate
            self.screen.fill((255, 255, 222))

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
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen,  
                         (104, 185, 70), 
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05 # pixel per frame

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
                         (254, 52, 110),  
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2  


if __name__ == '__main__':
    game = Game(600, 400)
