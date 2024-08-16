import pygame
import sys
import random

BLOCK_SIZE = 20
ROWS = 20
COLS = 20
FONTSIZE = 30
SCREEN_WIDTH = ROWS * BLOCK_SIZE + 1
SCREEN_HEIGHT = COLS * BLOCK_SIZE + 1
FPS = 8


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.score_font = pygame.font.SysFont("comicsans", FONTSIZE)
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)
        self.dead = False
        self.score = 0

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        if self.dead:
            self.score = 0
            self.snake.reset()
            self.apple.spawn()
            self.dead = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.snake.y_dir = 1
                    self.snake.x_dir = 0
                elif event.key == pygame.K_UP:
                    self.snake.y_dir = -1
                    self.snake.x_dir = 0
                elif event.key == pygame.K_LEFT:
                    self.snake.y_dir = 0
                    self.snake.x_dir = -1
                elif event.key == pygame.K_RIGHT:
                    self.snake.y_dir = 0
                    self.snake.x_dir = 1
        self.snake.update()
        if self.snake.head in self.snake.body:
            self.dead = True
        if (
            self.snake.head[0] < 0
            or self.snake.head[0] >= COLS
            or self.snake.head[1] < 0
            or self.snake.head[1] >= ROWS
        ):
            self.dead = True
        if self.apple.x == self.snake.head[0] and self.apple.y == self.snake.head[1]:
            self.snake.grow()
            self.apple.spawn()
            self.score += 1
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill("darkblue")
        self.draw_grid()
        score_text = self.score_font.render(f"{self.score}", 1, "white")
        self.screen.blit(score_text, (5, 0))
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(self.screen, "darkgray", (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(self.screen, "darkgray", (0, y), (SCREEN_WIDTH, y))

    def close(self):
        pygame.quit()
        sys.exit()


class Apple:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.x = 10
        self.y = 10

    def spawn(self):
        self.x = random.randint(0, COLS - 1)
        self.y = random.randint(0, ROWS - 1)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            "red",
            (
                self.x * BLOCK_SIZE,
                self.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            ),
        )


class Snake:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.reset()

    def reset(self):
        self.x_dir = 1
        self.y_dir = 0
        self.head = [0, 0]
        self.body = [[0, 1], [0, 2]]

    def draw(self):
        c = self.head[0]
        r = self.head[1]
        for i in range(len(self.body)):
            pygame.draw.rect(
                self.screen,
                "green",
                (
                    self.body[i][0] * BLOCK_SIZE,
                    self.body[i][1] * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                ),
            )

        pygame.draw.rect(
            self.screen,
            "green",
            (c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
        )

        pygame.draw.rect(
            self.screen,
            "green",
            (c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
        )

    def grow(self):
        self.body.append(self.body[len(self.body) - 1])

    def update(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]
        self.body[0] = self.head
        self.head = [self.head[0] + self.x_dir, self.head[1] + self.y_dir]


if __name__ == "__main__":
    game = Game()
    game.run()
