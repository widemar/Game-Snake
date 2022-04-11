import random
from turtle import Turtle


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_wid=0.4, stretch_len=0.4)
		self.color("red")
		self.speed("fastest")
		self.atualizar_local_comida()

	def atualizar_local_comida(self):
		numero_aleatorio_x = random.randint(-280, 280)
		numero_aleatorio_y = random.randint(-280, 280)
		self.goto(numero_aleatorio_x, numero_aleatorio_y)
