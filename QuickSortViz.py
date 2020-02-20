import pygame
import random


def quick_sort(reclist):
    quick_sort2(reclist, 0, len(reclist)-1)
    return reclist

def quick_sort2(reclist, lowest, highest):
    if lowest < highest:
        pivot = partition(reclist, lowest, highest)
        quick_sort2(reclist, lowest, pivot - 1)
        quick_sort2(reclist, pivot+1, highest)



def partition(reclist, lowest, highest):
    pivotId = get_pivot(reclist, lowest, highest)
    pivotVal = reclist[pivotId][3]
    reclist[pivotId][3], reclist[lowest][3] = reclist[lowest][3], reclist[pivotId][3]
    border = lowest

    for i in range(lowest, highest + 1):
        if reclist[i][3] < pivotVal:
            border += 1
            reclist[i][3], reclist[border][3] = reclist[border][3], reclist[i][3]
    reclist[lowest][3], reclist[border][3] = reclist[border][3], reclist[lowest][3]
    redraw_screen(screen, reclist, border, pivotId, lowest, highest)
    return border


def get_pivot(reclist, lowest, highest):
    mid = (lowest + highest) // 2
    pivot = highest
    if reclist[lowest][3] < reclist[mid][3]:
        if reclist[highest][3] > reclist[mid][3]:
            pivot = mid
    elif reclist[lowest][3] < reclist[highest][3]:
        pivot = lowest
    return pivot


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


def redraw_screen(screen, rects, borderId, pivotId, lowest, highest):
    screen.fill((0, 0, 0))
    for rec in rects:
        pygame.draw.rect(screen, (255, 255, 255), rec)
        pygame.draw.rect(screen, (255, 0, 0), rects[borderId])
        pygame.draw.rect(screen, (0, 255, 0), rects[pivotId])
        pygame.draw.rect(screen, (0, 0, 255), rects[lowest])
        pygame.draw.rect(screen, (0, 255, 255), rects[highest])
    pygame.display.update()

if __name__ == '__main__':
    screenWidth = 800
    screenHeight = 600
    recWidth = 2
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('QuickSortViz')
    recanglesHeights = get_random_list(screenHeight, screenWidth)
    rectangles = get_rectangles(recWidth, recanglesHeights)
    print(len(rectangles))
    print(rectangles)
    print(quick_sort(rectangles))

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
    pygame.quit()