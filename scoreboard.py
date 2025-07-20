from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()  # Çizgiyi gizle
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Skoru ekranda günceller.
        """
        self.clear()
        self.goto(-150, 250)
        self.write(f"Player 1: {self.score_1}", align=ALIGNMENT, font=FONT)
        self.goto(150, 250)
        self.write(f"Player 2: {self.score_2}", align=ALIGNMENT, font=FONT)

    def increase_score_1(self):
        """
        Player 1 skorunu artırır ve ekrana yazar.
        """
        self.score_1 += 1
        self.update_scoreboard()

    def increase_score_2(self):
        """
        Player 2 skorunu artırır ve ekrana yazar.
        """
        self.score_2 += 1
        self.update_scoreboard()

    def game_over(self, winner):
        """
        Oyunun sonlandığını ve kazananı ekranda gösterir.
        """
        self.goto(0, 0)
        self.write(f"GAME OVER! {winner} Wins!", align=ALIGNMENT, font=FONT)