from model import Snake, Food
from view import GameView
from controller import GameController

if __name__ == '__main__':
    # Initialize game objects
    snake = Snake()
    food = Food()
    view = GameView()
    controller = GameController(snake, food, view)

    # Start game loop
    controller.run_game()