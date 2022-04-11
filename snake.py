from turtle import Turtle

POSICAO_INICIAL = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_A_PERCORRER = 20
CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0


class Snake:
	def __init__(self):
		self.lista_de_quadrados = []
		self.criar_cobra()
		self.cabeca = self.lista_de_quadrados[0]

	def criar_cobra(self):
		"""Cria a cobra"""
		for posicao in POSICAO_INICIAL:
			self.adicionar_partes(posicao)

	def adicionar_partes(self, posicao):
		quadrado = Turtle(shape="square")
		quadrado.color("white")
		quadrado.penup()
		quadrado.goto(posicao)
		self.lista_de_quadrados.append(quadrado)

	def extender_cobra(self):
		self.adicionar_partes(self.lista_de_quadrados[-1].position())

	def move(self):
		"""Movimenta a cobra"""
		for num_quadrado in range(len(self.lista_de_quadrados) - 1, 0, -1):
			novo_x = self.lista_de_quadrados[num_quadrado - 1].xcor()
			novo_y = self.lista_de_quadrados[num_quadrado - 1].ycor()
			self.lista_de_quadrados[num_quadrado].goto(novo_x, novo_y)
		self.cabeca.forward(DISTANCIA_A_PERCORRER)

	def mover_para_cima(self):
		if self.cabeca.heading() != BAIXO:
			self.cabeca.seth(CIMA)

	def mover_para_esquerda(self):
		if self.cabeca.heading() != DIREITA:
			self.cabeca.seth(ESQUERDA)

	def mover_para_baixo(self):
		if self.cabeca.heading() != CIMA:
			self.cabeca.seth(BAIXO)

	def mover_para_direita(self):
		if self.cabeca.heading() != ESQUERDA:
			self.cabeca.seth(DIREITA)
