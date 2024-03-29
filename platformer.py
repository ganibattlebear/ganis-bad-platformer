"""
Platformer Game
"""
import arcade
​
# Constants
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Definitely Minecraft"
​
​
class MyGame(arcade.Window):
    """
    Main application class.
    """
​
    def __init__(self):
​
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
​
        arcade.set_background_color(arcade.csscolor.DARK_ORANGE)
​
    def setup_lvl_1(self):
        """ Set up the game here. Call this function to restart the game. """
        pass
​
    def on_draw(self):
        """ Render the screen. """
​
        arcade.start_render()
        # Code to draw the screen goes here
    self.player_sprite = arcade.Sprite("Documents/platform_tutorial/images/player_1/player_stand.png", .9)
    self.player_sprite.position()
​
def main():
    """ Main method """
    window = MyGame()
    window.setup_lvl_1()
    arcade.run()
​
​
if __name__ == "__main__":
    main()