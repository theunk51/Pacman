import pygame
from pacman import Pacman
# creates a game Windows
width, height = 500, 500
win = pygame.display.set_mode((width, height))

class Player():
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    # self.images = images (for aninamtions)
    self.rect = (x, y, width, height) # sprite location
    self.vel = 4 # how many pixel the sprite moves

  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect)

  def move(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
      self.x -= self.vel
    elif keys[pygame.K_RIGHT]:
      self.x += self.vel
    elif keys[pygame.K_UP]:
      self.y -= self.vel
    elif keys[pygame.K_DOWN]:
      self.y += self.vel

    self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win, player):
  win.fill((255, 255, 255))
  player.draw(win)
  pygame.display.update()

def main():
  run = True
  #p = Player(50, 50, 10, 10, (45, 234, 17))
  pm = Pacman()
  clock = pygame.time.Clock()

  while run:
    clock.tick(75)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    
    pm.move_sprite()
    redrawWindow(win, pm)

main()