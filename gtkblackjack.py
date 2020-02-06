import pygame


pygame.init()


width = 800
height = 600

screen = pygame.display.set_mode((width, height))

#s = pygame.display.get_window_size()
#print(s)
#exit()
pygame.display.set_caption("myBlackJack")
icon = pygame.image.load("img/MoiZoom.jpg")
pygame.display.set_icon(icon)



image = pygame.image.load("img/MoiZoom.jpg")
background = pygame.image.load("img/sprite/sprite.png")
image = pygame.transform.scale(image, (50, 50))

playerX = width//2
playerY = height//2
speed = 0.3
playerXChange = 0
playerYChange = 0



def player(playerX, playerY):
    screen.blit(image, (playerX, playerY))


def loop(playerX, playerY, playerXChange, playerYChange, speed):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("L")
                    playerXChange = -speed
                if event.key == pygame.K_RIGHT:
                    playerXChange = speed
                    print("R")
                if event.key == pygame.K_UP:
                    print("U")
                    playerYChange = -speed
                if event.key == pygame.K_DOWN:
                    print("D")
                    playerYChange = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    playerXChange = 0
                    playerYChange = 0

        color = (0, 0, 0)
        screen.fill(color)
        playerX += playerXChange
        playerY += playerYChange
        player(playerX, playerY)
        pygame.display.update()

if __name__ == "__main__":
    loop(playerX, playerY, playerXChange, playerYChange, speed)
