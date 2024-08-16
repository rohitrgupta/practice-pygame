import pygame
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

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
        pygame.display.update()

    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
