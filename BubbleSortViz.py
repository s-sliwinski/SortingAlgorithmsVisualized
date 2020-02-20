import pygame
import random

def bubble_sort(reclist):
    for i in range(0, len(reclist) - 1):
        for j in range(0, len(reclist) - 1 - i):
            if reclist[j][3] > reclist[j+1][3]:
                reclist[j][3], reclist[j+1][3] = reclist[j+1][3], reclist[j][3]
            redraw_screen(screen, reclist, j)
    return reclist, True


def get_random_list(screenheight, screenwidth):
    rlist = [random.randint(1, screenheight) for i in range(screenwidth//2)]
    return rlist


def get_rectangles(recwidth, reclist):
    rects = []
    x = screenWidth
    for recheight in reclist:
        rects.append(pygame.Rect(x, screenHeight, recwidth,  -recheight))
        x -= recWidth
    return rects


def redraw_screen(screen, rects, i):
    screen.fill((0, 0, 0))
    for rec in rects:
        pygame.draw.rect(screen, (255, 255, 255), rec)
        pygame.draw.rect(screen, (255, 0, 0), rects[i])
    pygame.display.update()


########################################################################
if __name__ == '__main__':
    screenWidth = 800
    screenHeight = 600
    recWidth = 2
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('BubbleSortViz')
    recanglesHeights = get_random_list(screenHeight, screenWidth)
    rectangles = get_rectangles(recWidth, recanglesHeights)
    print(len(rectangles))
    print(rectangles)
    print(bubble_sort(rectangles))
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
    pygame.quit()



