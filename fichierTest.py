import sys, time, pygame

# Intialize the pygame
pygame.init()

# create the screen
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('image/background.jpg')

# Caption and Icon
pygame.display.set_caption("Icone")
icon = pygame.image.load('image/3232.png').convert()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60


# Player
playerImg1 = pygame.image.load('image/Personnage2.png')
playerImg2 = pygame.image.load('image/Personnage2Retour.png')
playerImg3 = pygame.image.load('image/Personnage2Dos.png')
playerImg4 = pygame.image.load('image/Personnage2RetourDos.png')
playerImg=playerImg1
longueurImage,hauteurImage=playerImg.get_size()

playerX = 0
playerY = 600 - hauteurImage 
playerX_change = 0


ficAudioAvant = pygame.mixer.Sound('audio/enAvant.wav')
ficAudioArriere = pygame.mixer.Sound('audio/enArriere.wav')
ficAudioHaut = pygame.mixer.Sound('audio/enHaut.wav')
ficAudioBas = pygame.mixer.Sound('audio/enBas.wav')
ficAudioMur = pygame.mixer.Sound('audio/unMur.wav')
def player(x, y):
    screen.blit(playerImg, (x, y)) #remet l'image du joueur en cette position donnee

def stopSounds():
    ficAudioArriere.stop()
    ficAudioAvant.stop()
    ficAudioHaut.stop()
    ficAudioBas.stop()
    ficAudioMur.stop()

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
        if(playerImg==playerImg2):
            playerImg=playerImg4
        else:
            playerImg=playerImg3
        stopSounds()
        ficAudioHaut.play()
        yDeplacement = -4
    if keystate[pygame.K_DOWN]:
        if(playerImg==playerImg4 or playerImg==playerImg2):
            playerImg=playerImg2
        else:
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
        #stopSounds()
        #ficAudioMur.play()
    elif playerX >= (800-longueurImage):
        playerX = (800-longueurImage)
        #stopSounds()
        #ficAudioMur.play()

    if playerY <= 0:
        playerY = 0
        #stopSounds()
        #ficAudioMur.play()
    elif playerY >= (600-hauteurImage):
        playerY = (600-hauteurImage)
        #stopSounds()
        #ficAudioMur.play()

    player(playerX,playerY)
    pygame.display.update()