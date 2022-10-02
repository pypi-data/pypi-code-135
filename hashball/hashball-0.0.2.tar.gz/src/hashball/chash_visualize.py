# MIT License
#
# Copyright (c) 2021 Kevin L.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
CIRCLE_CENTER = (300, 300)
CIRCLE_RADIUS = 200

def visualize_hashball(cirhashkeys):
    import pygame
    import pygame.locals

    pygame.init()
    pygame.display.set_caption('Hashball Visualizer')
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Fill the scree with white color
    window.fill((59, 64, 73))
    
    # Draw the solid circle
    pygame.draw.circle(window, (177, 156, 217), CIRCLE_CENTER, CIRCLE_RADIUS, 0)

    line_color = (255, 255, 255)
    line_color_n = (0, 0, 0)

    for deg in cirhashkeys:
        end_points_on_circle = calculate_end_coords(deg)
        if deg > 0:
            pygame.draw.line(window, line_color, [300, 300], end_points_on_circle, width=1)
        else:
            pygame.draw.line(window, line_color, [300, 300], end_points_on_circle, width=1)
    
    my_font = pygame.font.SysFont('Georgia', 33)
    text_surface = my_font.render('Hashball Visualization', True, (255, 255, 255))
    text_width = text_surface.get_width()
    window.blit(text_surface, (300 - (text_width / 2), 30))


    my_font = pygame.font.SysFont('Georgia', 23)
    text_surface = my_font.render(f'Record Count: {len(cirhashkeys)}', True, (255, 255, 255))
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    window.blit(text_surface, (300 - (text_width / 2), 700 - 50))

    # Draws the surface object to the screen.
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE: done = True
            elif event.type == pygame.locals.QUIT:
                done = True

        # pygame.display.update()


def calculate_end_coords(deg):
    '''
    Finding the x,y coordinates on circle, based on given angle
    '''
    from math import cos, sin, pi, radians
    #center of circle, angle in degree and radius of circle
    center = CIRCLE_CENTER
    angle = radians(deg)
    radius = CIRCLE_RADIUS
    x = center[0] + (radius * cos(angle))
    y = center[1] + (radius * sin(angle))
    return [x, y]


if __name__ == "__main__":
    visualize_hashball([0, 90,270])