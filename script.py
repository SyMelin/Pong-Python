import pygame

pygame.init()
# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Python")
run = True

# colors
PINK = (255, 16, 240)
AQUA = (0, 253, 255)
BLACK = (0, 0, 0)

# ball parameters
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.35, 0.35

# paddle parameters
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2,  WIDTH -(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

# main loop
while run:
    # fill the screen with black
    # so that the previous drawings are erased, the new position is drawn,
    # and the human eye is tricked and can see the ball moving
    wn.fill(BLACK)

    # all the events that happens in the pygame window will be stored in i
    for i in pygame.event.get():
        # if the user presses the quit button, the game will stop
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_z:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9

        # check if the user releases the key
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                right_paddle_vel = 0
            if i.key == pygame.K_z or i.key == pygame.K_s:
                left_paddle_vel = 0

    # movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    # ball's movements control
    # if the ball hits the up or down wall, it will bounce
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    # if the ball hits the left or right wall, the ball will be reset to the center
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.35, 0.35

    # paddles' movements control
    # if the paddle is about to go over the boundaries, it will stop
    if right_paddle_y <= 0:
        right_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height

    # ball's collision with the paddles
    # if the ball hits the left paddle, it will bounce
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    # if the ball hits the right paddle, it will bounce
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    # draw the elements
    pygame.draw.circle(wn, PINK, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, AQUA, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, AQUA, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # update the screen
    pygame.display.update()

