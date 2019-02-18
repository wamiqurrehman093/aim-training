import arcade
import random

WIDTH = 480
HEIGHT = 640
TITLE = 'SNAKE GAME'

BLACK = arcade.color.BLACK
WHITE = arcade.color.WHITE
RED = arcade.color.RED

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()

    def setup(self):
        arcade.set_background_color(BLACK)

def main():
    window = Window(WIDTH, HEIGHT, TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
