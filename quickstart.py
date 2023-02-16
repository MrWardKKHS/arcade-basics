import arcade
"""Blah blah blah """
class MyGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(800, 800, "My awesome game")
        arcade.set_background_color((50, 50, 200))

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(300, 300, 30, arcade.color.AUROMETALSAURUS)

game = MyGame()
arcade.run()