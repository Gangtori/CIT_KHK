import pygame

WHITE = (255,255,255)
pad_width = 1024
pad_hiegth = 700

def rungame():
    global gamepad, clock

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        gamepad.fill(WHITE)
        pygame.display.update()
        clock.tick(60)

    pygame.puit()

def initGame():
    global gamepad, clock

    pygame.init() #초기화
    gamepad = pygame.display.set_mode((pad_width, pad_hiegth))
    pygame.display.set_caption("game Title")
    clock = pygame.time.Clock()
    rungame()

initGame()
