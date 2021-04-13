import pygame



class Player():
  def __init__(self):
    pass


class Pacman(pygame.sprite.Sprite):
  def __init__(self):
    #Player.__init__(self, 4, 5, 13, 12, (255, 255, 0))
    super().__init__(self)
    self.image = pygame.image.load("pacman.png").convert()
    self.image.set_colorkey((0, 0, 0))
    self.rect = self.image.get_rect() # updates x and y

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

  def draw(self, window):
    pygame.draw.rect(window, self.image, self.rect)
  