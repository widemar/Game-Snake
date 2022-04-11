from turtle import Turtle

TUPLA_FONTE = ("monospace", 20, "bold")
MOVER_TOPO = (0, 270)
COR_TEXTO = "white"
ALINHAMENTO_TEXTO = "center"


class Placar(Turtle):
	def __init__(self):
		super().__init__()
		self.pontuacao = 0
		self.color(COR_TEXTO)
		self.penup()
		self.goto(MOVER_TOPO)
		self.atualizar_placar()
		self.aumentar_placar()
		self.hideturtle()

	def atualizar_placar(self):
		self.write(arg=f"Placar: {self.pontuacao}", move=False, align=ALINHAMENTO_TEXTO, font=TUPLA_FONTE)

	def aumentar_placar(self):
		self.clear()
		self.atualizar_placar()
		self.pontuacao += 1

	def fim_de_jogo(self):
		self.home()
		self.write(arg=f"FIM DE JOGO", move=False, align=ALINHAMENTO_TEXTO, font=TUPLA_FONTE)
