import pygame
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.entity = Entity(self.sprites)
        entity = Entity(self.sprites, position=(100, 100))

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.sprites.update()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill("lightblue")
        self.sprites.draw(self.screen)
        pygame.display.update()

    def close(self):
        pygame.quit()
        sys.exit()


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((64, 64)), position=(0, 0)) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        self.rect.x += 1


if __name__ == "__main__":
    game = Game()
    game.run()
