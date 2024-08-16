import pygame
import sys

DISPLAY_W, DISPLAY_H = 800, 600


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("First game")
        self.clock = pygame.time.Clock()
        self.sprite_sheet = pygame.image.load("trainer_sheet.png").convert()

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(60)

    def draw(self):
        self.screen.fill("lightblue")
        sprite = pygame.Surface((128, 128))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (0, 0, 128, 128))
        self.screen.blit(sprite, (0, DISPLAY_H - 128))
        pygame.display.update()

    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
