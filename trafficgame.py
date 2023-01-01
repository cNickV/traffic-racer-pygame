import pygame

from pygame.locals import *

# Ajustar la resolución de la pantalla para que no se dibuje fuera de los límites
size = width, height = (1200, 800)
road_w = int(width / 1.6)
roadmark_w = int(width/80)

pygame.init()
running = True
screen = pygame.display.set_mode(size)

pygame.display.set_caption("cNick's car game")

# Rellenar el fondo de la pantalla con un color verde "limón"
screen.fill((82, 190, 128))


# Actualizar la pantalla para mostrar los cambios
pygame.display.update()

# cargar vehículos
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = width/2 + road_w/4, height*0.8

# cargar enemigos

otherCar = pygame.image.load("otherCar.png")
otherCar_loc = otherCar.get_rect()
otherCar_loc.center = width/2 - road_w/4, height*0.2


# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

    # Dibujar las lineas de las carreteras

    # Dibujar el centro de la pantalla con un color negro suave
    pygame.draw.rect(screen, (50, 50, 50),
                     (width/2-road_w/2, 0, road_w, height))

    # lineas amarillas
    pygame.draw.rect(screen, (241, 196, 15), (width/2 -
                                              roadmark_w/2, 0, roadmark_w, height))

    # linea blanca izquierda
    pygame.draw.rect(screen, (242, 243, 244), (width/2 -
                                               road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # linea blanca derecha
    pygame.draw.rect(screen, (242, 243, 244), (width/2 +
                                               road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    screen.blit(car, car_loc)
    screen.blit(otherCar, otherCar_loc)
    pygame.display.update()


pygame.quit()
