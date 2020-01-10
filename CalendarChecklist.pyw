import pygame, sys, time, os
from calendar import monthrange
from pygame.locals import *
from assets.terminate import *
from assets.waitForPlayerToPressKey import *
from assets.DrawTextFileFont import *

Version = "1.0"
WINDOWSIZE = (672, 672)
BACKGROUNDCOLOUR = (44, 44, 44)
TEXTCOLOUR = (255, 255, 255)
LEFT = 1
RIGHT = 3
month=1
year=2020
file=""

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(Version)
windowSurface = pygame.display.set_mode(WINDOWSIZE)
icon = pygame.image.load("assets\\iconImage.png")
pygame.display.set_icon(icon)
font = "assets//moon_get-Heavy.ttf"

main_list = pygame.sprite.Group()
button_list = pygame.sprite.Group()
select_list = pygame.sprite.Group()

Images=[]
for object in sorted(os.listdir("assets\\images"), key=len):
    Images.append(pygame.transform.scale(pygame.image.load("assets\\images\\" + object), (96, 96)))

selectImage = Images[2]

class window(pygame.sprite.Sprite):
    def __init__(self, imageType, x, y, objectName):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageType
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.name = objectName
    def counterLoop(self, top):
        if self.counter > top:
            self.counter = 0
        elif self.counter < 0:
            self.counter = top
    def rightbutton(self):
        if pygame.sprite.spritecollideany(self, select_list):
            self.counter -= 1
            self.counterLoop(2)
            self.image = Images[self.counter]
    def leftbutton(self):
        if pygame.sprite.spritecollideany(self, select_list):
            self.counter += 1
            self.counterLoop(2)
            self.image = Images[self.counter]
    def loadMonth(self):
        self.image = Images[self.counter]
    def activate(self):
        global month, year
        if pygame.sprite.spritecollideany(self, select_list):
            saveBox(str(year) + "_" + str(month))
            if self == g7i:
                month -= 1
            if self == o7i:
                month += 1
            if month <= 0:
                month = 12
                year -= 1
            if month >= 13:
                month = 1
                year += 1
            if os.path.isfile("assets\\months\\" + str(year) + "_" + str(month) + ".mon") == True:
                loadBox(str(year) + "_" + str(month))
            else:
                for object in main_list:
                    object.counter = 0
                    object.loadMonth
                    saveBox(str(year) + "_" + str(month))
                    loadBox(str(year) + "_" + str(month))
    def save(self):
        global file
        file.write(str(self.name) + " " + str(self.counter) + " \n")

class select(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(selectImage, (1, 1))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

def controls():
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            select_list.update(event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                for object in main_list:
                    object.leftbutton()
                for object in button_list:
                    object.activate()
            if event.button == RIGHT:
                for object in main_list:
                    object.rightbutton()
        if event.type == QUIT:
            terminate()

def numbers():
    global month, year
    monthNumber = 0
    monthX = 0
    monthY = 0
    monthNum = 1
    monthNumber = int(str(monthrange(year, month)).split()[1].replace(")", ""))
    for i in range(monthNumber):
        DrawText(str(monthNum), font, 50, TEXTCOLOUR, windowSurface, monthX + 10, monthY, 480, 672)
        monthX += 96
        if monthX >= 480 - 1:
            monthX = 0
            monthY += 96
        monthNum += 1

def mainLoop():
    global month, year
    windowSurface.fill(BACKGROUNDCOLOUR)
    controls()
    main_list.draw(windowSurface)
    button_list.draw(windowSurface)
    select_list.draw(windowSurface)
    numbers()
    DrawText("Month " + str(month), font, 50, TEXTCOLOUR, windowSurface, 480, 0, 672, 672)
    DrawText("Year " + str(year), font, 50, TEXTCOLOUR, windowSurface, 480, 192, 672, 672)
    pygame.display.update()

b1i = window(Images[0], 0, 0, "b1i")
b2i = window(Images[0], 0, 96, "b2i")
b3i = window(Images[0], 0, 192, "b3i")
b4i = window(Images[0], 0, 288, "b4i")
b5i = window(Images[0], 0, 384, "b5i")
b6i = window(Images[0], 0, 480, "b6i")

i1i = window(Images[0], 96, 0, "i1i")
i2i = window(Images[0], 96, 96, "i2i")
i3i = window(Images[0], 96, 192, "i3i")
i4i = window(Images[0], 96, 288, "i4i")
i5i = window(Images[0], 96, 384, "i5i")
i6i = window(Images[0], 96, 480, "i6i")

n1i = window(Images[0], 192, 0, "n1i")
n2i = window(Images[0], 192, 96, "n2i")
n3i = window(Images[0], 192, 192, "n3i")
n4i = window(Images[0], 192, 288, "n4i")
n5i = window(Images[0], 192, 384, "n5i")
n6i = window(Images[0], 192, 480, "n6i")

g1i = window(Images[0], 288, 0, "g1i")
g2i = window(Images[0], 288, 96, "g2i")
g3i = window(Images[0], 288, 192, "g3i")
g4i = window(Images[0], 288, 288, "g4i")
g5i = window(Images[0], 288, 384, "g5i")
g6i = window(Images[0], 288, 480, "g6i")

o1i = window(Images[0], 384, 0, "o1i")
o2i = window(Images[0], 384, 96, "o2i")
o3i = window(Images[0], 384, 192, "o3i")
o4i = window(Images[0], 384, 288, "o4i")
o5i = window(Images[0], 384, 384, "o5i")
o6i = window(Images[0], 384, 480, "o6i")

b7i = window(Images[0], 0, 576, "b7i")
g7i = window(Images[1], 288, 576, "g7i")
o7i = window(Images[1], 384, 576, "o7i")

main_list.add(b1i)
main_list.add(b2i)
main_list.add(b3i)
main_list.add(b4i)
main_list.add(b5i)
main_list.add(b6i)
main_list.add(b7i)

main_list.add(i1i)
main_list.add(i2i)
main_list.add(i3i)
main_list.add(i4i)
main_list.add(i5i)
main_list.add(i6i)

main_list.add(n1i)
main_list.add(n2i)
main_list.add(n3i)
main_list.add(n4i)
main_list.add(n5i)
main_list.add(n6i)

main_list.add(g1i)
main_list.add(g2i)
main_list.add(g3i)
main_list.add(g4i)
main_list.add(g5i)
main_list.add(g6i)

main_list.add(o1i)
main_list.add(o2i)
main_list.add(o3i)
main_list.add(o4i)
main_list.add(o5i)
main_list.add(o6i)

button_list.add(g7i)
button_list.add(o7i)

select_list.add(select())

def saveBox(filename):
    global file
    file = open("assets\\months\\" + str(filename) + ".mon","w+")
    for object in main_list:
        object.save()
    file.close()
def loadBox(filename):
    global file
    file = open("assets\\months\\" + str(filename) + ".mon","r")
    for line in file:
        for object in main_list:
            splitline = line.split(" ")
            if line[:3] == str(object.name):
                object.counter = int(line[4])
                object.loadMonth()

month=int(time.strftime("%m"))
year=int(time.strftime("%Y"))
if os.path.isfile("assets\\months\\" + str(year) + "_" + str(month) + ".mon") == True:
    loadBox(str(year) + "_" + str(month))
else:
    for object in main_list:
        object.counter = 0
        object.loadMonth
        saveBox(str(year) + "_" + str(month))
        loadBox(str(year) + "_" + str(month))
while True:
    mainLoop()
