import pygame
import time
import random

pygame.init() #Inicializa todos los modulos importados de pygame

green = (0,255,0)
yellow = (255,255,102)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width,dis_height)) #Inicializa pantalla de 800x600

pygame.display.update() #Actualizar display
pygame.display.set_caption('Snake game') #Titulo del display

snake_block = 20
snake_speed = 15 #FPS

clock = pygame.time.Clock() #Objeto que trackea el tiempo

font_style = pygame.font.SysFont(None, 25) #Crear objeto de fuente de las fuentes del sistema
score_font = pygame.font.SysFont(None, 25)

def score(score):
	value = score_font.render("Score" + str(score), True, green)
	dis.blit(value, [0,0])

def snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, black, [x[0],x[1],snake_block,snake_block])

def message(msg,color):
	mesg = font_style.render(msg,True,color) #Renderizar mensaje en una superficie
	dis.blit(mesg, [dis_width/2 - mesg.get_width()/2, dis_height/2 - mesg.get_height()/2]) #Anadir mesg a display, obtener altura y ancho de mensaje

def gameLoop():
	game_over = False
	game_close = False

	x1 = dis_width / 2 - snake_block / 2
	y1 = dis_height / 2 - snake_block / 2
	x1_change = 0
	y1_change = 0

	foodx = round(random.randrange(0 + snake_block, dis_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0 + snake_block, dis_height - snake_block) / 10.0) * 10.0

	snake_list = []
	length_snake = 1

	while not game_over:
		while game_close == True:
			dis.fill(white)
			message("Perdiste! Presiona S-Salir o N-Juego nuevo", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						game_over = True
						game_close = False
					if event.key == pygame.K_n:
						gameLoop()

		for event in pygame.event.get(): #Iterar en todos los eventos que ocurran
			if event.type == pygame.QUIT: #.QUIT evento del boton quit, .type devuelve el tipo de evento
				game_over = True
			if event.type == pygame.KEYDOWN: #Si el evento es de tipo presionar tecla
				if event.key == pygame.K_LEFT: #Si el id del evento es flecha izquierda
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -snake_block
				elif event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = snake_block

		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #Si choca los bordes pierde
			game_close = True

		x1 += x1_change
		y1 += y1_change

		dis.fill(white) #Pintar de color blanco el display

		pygame.draw.rect(dis, green, [foodx,foody,snake_block,snake_block]) #Dibujar comida
		
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)

		if len(snake_list) > length_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				game_close = True

		snake(snake_block, snake_list)
		score(length_snake - 1)

		pygame.display.update()

		if abs(x1 - foodx) < 20 and abs(y1 - foody) < 20:
			foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
			length_snake += 1	

		clock.tick(snake_speed) #Delimitar FPS del juego

	pygame.quit() #Cierra todo los modulos inicializados
	quit()

gameLoop()