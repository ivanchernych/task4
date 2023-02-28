import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Cursor(pygame.sprite.Sprite):
    def __init__(self, cursor, image):
        super().__init__(cursor)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def mixing(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Game:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)
        self.start_game()

    def start_game(self):
        cursor = pygame.sprite.Group()
        image = load_image('arrow.png', -1)
        screen = pygame.display.set_mode(size)
        cur = Cursor(cursor, image)

        FPS = 60
        tick = 0
        clock = pygame.time.Clock()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEMOTION:
                    cur.mixing(event.pos)
            screen.fill((0, 0, 0))

            tick += 1
            clock.tick(FPS)
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
                cursor.update()
                cursor.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height, = 600, 300
    Game(size)