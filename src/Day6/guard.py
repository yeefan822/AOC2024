from enum import Enum

class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
class Guard:
    def __init__(self, x, y, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def attempt_move(self):
        next_x, next_y = self.x, self.y

        if self.direction == Direction.UP:
            next_y -= 1
        elif self.direction == Direction.DOWN:
            next_y += 1
        elif self.direction == Direction.LEFT:
            next_x -= 1
        elif self.direction == Direction.RIGHT:
            next_x += 1
            
        return next_x, next_y
        
    def move(self, next_x, next_y):
        self.x, self.y = next_x, next_y
   
                
    def turn(self):
        match self.direction:
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.DOWN:
                self.direction = Direction.LEFT
            case Direction.LEFT:
                self.direction = Direction.UP
            case Direction.RIGHT:
                self.direction = Direction.DOWN
                
    
