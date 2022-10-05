import pygame

from text import Text
from input import Input
from buttons import Button

pygame.init()

width, height = 1280, 720
fps = 60

win = pygame.display.set_mode((width, height), pygame.SRCALPHA)
pygame.display.set_caption('widgets test')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)

bt = Button(win, x = 100, y = 100, width = 200, fontSize = 60, borderRadius = 25, text = 'Click!')
input = Input(win, x = 100, y = 400, borderRadius = 15, maxChars = 256, noText = 'Enter your text...', cursorColor = (255, 0, 0))
tx = Text(win, x = 450, y = 100, cursorColor = (255, 0, 0), fontSize = 50, color = (0, 150, 255, 128))

while 1:
    clock.tick(fps)
    win.fill((60, 60, 60))
    tx.Scroll()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            input.Press(event.unicode)
            tx.Press(event.unicode)
    
    bt.update()
    input.update()
    tx.update()

    fpsINFO = font.render(str(int(clock.get_fps())), 1, (255, 255, 255))
    win.blit(fpsINFO, (10, 10))
    
    pygame.display.update()