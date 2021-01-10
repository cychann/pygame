import time
import random as rnd
import math
import pygame
from player import Player
from bullet import Bullet1
from bullet import Bullet2
from bullet import Bullet3

lastcollision = None  # 초기값


def collision(obj1, obj2):
    global lastcollision  # lastcollision 변수 선언
    # 마지막 충돌 시간과 현재 시간을 비교해서 그 차이가 무적 시간보다 작다면 충돌을 감지하지 못하도록
    if lastcollision is not None and time.time() - lastcollision < 3:
        if ((int(((time.time()-lastcollision))*10)) % 2 == 0):  # 일정시간동안 깜빡이게 하기 위해 0과 1의 값이 반복되서 나오도록
            # 위 조건을 만족할때 True를 넣어주면 이 시간에는 비행기가 출력이 안된다.
            player.nodamgetime = True
        else:
            # 위 조건을 만족하지 않을 때는 False값을 넣어줘서 비행기가 출력된다.
            player.nodamgetime = False

        return False
    if math.sqrt((obj1.pos[0] - obj2.pos[0]) ** 2 + (obj1.pos[1] - obj2.pos[1]) ** 2) < 20:
        collision_sound.play()  # 부딪히면 효과음(미션1)
        # 부딪혔을 때 터지는 그림효과(미션2)
        screen.blit(boom_image, (obj1.pos[0], obj1.pos[1]))
        pygame.display.update()  # 터지는 그림을 그리고 화면 갱신
        lastcollision = time.time()  # 무적시간이 아니면서 충돌을 했다면 마지막 충돌 시간을 업데이트
        return True
    return False


def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)


# Initialize the pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
WIDTH, HEIGHT = 1000, 800

# Background image
bg_image = pygame.image.load('bg.jpg')

# Background music
pygame.mixer.music.load('bgm.wav')
pygame.mixer.music.play(-1)

pygame.display.set_caption("총알 피하기")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

player = Player(WIDTH/2, HEIGHT/2)

bullets1 = []  # 총알1
for i in range(3):
    bullets1.append(Bullet1(0, rnd.random()*HEIGHT,
                            rnd.random()-0.5, rnd.random()-0.5))

bullets2 = []  # 총알2
for i in range(3):
    bullets2.append(Bullet2(0, rnd.random()*HEIGHT,
                            rnd.random()-0.5, rnd.random()-0.5))

bullets3 = []  # 총알3
for i in range(3):
    bullets3.append(Bullet3(0, rnd.random()*HEIGHT,
                            rnd.random()-0.5, rnd.random()-0.5))


time_for_adding_bullets = 0

start_time = time.time()

bg_posx = -500  # 배경을 그리기 위한 x좌표
bg_posy = -100  # y좌표

# 부딪혔을 때 효과음 선언
collision_sound = pygame.mixer.Sound('collision.wav')
# 부딪혔을 때 터지는 그림
boom_image = pygame.image.load('boom.png')
boom_image = pygame.transform.scale(boom_image, (64, 64))  # 비행기와 같은 크기로

