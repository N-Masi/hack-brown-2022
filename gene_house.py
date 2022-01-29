import sys, pygame
pygame.init()

size = width, height = 512, 512
speed = 3
velocity = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

background = pygame.image.load("background.png")
player = pygame.image.load("char_walk_right.gif")
player_rect = player.get_rect()
clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)
time = "0"
text = font.render("Time: "+str(time), True, (10, 10, 10))
textpos = text.get_rect(x=100, y=10)
score = 0
score_text = font.render("Score: "+str(score), True, (10, 10, 10))
scoretextpos = text.get_rect(x=300, y=10)

while 1:
    clock.tick(60)
    time = str(pygame.time.get_ticks()//1000)
    text = font.render("Time: "+time, True, (10, 10, 10))
    score = 0
    score_text = font.render("Score: "+str(score), True, (10, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            velocity[0]=0
            velocity[1]=speed
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            velocity[0]=0
            velocity[1]=-speed
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            velocity[0]=speed
            velocity[1]=0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            velocity[0]=-speed
            velocity[1]=0
        else:
            velocity[0]=0
            velocity[1]=0

    if player_rect.left < -25:
        velocity[0] = max(0, velocity[0])
    if player_rect.right > width + 25:
        velocity[0] = min(0, velocity[0])
    if player_rect.top < 0:
        velocity[1] = max(0, velocity[1])
    if player_rect.bottom > height:
        velocity[1] = min(0, velocity[1])
    player_rect = player_rect.move(velocity)

    screen.fill(black)
    screen.blit(background, (0,0))
    screen.blit(player, player_rect)
    screen.blit(text, textpos)
    screen.blit(score_text, scoretextpos)
    pygame.display.flip()