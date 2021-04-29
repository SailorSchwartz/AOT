import pygame, math, sys, random, os, time

########

displayWidth = 320
displayHeight = 288
clock = pygame.time.Clock()
fps = 60

########

white = 208,208,88
light = 160,168,64
dark = 112,128,40
black = 64,80,16


########

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.z = 1
        self.collide = 0
        self.speed = 4

    def collideDetect(self):
        if pygame.sprite.spritecollideany(player, collideList):
            self.collide = 1
        else:
            self.collide = 0
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
        if key[pygame.K_q]:
            self.z += 1
            print(self.z)
        if key[pygame.K_e] and self.z > 0:
            self.z += -1
            print(self.z)
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def draw(self):
        gameDisplay.blit(self.image, [self.x, self.y])
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def moveAndCollide(self):
        pos = (self.x, self.y)
        self.move()
        self.collideDetect()
        if player.collide and self.z < 50:
            self.x, self.y = pos
            self.updateRect()
            self.collide = 0

class House(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.top)





class Quad(pygame.sprite.Sprite):
    def __init__(self,color,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


########

spriteList = pygame.sprite.Group()
collideList = pygame.sprite.Group()

########

screenQuad = Quad(white, 16, 16, 288, 256)
spriteList.add(screenQuad)


whiteTest = Quad(white, 16, 16, 16, 16)
spriteList.add(whiteTest)

lightTest = Quad(light, 32, 16, 16, 16)
spriteList.add(lightTest)

darkTest = Quad(dark, 48, 16, 16, 16)
spriteList.add(darkTest)

blackTest = Quad(black, 64, 16, 16, 16)
spriteList.add(blackTest)

houseOne = House(80,80,"assets/house.png")
spriteList.add(houseOne)
collideList.add(houseOne)
houseTwo = House(80,144,"assets/house.png")
spriteList.add(houseTwo)
collideList.add(houseTwo)

player = Player(160,160,"assets/player.png")
spriteList.add(player)

#######





#######

pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('AOT')

def main():
    run = True
    while run:
        gameDisplay.fill(black)

        spriteList.draw(gameDisplay)

        player.moveAndCollide()








        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pass


        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            pygame.draw.line(gameDisplay, black, (player.x + 16 ,player.y + 16 ),(houseOne.rect.x + 16 ,houseOne.rect.y + 16 ),2)
            pygame.draw.line(gameDisplay, black, (player.x + 16 ,player.y + 16 ),(houseTwo.rect.x + 16 ,houseTwo.rect.y + 16 ),2)
            player.z += 2
        if player.z > 0:
            player.z -= 1
        print(player.z)
        pygame.display.update()
        clock.tick(fps)
        
main()
