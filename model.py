import random

class Snake:
    def __init__(self):
        # Initialize snake with starting position and length
        self.body = [(10, 10), (10, 11), (10, 12)]
        self.direction = 'up'

    def move(self):
        # Move snake in current direction
        head = self.body[0]
        if self.direction == 'up':
            new_head = (head[0]-1, head[1])
        elif self.direction == 'down':
            new_head = (head[0]+1, head[1])
        elif self.direction == 'left':
            new_head = (head[0], head[1]-1)
        elif self.direction == 'right':
            new_head = (head[0], head[1]+1)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        # Add new segment to snake body
        tail = self.body[-1]
        self.body.append(tail)

    def check_collision(self, width, height):
        # Check if snake collides with walls or itself
        head = self.body[0]
        if head[0] < 0 or head[0] >= height or head[1] < 0 or head[1] >= width:
            return True
        if head in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        # Initialize food with random position
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def generate(self):
        # Generate new random position for food
        self.position = (random.randint(0, 19), random.randint(0, 19))