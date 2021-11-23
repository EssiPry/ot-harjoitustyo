import pygame

def main():
    pygame.init()
    game_display = pygame.display.set_mode((300, 600))
    pygame.display.set_caption('Testi-tetris')

    x = 120
    y = 00
    width = 60
    height = 60
    vel = 30

    clock = pygame.time.Clock()

    run = True

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x >= vel:
            x -= vel

        if keys[pygame.K_RIGHT] and x < 300 - width:
            x += vel

        if keys[pygame.K_DOWN] and y <= 600 - height -vel:
            y += vel

        game_display.fill((0,0,0))
        pygame.draw.rect(game_display,(255, 134, 94), (x, y, width, height))
        pygame.display.flip()
        if y <= 600 - height:
            y += 1
        clock.tick(60)


if __name__== "__main__":
    main()
