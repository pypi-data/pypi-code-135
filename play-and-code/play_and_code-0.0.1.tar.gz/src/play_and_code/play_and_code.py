import pygame
window = None 
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
BACKGROUND_COLOR = (0,0,0)
TICK_SPEED = 60

# SPACE = pygame.K_SPACE
SPACE = ' '
ESCAPE = pygame.K_ESCAPE
UP = pygame.K_UP
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

keys_pressed = set()
keys_released = set()
esc_pressed = False
run = True

def background(color):
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = clamp_color(color)

def width(w):
    global WINDOW_WIDTH
    WINDOW_WIDTH = w
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def height(h):
    global WINDOW_HEIGHT
    WINDOW_HEIGHT = h
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
def tick_speed(speed):
    global TICK_SPEED
    TICK_SPEED = speed

def rect(color, x, y, w, h):
    global window
    re = (x,y,w,h)
    pygame.draw.rect(window, clamp_color(color), re)
    return re

def intersects(r0, r1):
    return pygame.Rect(r0[0], r0[1], r0[2], r0[3]).colliderect(pygame.Rect(r1[0], r1[1], r1[2], r1[3]))

def text(text, color, x, y, size):
    font = pygame.font.SysFont(None, size)
    image = font.render(str(text), False, color)
    window.blit(image, (x - image.get_width() / 2,y - image.get_height() / 2))

def clamp_color(color):
    return (color[0] % 256, color[1] % 256, color[2] % 256)

def color(r,g,b):
    return (r % 256, g % 256, b % 256)

def is_key_pressed(key):
    return key in keys_pressed or esc_pressed and key == ESCAPE

def was_key_just_released(key):
    return key in keys_released

def exit():
    global run
    run = False

def start(fun):
    global window, keys_pressed, run, esc_pressed, keys_released
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    
    while run:
        keys_released = set()
        next_keys_pressed = set(keys_pressed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == ESCAPE:
                    esc_pressed = True
            
                if event.unicode != "":
                    next_keys_pressed.add(event.unicode)
                    keys_pressed.add(event.unicode)
                else:
                    next_keys_pressed.add(event.key)
                    keys_pressed.add(event.key)
                    
            if event.type == pygame.KEYUP:
                if event.unicode != "":
                    keys_released.add(event.unicode)
                    next_keys_pressed.remove(event.unicode)
                else:
                    keys_released.add(event.key)
                    next_keys_pressed.remove(event.key)
                
        window.fill(BACKGROUND_COLOR)
        fun()
        pygame.display.update()
        
        keys_pressed = next_keys_pressed

        clock.tick(TICK_SPEED)
    
    pygame.quit()

