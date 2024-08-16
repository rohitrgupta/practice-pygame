import pygame
import sys

WIDTH = 700
HEIGHT = 400
FPS = 60
BACKGROUND_COLOR = "blue"
PADDEL_COLOR = "white"
PADDEL_HEIGHT = 80
PADDEL_WIDTH = 10
PADDEL_VELOCITY = 0.2
LINEWIDTH = 4
BALL_COLOR = "yellow"
BALL_REDIOUS = 7
BALL_VELOCITY = 0.4
BALL_MAX_Y_VELOCITY = 0.2


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.score_font = pygame.font.SysFont("comicsans", 40)
        self.left_score = 0
        self.right_score = 0
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.left_paddel = Paddel(self.screen, 10, 40)
        self.right_paddel = Paddel(self.screen, 680, 40)
        self.ball = Ball(self.screen, 30, 300, [self.left_paddel, self.right_paddel])

        self.time_factor = 0

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.left_paddel.set_direction(-1)
        elif keys[pygame.K_s]:
            self.left_paddel.set_direction(1)
        else:
            self.left_paddel.set_direction(0)

        if keys[pygame.K_UP]:
            self.right_paddel.set_direction(-1)
        elif keys[pygame.K_DOWN]:
            self.right_paddel.set_direction(1)
        else:
            self.right_paddel.set_direction(0)
        self.left_paddel.update(self.time_factor)
        self.right_paddel.update(self.time_factor)

        self.ball.update(self.time_factor)
        if self.ball.x < 0:
            self.right_score += 1
            self.ball.set_ball(50, HEIGHT / 2, 1)
        if self.ball.x > WIDTH:
            self.left_score += 1
            self.ball.set_ball(WIDTH - 50, HEIGHT / 2, -1)
        self.time_factor = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_score()
        self.draw_field()
        self.left_paddel.draw()
        self.right_paddel.draw()
        self.ball.draw()
        pygame.display.update()

    def draw_score(self):
        left_score_text = self.score_font.render(f"{self.left_score}", 1, PADDEL_COLOR)
        right_score_text = self.score_font.render(
            f"{self.right_score}", 1, PADDEL_COLOR
        )
        self.screen.blit(left_score_text, (WIDTH * 1 / 4, 5))
        self.screen.blit(right_score_text, (WIDTH * 3 / 4, 5))

    def draw_field(self):
        draw = True
        x = WIDTH / 2 - LINEWIDTH / 2
        length = int(HEIGHT / 21)
        for y in range(0, HEIGHT, length):
            if draw:
                pygame.draw.line(
                    self.screen, PADDEL_COLOR, (x, y), (x, y + length), LINEWIDTH
                )
                draw = False
            else:
                draw = True

    def close(self):
        pygame.quit()
        sys.exit()


class Paddel:
    def __init__(self, screen, x, y) -> None:
        self.x = x
        self.y = y
        self.screen = screen
        self.velocity = 0

    def draw(self):
        pygame.draw.rect(
            self.screen,
            PADDEL_COLOR,
            (self.x, self.y, PADDEL_WIDTH, PADDEL_HEIGHT),
        )

    def update(self, time_factor):
        self.y += time_factor * self.velocity
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - PADDEL_HEIGHT:
            self.y = HEIGHT - PADDEL_HEIGHT

    def set_direction(self, direction):
        if direction > 1 or direction < -1:
            return
        self.velocity = PADDEL_VELOCITY * direction


class Ball:
    def __init__(self, screen, x, y, paddels) -> None:
        self.screen = screen
        self.paddels = paddels
        self.set_ball(x, y)
        self.y_vel = 0

    def set_ball(self, x, y, direction=1):
        self.x = x
        self.y = y
        self.x_vel = BALL_VELOCITY * direction

    def draw(self):
        pygame.draw.circle(self.screen, BALL_COLOR, (self.x, self.y), BALL_REDIOUS)

    def update(self, time_factor):
        self.y += time_factor * self.y_vel
        self.x += time_factor * self.x_vel
        if self.y - BALL_REDIOUS < 0:
            self.y_vel = self.y_vel * -1

        if self.y + BALL_REDIOUS > HEIGHT:
            self.y_vel = self.y_vel * -1

        for p in self.paddels:
            if self.is_colliding(p):
                pos = self.y - p.y
                disp = pos - PADDEL_HEIGHT / 2
                self.y_vel = disp * BALL_MAX_Y_VELOCITY / PADDEL_HEIGHT
                self.x_vel = -self.x_vel

    def is_colliding(self, paddel):
        return (
            self.y >= paddel.y
            and self.y <= paddel.y + PADDEL_HEIGHT
            and self.x >= paddel.x
            and self.x <= paddel.x + PADDEL_WIDTH
        )


if __name__ == "__main__":
    game = Game()
    game.run()
