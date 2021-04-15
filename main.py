import pygame


# creates a game Windows
BLACK = (0, 0, 0)
WHITE = (255,255, 255)
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
screen.fill(BLACK)

class Pacman(pygame.sprite.Sprite):
  '''represents pacman '''
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.name = "pacman"
    # loads in the image
    self.image = pygame.image.load('images/pacman.png').convert()
    self.x, self.y = 50, 5
    # gets the position of the image
    self.rect = self.image.get_rect()
    screen.blit(self.image, self.rect)


  def move(self):
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
      self.x -= 4
    elif key[pygame.K_RIGHT]:
      self.x += 4
    elif key[pygame.K_UP]:
      self.y -= 4
    elif key[pygame.K_DOWN]:
      self.y += 4
    
    self.rect = (self.x, self.y, width, height)
  
  def update(self, screen, clock):
    self.move()
    clock.tick(75)
    screen.fill(BLACK)
    screen.blit(self.image, self.rect)
    pygame.display.flip()
    


def main():
  clock = pygame.time.Clock()
  run = True
  pm = Pacman()

  while run:
    # sets FPS
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()

    pm.update(screen, clock)
    
main()