# 목숨을 표현하기 위한 하트
life_image = pygame.image.load('heart.png')
life_image = pygame.transform.scale(life_image, (30, 30))
# Game Loop
running = True
gameover = False
score = 0
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 게임 창의 X버튼을 눌렀을 때
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)

    # 화면에 검은색 채우기 (RGB - Red, Green, Blue)
    # screen.fill((0, 0, 0))

    if event.type == pygame.KEYDOWN:
        if -1053 < bg_posx < 0 and -700 < bg_posy < 0:  # 배경이미지의 끝에 도달하기 전까지만 움직이도록 한다
            if event.key == pygame.K_LEFT:  # 118줄에서 해당 숫자의 의미는 보고서에 적어놓았습니다.
                bg_posx += -0.05 * dt
            elif event.key == pygame.K_RIGHT:
                bg_posx += 0.05 * dt
            elif event.key == pygame.K_UP:
                bg_posy += 0.05 * dt
            elif event.key == pygame.K_DOWN:
                bg_posy += -0.05 * dt
        if bg_posx <= -1053:  # 127~134줄의 코드는 끝에 도달하였을 때
            bg_posx += 1  # 배경의 x,y좌표를 다시 118 if문에 해당하는 범위 안으로 넣어주기 위해서이다.
        elif bg_posx >= 0:  # 이 작업을 해주지 않으면 화면 끝에 도달 후, 화면이 다시 움직이지 않는다.
            bg_posx -= 1
        if bg_posy <= -700:
            bg_posy += 1
        elif bg_posy >= 0:
            bg_posy -= 1

    screen.blit(bg_image, (bg_posx, bg_posy))  # 배경 그리기
    player.update(dt, screen)
    player.draw(screen)

    for b in bullets1:  # 총알1
        b.update_and_draw(dt, screen)
    for b in bullets2:  # 총알2
        b.update_and_draw(dt, screen)
    for b in bullets3:  # 총알3
        b.update_and_draw(dt, screen)

    if gameover:
        player.nodamgetime = False  # 게임이 종료되었을 때 비행기가 사라지지 않게 하기 위해
        draw_text("GAME OVER", 100, (WIDTH/2 - 300,
                                     HEIGHT/2 - 50), (255, 255, 255))
        txt = "Time: {:.1f}  Bullets: {}".format(score, len(
            bullets1) + len(bullets2) + len(bullets3))  # 총알1+총알2+총알3
        draw_text(txt, 32, (WIDTH/2 - 150, HEIGHT/2 + 50), (255, 255, 255))
        scoreboard = open("writescore.txt", "r")
        scorelist = scoreboard.readlines()  # 이전 기록들을 가져와 읽기
        tmp = 0  # 기록들을 한줄마다 입력하기 위한 상수
        for s in scorelist:
            tmp += 1
            # 30*tmp를 하여 각 리스트를 출력할때마다 각각 다른 줄에 입력되도록
            draw_text("({}) : {}".format(tmp, s.strip()),
                      20, (50, 30*tmp), (255, 255, 255))
        # 만약 점수가 10개보다 적게 저장되어 있으면 매기록이 10위 안에 드므로 무조건 ranking안에 존재한다.
        if len(scorelist) < 10:
            draw_text("New record!! ->", 32, (100, 450),
                      (0, 255, 0))  # 시간점수 옆에 메시지를 띄어주고
            draw_text("! Congratulations !", 70,
                      (230, 100), (0, 255, 0))  # 축하 메시지와
            # 점수가 순위권 안에 있음을 강조한다.
            draw_text("It's in the ranking score!!",
                      32, (330, 500), (0, 255, 0))
        # 만약 점수가 10개이상이 되면, 점수표에 기록되어 있는 점수 중에서 가장 작은 수와 현재 스코어를 비교한다.
        elif len(scorelist) >= 10:
            if score > float(scorelist[9]):  # 만약 현재 스코어가 순위권 안에 있다면
                draw_text("New record!! ->", 32, (100, 450), (0, 255, 0))
                draw_text("! Congratulations !", 70, (230, 100), (0, 255, 0))
                draw_text("It's in the ranking score!!",
                          32, (330, 500), (0, 255, 0))
            elif score <= float(scorelist[9]):  # 만약 현재 스코어가 순위권 안에 들지 못하는 점수라면
                # 다시 시도하여 순위권에 들라는 메시지를 보여준다
                draw_text("Try Again..!", 70, (330, 100), (255, 0, 0))
    else:
        score = time.time() - start_time
        txt = "Time: {:.1f}  Bullets: {}".format(score, len(
            bullets1) + len(bullets2) + len(bullets3))  # 총알1+총알2+총알3
        draw_text(txt, 32, (10, 10), (255, 255, 255))
        lifetxt = "life: %d" % (player.life)
        draw_text(lifetxt, 32, (WIDTH/2, 10),
                  (255, 255, 255))  # 게임 상단에 life를 정수로 표현

        for life in range(player.life):
            # 목숨 개수 만큼 오른쪽 상단에 life이미지 출력
            screen.blit(life_image, (life*30 + 600, 10))

    pygame.display.update()  # 화면에 새로운 그림을 그린다 (화면을 갱신한다)

    if not gameover:
        for b1 in bullets1:  # 총알1
            if collision(player, b1):
                player.life -= 1  # 생명력을 1감소
                if player.life <= 0:  # 생명력이 0보다 작으면 게임을 종료하도록
                    gameover = True
        for b2 in bullets2:  # 총알2
            if collision(player, b2):
                player.life -= 2  # 생명력을 2감소
                if player.life <= 0:  # 생명력이 0보다 작으면 게임을 종료하도록
                    gameover = True
        for b3 in bullets3:  # 총알3
            if collision(player, b3):
                player.life -= 3  # 생명력을 3감소
                if player.life <= 0:  # 생명력이 0보다 작으면 게임을 종료하도록
                    gameover = True

        time_for_adding_bullets += dt*0.1  # 밸런스 조정을 위해 총알개수가 늘어나는 시간 감소
        if time_for_adding_bullets > 1000:
            bullets1.append(Bullet1(0, rnd.random()*HEIGHT,
                                    rnd.random()-0.5, rnd.random()-0.5))
            bullets2.append(Bullet2(0, rnd.random()*HEIGHT,
                                    rnd.random()-0.5, rnd.random()-0.5))
            bullets3.append(Bullet2(0, rnd.random()*HEIGHT,
                                    rnd.random()-0.5, rnd.random()-0.5))
            time_for_adding_bullets -= 1000

scoreboard = open("writescore.txt", "r")
scorelist = scoreboard.readlines()  # 기존에 존재하는 writescore라는 텍스트 파일을 읽은 후 작업진행
if len(scorelist) < 10:
    scoreboard = open("writescore.txt", "a")  # 정보가 쌓이도록
    scoreboard.write(str(score) + "\n")  # writescore.txt에 점수를 저장
    scoreboard = open("writescore.txt", "r")
    scorelist = scoreboard.readlines()  # 텍스트파일에 저장된 점수들을 읽고 리스트로 가져와
    scorelist = sorted(map(float, scorelist))  # 정렬한다
    scorelist.sort(reverse=True)  # 가장 오래 생존한 시간부터 출력되도록
    scoreboard = open("writescore.txt", "w")  # 기존의 내용들을 덮고 정렬된 점수로 표현시킨다
    for item in scorelist:
        scoreboard.write(str(item)[0:6] + "\n")  # 소수점 간결 표현 위해 6개만 출력되도록
elif len(scorelist) >= 10:  # 가장 길게 생존한 점수를 10개까지 저장하기 위해
    scoreboard = open("writescore.txt", "a")
    scoreboard.write(str(score) + "\n")
    scoreboard = open("writescore.txt", "r")
    scorelist = scoreboard.readlines()
    scorelist = sorted(map(float, scorelist))
    scorelist.sort(reverse=True)
    del scorelist[10]  # 가장 적은 생존시간을 삭제 후
    scoreboard = open("writescore.txt", "w")  # 최대 생존 점수 10개를 출력
    for item in scorelist:
        scoreboard.write(str(item)[0:6] + "\n")
