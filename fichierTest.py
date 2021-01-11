import sys, time, pygame

# Intialize the pygame
pygame.init()

#Ecran
size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

# create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('background.jpg')

# Caption and Icon
pygame.display.set_caption("Icone")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)



# Player
playerImg = pygame.image.load('Personnage.jpg')
playerX = 370
playerY = 380
playerX_change = 0




def player(x, y):
    screen.blit(playerImg, (x, y))





# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    #Background Image
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    	# si touche enfoncée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4

	#Quand touche est relachée
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    #vérifier les limites de l'espace de jeu
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX,playerY)
    pygame.display.update()