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
playerImg3 = pygame.image.load('image/PersonnageDos.jpg')
playerImg=playerImg1
playerX = 370
playerY = 380
playerX_change = 0

longueurImage,hauteurImage=playerImg.get_size()

ficAudioAvant = pygame.mixer.Sound('audio/enAvant.wav')
ficAudioArriere = pygame.mixer.Sound('audio/enArriere.wav')
ficAudioHaut = pygame.mixer.Sound('audio/enHaut.wav')
ficAudioBas = pygame.mixer.Sound('audio/enBas.wav')
def player(x, y):
    screen.blit(playerImg, (x, y))

def stopSounds():
    ficAudioArriere.stop()
    ficAudioAvant.stop()
    ficAudioHaut.stop()
    ficAudioBas.stop()

def updatePlayer():
    keystate = pygame.key.get_pressed()
    xDeplacement = 0
    yDeplacement = 0
    playerImg=playerImg1
    if keystate[pygame.K_LEFT]:
        playerImg=playerImg2
        stopSounds()
        ficAudioArriere.play()
        xDeplacement = -4
    if keystate[pygame.K_RIGHT]:
        playerImg=playerImg1
        stopSounds()
        ficAudioAvant.play()
        xDeplacement = 4
    if keystate[pygame.K_UP]:
        playerImg=playerImg3
        stopSounds()
        ficAudioHaut.play()
        yDeplacement = -4
    if keystate[pygame.K_DOWN]:
        playerImg=playerImg1
        stopSounds()
        ficAudioBas.play()
        yDeplacement = 4
    return(playerImg,xDeplacement,yDeplacement) 

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

	
    	# si touche enfoncée

        playerImg,playerX_change,playerY_change = updatePlayer()

    #vérifier les limites de l'espace de jeu
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= (800-longueurImage):
        playerX = (800-longueurImage)

    if playerY <= 0:
        playerY = 0
    elif playerY >= (600-hauteurImage):
        playerY = (600-hauteurImage)

    player(playerX,playerY)
    pygame.display.update()