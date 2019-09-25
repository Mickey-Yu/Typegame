import sys
import time
import pygame
from pygame.locals import *

class Typegame:

    def print_text(self,font, x, y, text, color=(0, 0, 0)):
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x, y))

    def draw_background(self,r,g,b):
        screen.fill((r,g,b))
        self.print_text(font1, 0, 0, "Please complete in 1 min:")
        y=30
        for line in text:
            self.print_text(font1, 0,y, line)
            y+=30

    def handleWord(self,data):
        data = data.replace("\n", '')
        text = data.split("\\n")
        word = ''
        for line in text:
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("!", "")
            word = word + line
            word = word + " "
        word = word + "/"
        word = word.split(" ")
        return [word, text]

f = open("text.txt", encoding="utf-8")
data = f.readlines()
f.close()

typegame=Typegame()
database=typegame.handleWord(data[0])
word=database[0]
text=database[1]

pygame.init()
screen = pygame.display.set_mode((640, 600))
pygame.display.set_caption('打字游戏')
font1 = pygame.font.SysFont('arial',16)
font2 =pygame.font.SysFont('arial',60)
BLACK = (0, 0, 0)

pre_event_key=0
key_flag = False
seconds = 61
score = 0
typecount=0
speed = 0
clock_start = 0
time_start=0
game_over = True
i=0
current=0
input=''
iptstr='  '

while True:
    typegame.draw_background(180, 100, 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
            if event.key==K_ESCAPE:
                sys.exit()
            elif event.type == KEYUP:
                key_flag = False
            elif event.key == K_RETURN:
                if game_over:
                    game_over = False
                    clock_start = time.time()
                    score = 0
                    speed = 0
                    typecount = 0
                    clock = clock_start
            elif not game_over:
                current = time.time() - clock
                if seconds < current:
                    game_over = True
                    break
                else:
                    if event.key==K_SPACE:
                        i+=1
                        input=''
                        iptstr+=' '
                    else:
                        if  event.key == K_LSHIFT or event.key == K_RSHIFT:
                            pre_event_key = K_LSHIFT
                            continue
                        else:
                            if pre_event_key == K_LSHIFT:
                                pre_event_key = None
                                input=input+chr(event.key-32)
                                iptstr+=chr(event.key-32)
                                clock_start = time.time()
                                typecount += 1
                                speed = 60 * typecount / (clock_start - clock)
                            else:
                                input=input+chr(event.key)
                                iptstr +=chr(event.key)
                                clock_start = time.time()
                                typecount += 1
                                speed = 60 * typecount /(clock_start - clock)
                        if input ==word[i]:
                            score+=1
                        if event.key==K_SLASH :
                            database = typegame.handleWord(data[1])
                            word = database[0]
                            text = database[1]
                            iptstr='  '
                            i=0
                            continue

    if key_flag:
        typegame.print_text(font1, 500, 0, "<key>")

    if not game_over:
        current = time.time() - clock
        if seconds < current:
            game_over = True

        if speed<=30:
            typegame.draw_background(180,150,0)
        else:
            if speed<=35:
                typegame.draw_background(180,140,0)
            else:
                if speed<=40:
                    typegame.draw_background(180,160,0)
                else:
                    if speed<=45:
                        typegame.draw_background(180,180,0)
                    else:
                        if speed<=50:
                            typegame.draw_background(180, 200, 0)
                        else:
                            if speed<=55:
                                typegame.draw_background(180,220,0)
                            else:
                                if speed<=60:
                                    typegame.draw_background(180,240,0)
                                else:
                                    typegame.draw_background(180,255,0)

    typegame.print_text(font1, 0, 130, "You score:%s : " % score)
    if game_over:
        typegame.print_text(font1, 0, 170, "Press Enter to start : ")
    if not game_over:
        typegame.print_text(font1, 0, 150, "Time: " + str(int(seconds-current)))
        typegame.print_text(font1, 0, 320, 'Your input:', BLACK)
        typegame.print_text(font1, 0, 340, iptstr, BLACK)
    typegame.print_text(font1, 0, 200, "Speed: " + str(int(speed)) + " letters/min")
    typegame.print_text(font2, 0, 250, word[i], BLACK)

    pygame.display.update()
