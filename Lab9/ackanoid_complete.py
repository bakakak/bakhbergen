import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60
time=0
time1=0
wid=0
f=False
speed=0.005
pause=1

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 8
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
# collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
#unbreakable block
position=random.randrange(0,39)
unblock=block_list[position]
uncolor=color_list[position]
font = pygame.font.Font('freesansbold.ttf', 16)
text1 = font.render('Unbreak', True, (0,0,0), uncolor)
textRect = text1.get_rect()
textRect.center = (unblock[0]+unblock[2]/2,unblock[1]+unblock[3]/2)
block_list.pop(position)
color_list.pop(position)
#bonus
posbonus=random.randrange(0,39)
while posbonus==position:
    posbonus=random.randrange(0,39)
bonus=block_list[posbonus]
boncol=color_list[posbonus]
text2 = font.render('Bonus', True, (0,0,0), color_list[posbonus])
textRect2 = text2.get_rect()
textRect2.center = (block_list[posbonus][0]+block_list[posbonus][2]/2,block_list[posbonus][1]+block_list[posbonus][3]/2)
#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over:'+ str(game_score), True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)
block_list.pop(posbonus)
color_list.pop(posbonus)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)
colbl1=(255,255,255)
colbl2=(120,120,120)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pause=pause*(-1)
    if pause==1:
        screen.fill(bg)
        
        # print(next(enumerate(block_list)))
        
        [pygame.draw.rect(screen, color_list[color], block)
        for color, block in enumerate (block_list)] #drawing blocks
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.rect(screen, uncolor, unblock)
        screen.blit(text1, textRect)
        if f==False:
            pygame.draw.rect(screen, boncol, bonus)
            screen.blit(text2, textRect2)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
        # print(next(enumerate (block_list)))

        #Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy
        ballSpeed=ballSpeed+speed
        #paddle shrink
        time+=1
        if(time%100==0):
            paddle.width-=1

        #Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        #Collision blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
        if ball.colliderect(bonus) and f==False:
            time1=time
            wid=paddle.width
            paddle.left=0
            paddle.width=1200
            f=True
            dx, dy = detect_collision(dx, dy, ball, unblock)
        if time>time1+200 and f==True and paddle.width>wid:
            paddle.width-=3
            # collision_sound.play()
        if ball.colliderect(unblock):
            dx, dy = detect_collision(dx, dy, ball, unblock)
            
        #Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        #Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losefont.render('Game Over:'+ str(game_score), True, (255, 255, 255)), losetextRect)
        elif not len(block_list):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)
        # print(pygame.K_LEFT)
        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed


        pygame.display.flip()
        clock.tick(FPS)
    else:
        bl1=pygame.Rect(W/3+10,H/3+10,W/6-15,H/6-10)
        bl2=pygame.Rect(W/3+5+W/6,H/3+10,W/6-15,H/6-10)
        pygame.draw.rect(screen,(0,0,0),(W/3,H/3,W/3,H/3))
        pygame.draw.rect(screen,colbl1,bl1)
        pygame.draw.rect(screen,colbl2,bl2)
        easyfont = pygame.font.SysFont('comicsansms', 50)
        easytext = easyfont.render('EASY', True, (0, 0, 0))
        easytextRect = easytext.get_rect()
        easytextRect.center = (W/3+10+(W/6-15)/2,H/3+10+(H/6-10)/2)
        screen.blit(easytext, easytextRect)
        hardfont = pygame.font.SysFont('comicsansms', 50)
        hardtext = easyfont.render('HARD', True, (0, 0, 0))
        hardtextRect = hardtext.get_rect()
        hardtextRect.center = (W/3+10+(W/2-15)/2,H/3+10+(H/6-10)/2)
        screen.blit(hardtext, hardtextRect)
        pygame.display.flip()
        mouse_button=pygame.mouse.get_pressed()
        if mouse_button[0] and pygame.mouse.get_pos()[0]>W/3+10 and pygame.mouse.get_pos()[1]>H/3+10 and pygame.mouse.get_pos()[0]<W/3+10+W/6-15 and pygame.mouse.get_pos()[1]<H/3+10+H/6-10:
            speed=0
            paddle.width=300
            colbl1=(120,120,120)
            colbl2=(255,255,255)
        if mouse_button[0] and pygame.mouse.get_pos()[0]>W/3+5+W/6 and pygame.mouse.get_pos()[1]>H/3+10 and pygame.mouse.get_pos()[0]<W/3+10+W/3-15 and pygame.mouse.get_pos()[1]<H/3+10+H/6-10:
            speed=0.005
            paddle.width=200
            colbl2=(120,120,120)
            colbl1=(255,255,255)
        clock.tick(FPS)