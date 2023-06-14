import pygame

class GameController:
    def __init__(self, snake, food, view):
        # Initialize game controller with game objects
        self.snake = snake
        self.food = food
        self.view = view
        self.score = 0

    def handle_events(self):
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != 'down':
                    self.snake.direction = 'up'
                elif event.key == pygame.K_DOWN and self.snake.direction != 'up':
                    self.snake.direction = 'down'
                elif event.key == pygame.K_LEFT and self.snake.direction != 'right':
                    self.snake.direction = 'left'
                elif event.key == pygame.K_RIGHT and self.snake.direction != 'left':
                    self.snake.direction = 'right'

    def update(self):
        # Update game objects
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.generate()
            self.score += 10
        if self.snake.check_collision(self.view.width//20, self.view.height//20):
            pygame.quit()
            quit()

    def draw(self):
        # Draw game objects on game window
        self.view.clear()
        self.view.draw_snake(self.snake)
        self.view.draw_food(self.food)
        self.view.draw_score(self.score)
        self.view.update()

    def run_game(self):
        # Main game loop
        clock = pygame.time.Clock()
        while True:
            clock.tick(10)
            self.handle_events()
            self.update()
            self.draw()