import pygame
from pacman import Pacman
# creates a game Windows
BLACK = (0, 0, 0)

width, height = 500, 500
win = pygame.display.set_mode((width, height))
win.fill(BLACK)


def redrawWindow(win, player):
  win.fill((255, 255, 255))
  player.draw(win)
  pygame.display.update()

def main():
  run = True
  #p = Player(50, 50, 10, 10, (45, 234, 17))
  clock = pygame.time.Clock()

  while True:   
    clock.tick(75)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    pygame.display.update()


main()