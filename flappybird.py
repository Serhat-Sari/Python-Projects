import pygame, sys , random

pygame.init()

screen = pygame.display.set_mode((320,640))
clock = pygame.time.Clock()

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (330,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (330,random_pipe_pos-180))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 320:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def check_collide(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
            

    if bird_rect.top <= 0 or bird_rect.bottom >= 575:
        return False
    
    return True

#background-day
bg_surface = pygame.image.load('flappy/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(320,640))

#floor
floor_surface = pygame.image.load('flappy/sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(1024,100))
floor_x_pos = 0

#birb
bird_surface = pygame.image.load('flappy/sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale(bird_surface,(33,25))
bird_rect = bird_surface.get_rect(center = (33,320))

#pipe XD
pipe_surface = pygame.image.load('flappy/sprites/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1400)
pipe_height = [230,240,250,280,320,350,370,400]

gravity = 0.08
bird_movement = 0
game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_active:
                bird_movement = 0
                bird_movement = -2.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (33,320)
                bird_movement = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface,(0,0))

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_collide(pipe_list)

    screen.blit(floor_surface,(floor_x_pos,555))
    floor_x_pos -= 1
    if floor_x_pos <= -512:
        floor_x_pos = 0

    
    pygame.display.update()
    clock.tick(120)




