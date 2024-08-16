import pygame
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.score_font = pygame.font.SysFont("comicsans", 40)
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.running = True

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
