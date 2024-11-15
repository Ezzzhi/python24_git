import arcade

class Game(arcade.Window):
    def on_drow(self):
        self.clear((255, 255, 255))


if __name__ == '__main__':
    window = Game()
    arcade.run()