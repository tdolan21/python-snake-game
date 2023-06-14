import pygame

class GameView:
    def __init__(self):
        # Initialize game window
        pygame.init()
        self.width = 400
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.font = pygame.font.SysFont('Arial', 20)

    def draw_snake(self, snake):
        # Draw snake on game window
        for segment in snake.body:
            rect = pygame.Rect(segment[1]*20, segment[0]*20, 20, 20)
            pygame.draw.rect(self.screen, (0, 255, 0), rect)

    def draw_food(self, food):
        # Draw food on game window
        rect = pygame.Rect(food.position[1]*20, food.position[0]*20, 20, 20)
        pygame.draw.rect(self.screen, (255, 0, 0), rect)

    def draw_score(self, score):
        # Draw score on game window
        text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def update(self):
        # Update game window
        pygame.display.update()

    def clear(self):
        # Clear game window
        self.screen.fill((0, 0, 0))