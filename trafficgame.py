import pygame
from pygame.locals import *
import random

# Ajustar la resolución de la pantalla para que no se dibuje fuera de los límites
size = width, height = (1200, 800)
road_w = int(width / 1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
level = 1
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)

pygame.display.set_caption("cNick's car game")


# Actualizar la pantalla para mostrar los cambios
pygame.display.update()

# cargar vehículos
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# cargar enemigos

otherCar = pygame.image.load("otherCar.png")
otherCar_loc = otherCar.get_rect()
otherCar_loc.center = left_lane, height*0.2

start_time = pygame.time.get_ticks()

# game loop
while running:
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    if elapsed_time >= 30:
        level += 1
        speed += 3

    # animar vehículo enemigo
    otherCar_loc[1] += speed
    if otherCar_loc[1] > height:
        if random.randint(0, 1) == 0:
            otherCar_loc.center = right_lane, -200
        else:
            otherCar_loc.center = left_lane, -200

    # end game
    if car_loc[0] == otherCar_loc[0] and otherCar_loc[1] > car_loc[1] - 250:
        print("GAME OVER!! PAPÚ, PERDISTE NOOB")
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

                # Rellenar el fondo de la pantalla con un color verde "limón"
    screen.fill((82, 190, 128))

    # Dibujar las lineas de las carreteras

    # Dibujar el centro de la pantalla con un color negro suave
    pygame.draw.rect(screen, (50, 50, 50),
                     (width/2-road_w/2, 0, road_w, height))

    # lineas amarillas
    pygame.draw.rect(screen, (241, 196, 15),
                     (width/2 - roadmark_w/2, 0, roadmark_w, height))

    # linea blanca izquierda
    pygame.draw.rect(screen, (242, 243, 244),
                     (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # linea blanca derecha
    pygame.draw.rect(screen, (242, 243, 244),
                     (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    screen.blit(car, car_loc)
    screen.blit(otherCar, otherCar_loc)
    pygame.display.update()


pygame.quit()
