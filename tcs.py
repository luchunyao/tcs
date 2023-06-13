Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import random
import tkinter as tk


class Snake:
    def __init__(self, head, snake_list):
        self.snake = snake_list
        self.head = head
        self.direction = ""

    def move(self, head):
        if self.direction == "up":
            x, y = self.snake[0]
            if y == 0:
                return False
            self.snake.insert(0, (x, y - 10))
        elif self.direction == "down":
            x, y = self.snake[0]
            if y == 490:
                return False
            self.snake.insert(0, (x, y + 10))
        elif self.direction == "left":
            x, y = self.snake[0]
            if x == 0:
                return False
            self.snake.insert(0, (x - 10, y))
        elif self.direction == "right":
            x, y = self.snake[0]
            if x == 490:
                return False
            self.snake.insert(0, (x + 10, y))
        if head not in self.snake:
            self.snake.pop()
            return True
        else:
            return False

    def hit_self(self):
        if len(self.snake) != len(set(self.snake)):
            return True
        else:
            return False

    def hit_wall(self):
        if self.snake[0][0] <= 0 or self.snake[0][0] > 490 \
                or self.snake[0][1] <= 0 or self.snake[0][1] > 490:
            return True
        else:
            return False


def create_new_food(head, snake, food_list):
    if head in food_list:
        food_list.remove(head)
...         food = random.choice([i for i in range(5, 500, 10)
...                               if (i, i) not in snake])
...         food_list.append((food, food))
...     return food_list
... 
... 
... def change_direction(event, snake):
...     if event.keysym == "Up":
...         if snake.direction != "down":
...             snake.direction = "up"
...     elif event.keysym == "Down":
...         if snake.direction != "up":
...             snake.direction = "down"
...     elif event.keysym == "Left":
...         if snake.direction != "right":
...             snake.direction = "left"
...     elif event.keysym == "Right":
...         if snake.direction != "left":
...             snake.direction = "right"
... 
... 
... def game_over():
...     canvas.delete(tk.ALL)
...     canvas.create_text(canvas.winfo_width() / 2,
...                        canvas.winfo_height() / 2,
...                        text="Game Over",
...                        fill="white",
...                        font=("TkDefaultFont", 36, "bold"))
... 
... 
... def update_canvas():
...     global food_list
...     global score
...     global time_step
... 
...     if snake.move(snake.head):
...         canvas.delete("snake")
...         for x, y in snake.snake:
...             canvas.create_rectangle(x, y, x + 10, y + 10,
