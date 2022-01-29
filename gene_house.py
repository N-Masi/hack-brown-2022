import sys, pygame
pygame.init()

# game hyperparameters
size = width, height = 512, 512
speed = 3
velocity = [0, 0]
black = 0, 0, 0

# display screen
screen = pygame.display.set_mode(size)

# load & initalize images
background = pygame.image.load("assets/background.png")
player = pygame.image.load("assets/char_walk_right.gif")
player_rect = player.get_rect()

# initialize clock
clock = pygame.time.Clock()

# set up Time & Score text
font = pygame.font.Font(None, 32)
time = 0
text = font.render("Time: "+str(time), True, (10, 10, 10))
textpos = text.get_rect(x=100, y=10)
score = 0
score_text = font.render("Score: "+str(score), True, (10, 10, 10))
scoretextpos = text.get_rect(x=300, y=10)

# create list of crops
crops = []

# tomato class
class Tomato():

    def __init__(self):
        self.image = pygame.image.load("assets/seeds.png")
        self.crop_rect = player_rect.copy().move(70,50)
        self.timestamp = pygame.time.get_ticks()//1000

    def check_grow(self):
        if time - self.timestamp >= 5:
            self.grow()
            self.timestamp = time

    def grow(self):
        pass
        if self.image == pygame.image.load("assets/seeds.png")
            self.image = pygame.image.load("assets/bud.png")

        elif self.image == pygame.image.load("assets/bud.png")
            self.image = pygame.image.load("assets/sprout.png")

        elif self.image == pygame.image.load("assets/sprout.png")
            self.image = pygame.image.load("assets/tomato_bloom.png")

        else pass


# main game loop
while 1:
    # tick clock & update time & score
    clock.tick(60)
    time = pygame.time.get_ticks()//1000
    text = font.render("Time: "+str(time), True, (10, 10, 10))
    score = 0
    score_text = font.render("Score: "+str(score), True, (10, 10, 10))

    # move character if key is pressed
    for event in pygame.event.get():
        # handle quitting the game
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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            tomato = Tomato()
            valid_spot = True
            # test if the new tomato would overlap an old one
            for crop in crops:
                if pygame.Rect.colliderect(tomato.crop_rect, crop.crop_rect):
                    valid_spot = False
            # add the tomato to crops if it doesn't overlap any other crop
            if valid_spot:
                crops.append(tomato)
        else:
            velocity[0]=0
            velocity[1]=0
            

    # prevent player from moving off-screen
    if player_rect.left < -25:
        velocity[0] = max(0, velocity[0])
    if player_rect.right > width + 25:
        velocity[0] = min(0, velocity[0])
    if player_rect.top < 0:
        velocity[1] = max(0, velocity[1])
    if player_rect.bottom > height:
        velocity[1] = min(0, velocity[1])
    player_rect = player_rect.move(velocity)

    # redraw the screen
    screen.fill(black)
    screen.blit(background, (0,0))
    screen.blit(text, textpos)
    screen.blit(score_text, scoretextpos)
    # draw everything in the crops list
    for crop in crops:
        crop.check_grow()
        screen.blit(crop.image, crop.crop_rect)
    screen.blit(player, player_rect)
    pygame.display.flip()