from turtle import Screen
import time
from snake import Snake
from food import Food
from placar import Placar

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo Snake")
tela.tracer(0)

snake = Snake()
food = Food()
placar = Placar()

tela.listen()

tela.onkey(snake.mover_para_cima, "w")
tela.onkey(snake.mover_para_esquerda, "a")
tela.onkey(snake.mover_para_baixo, "s")
tela.onkey(snake.mover_para_direita, "d")

jogo_ativo = True
while jogo_ativo:
	tela.update()
	time.sleep(0.1)

	snake.move()
	# Detecta a colisão com a comida
	if snake.cabeca.distance(food) < 15:
		food.atualizar_local_comida()
		snake.extender_cobra()
		placar.aumentar_placar()

	# Detecta a colisão com a parede
	if snake.cabeca.xcor() >= 300 or snake.cabeca.xcor() <= -300 or \
			snake.cabeca.ycor() >= 300 or snake.cabeca.ycor() <= -300:
		placar.fim_de_jogo()
		jogo_ativo = False

	# Detecta a colisão com a propria cobra
	for quadrado in snake.lista_de_quadrados[1:]:
		if snake.cabeca.distance(quadrado) < 10:
			placar.fim_de_jogo()
			jogo_ativo = False
tela.exitonclick()
