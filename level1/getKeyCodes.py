import pygame
from tLib.level0 import tools


def raw():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stopLoop()
        if e.type == pygame.KEYDOWN:
            print(e)

def formatted():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stopLoop()
        if e.type == pygame.KEYDOWN:
            print('pressed Key {0} has unicode {1} and scancode {2}'.format(e.key,e.unicode,e.scancode))

def full():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stopLoop()
        print(e)

def Type():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stopLoop()
        print('You have triggered an event of type:', pygame.event.event_name(e.type))

def noMouse():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stopLoop()
        if e.type != pygame.MOUSEMOTION:
            print(e)

def noMouseType():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stopLoop()
        if e.type != pygame.MOUSEMOTION:
            print('You have triggered an event of type:', pygame.event.event_name(e.type))


reactions = (raw, formatted, full, Type, noMouse, noMouseType)
del raw, formatted, full, Type, noMouse, noMouseType


def react(index):
    (tools.getListItem(reactions, index, None))()


loopGoing = True
funcKeys = (['raw'], ['formatted', 'doit', 'log keys'], ['full', 'everything', 'all'], ['type', 'event type'], ['full no mouse', 'no mouse'], ['type no mouse'])

def get_num_for_str(string):
    for k in range(len(funcKeys)):
        if string in funcKeys[k]:
            return k


def loop(func_name):
    global loopGoing
    func = reactions[get_num_for_str(func_name)]
    try:
        while loopGoing:
            func()
    except pygame.error:
        print('An Error has occurred. Maybe you didn\'t call start() before loop() ?')


def stopLoop():
    global loopGoing
    loopGoing = False

def start(width, height):
    pygame.init()
    pygame.display.set_mode((width, height))

def start_loop(width, height, func_name):
    start(width, height)
    loop(func_name)
