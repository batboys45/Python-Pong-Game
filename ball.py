from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.random_angle = random.randint(45, 135)
        self.setheading(self.random_angle)
        self.move_speed = 0.1
        self.min_angle = 30
        self.max_angle = 150

    def move(self):
        """
        Topu mevcut yönüne göre hareket ettir.
        """
        self.forward(10)

    def bounce_y(self):
        """
        Y ekseninde yansıma (üst/alt kenar). Açıyı yansımada minimum ve maksimum sınırlar içinde ayarlar.
        """
        current_angle = self.heading()
        new_angle = 360 - current_angle


        if new_angle < self.min_angle or new_angle > (360 - self.min_angle):
            new_angle = self.min_angle if new_angle < 180 else (360 - self.min_angle)

        self.setheading(new_angle)

    def bounce_x(self):
        """
        X ekseninde yansıma (paddle'lara çarptığında). Açıyı yansımada minimum ve maksimum sınırlar içinde ayarlar.
        """
        current_angle = self.heading()
        new_angle = 180 - current_angle


        if new_angle < self.min_angle or new_angle > (180 - self.min_angle):
            new_angle = self.min_angle if new_angle < 90 else (180 - self.min_angle)

        self.setheading(new_angle)


        self.move_speed *= 0.9

    def reset_position(self):
        """
        Topun başlangıç konumuna dönmesi. Hız sıfırlanır ve yeni bir rastgele açı hesaplanır.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.random_angle = random.randint(45, 135)
        self.setheading(self.random_angle)