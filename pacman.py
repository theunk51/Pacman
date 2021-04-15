import pygame
'''
Displacement formula
s = ut + 1/2(a)^2

a = acceleration		s = displacement
u = velocity				t = time
'''

class Pacman(pygame.sprite.Sprite):
  def __init__(self):
    #Player.__init__(self, 4, 5, 13, 12, (255, 255, 0))
    super().__init__()
    self.image = pygame.image.load("images/pacman.png").convert()
    self.image.set_colorkey((0, 0, 0))
    self.rect = self.image.get_rect() # updates x and y
    pygame.gamedisplay.blit(self.image, (seld.))

  def move_sprite(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.x -= self.vel
    elif keys[pygame.K_RIGHT]:
      self.x += self.vel
    elif keys[pygame.K_UP]:
      self.y -= self.vel
    elif keys[pygame.K_DOWN]:
      self.y += self.vel

    self.rect = self.image.get_rect()

  def draw(self, window):
    pygame.draw.rect(window, self.image,)
  