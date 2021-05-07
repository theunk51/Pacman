import pygame
import matplotlib.pyplot as plt
# creates a game Windows
''''
BLACK = (0, 0, 0)
WHITE = (255,255, 255)
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
screen.fill(BLACK)




def main():
  clock = pygame.time.Clock()
  run = True

  while run:
    # sets FPS
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()

    pm.update(screen, clock)
    
main()
'''

image_pos= []
img = [] 

class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

ss = SpriteSheet('images/ghost-sheet.png')
img = ss.image_at((12, 11, 44, 44), colorkey=(255, 255, 255))
plt.imshow(img)