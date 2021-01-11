import sys, time, pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('image/background.jpg')

# Caption and Icon
pygame.display.set_caption("Icone")
icon = pygame.image.load('image/icone.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60


# Player
playerImg1 = pygame.image.load('image/Personnage.jpg')
playerImg2 = pygame.image.load('image/PersonnageRetour.jpg')
playerImg=playerImg1
playerX = 370
playerY = 380
playerX_change = 0

longueurImage,hauteurImage=playerImg.get_size()


def player(x, y):
    screen.blit(playerImg, (x, y))

def updatePlayer():
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        return(-4)
    if keystate[pygame.K_RIGHT]:
        return(4)
    else:
        return(0)

# Game Loop
running = True
while running:

    clock.tick(FPS)	

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    #Background Image
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	
        playerX_change = 0
	
    	# si touche enfoncée

        playerX_change = updatePlayer()

    #vérifier les limites de l'espace de jeu
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= (800-longueurImage):
        playerX = (800-longueurImage)

    player(playerX,playerY)
    pygame.display.update()