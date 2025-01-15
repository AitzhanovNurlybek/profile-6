import pygame
clock = pygame.time.Clock()


pygame.init()
pygame.display.set_caption("Nurlybeks game")



screen = pygame.display.set_mode((700,400),flags=pygame.NOFRAME)
bg = pygame.image.load("background.png").convert()

monster = pygame.image.load("monster.png").convert_alpha()
monster_x = 702
monster_list_in_game = []

walk_left = [
    pygame.image.load("player_left/player_left1.png").convert_alpha(),
    pygame.image.load("player_left/player_left2.png").convert_alpha(),
    pygame.image.load("player_left/player_left3.png").convert_alpha(),
    pygame.image.load("player_left/player_left4.png").convert_alpha(),   
]

walk_right=[
    pygame.image.load("player_right/player_right1.png").convert_alpha(),
    pygame.image.load("player_right/player_right2.png").convert_alpha(),
    pygame.image.load("player_right/player_right3.png").convert_alpha(),
    pygame.image.load("player_right/player_right4.png").convert_alpha(),
]


bg_x = 0
player_anim_count = 0
player_speed = 5
player_x = 150
player_y = 227
is_jump = False
jump_count = 7

running = True
#таймер появления монстра 
monster_timer = pygame.USEREVENT + 1
pygame.time.set_timer(monster_timer,3000)
while running:

    pygame.display.update()

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    # Loop through all monsters to check collision with each one
    for monster_rect in monster_list_in_game:
        if player_rect.colliderect(monster_rect):
            print("ТЫ лох")
            # Handle player death (reset position, or perform any other action)
            player_x = 150
            player_y = 227
            # Optionally, you can also remove the collided monster from the list
            monster_list_in_game.remove(monster_rect)

    keys = pygame.key.get_pressed()
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 700, 0))

    # Blit the monsters
    for monster_rect in monster_list_in_game:
        screen.blit(monster, monster_rect)

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 30:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 600:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2

            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    if player_anim_count == 3:
        player_anim_count == 0  # Here was the issue: should be '=', not '=='
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -700:
        bg_x = 0

    # Move monsters and remove them if they go off screen
    for monster_rect in monster_list_in_game:
        monster_rect.move_ip(-7, 0)
        if monster_rect.right < 0:
            monster_list_in_game.remove(monster_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == monster_timer:
            monster_list_in_game.append(monster.get_rect(topleft=(702, 245)))

    clock.tick(20)
