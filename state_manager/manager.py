import pygame
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.state_manager = GameStateManager("start")
        self.start = Start(self.screen, self.state_manager)
        self.level = Level(self.screen, self.state_manager)
        self.states = {"start": self.start, "level": self.level}

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                print("event", event)
                self.state_manager.state = "level"

    def draw(self):
        self.states[self.state_manager.state].draw()
        pygame.display.update()
        self.clock.tick(60)
        # self.screen.fill("lightblue")

    def close(self):
        pygame.quit()
        sys.exit()


class GameStateManager:
    def __init__(self, initial_state) -> None:
        self.state = initial_state


class Level:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def draw(self):
        self.display.fill("blue")


class Start:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def draw(self):
        self.display.fill("red")


if __name__ == "__main__":
    game = Game()
    game.run()
