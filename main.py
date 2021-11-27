import pygame
import sys
import random
from time import sleep

padWidth = 480 # 게임화면의 가로크기
padHeight = 640 # 게임화면의 세로크기
rockImage = ['icecream.png', 'fried-chicken.png ', 'pizza.png ', 'cake.png ', 'hamburger.png ',
             'egg.png', 'broccoli.png', 'cabbage', 'carrot.png', 'vegetable.png'] # 음식 이미지 추가 - Yu

# Sae 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font("폰트 경로인가?", 20)
    text = font.render('파괴한 운석 수:' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (10, 0))


# Sae 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font("폰트", 20)
    text = font.render('놓친 운석:' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (360, 0))


def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting') # 게임 이름 추가 - Yu
    clock = pygame.time.Clock() # 시간 추척 추가 - Yu


    pygame.init()   #Han
    gamePad = pygame #Han

    missile = pygame.image.load('spoon-and-fork.png') # Sae 미사일그림







def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound

    # Sae 무기좌표 리스트
    missileXY = []

    # 음식 랜덤 생성 - Yu
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size # 운석 실제 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    # 운석 초기 위치 설정 - Yu
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in  [pygame.QUIT]: #게임 프로그램 종료
                pygame.quit()
                sys.exit()
        drawObject(background, 0, 0) #배경화면 그리기 -Han
        pygame.display.update() #게임화면을 다시 그림 -Han
        clock.tick(60) # 게임화면의 초당 프레임수를 60으로 설정 - Yu

    pygame.quit() # pygame 종료 - Yu

            # 전투기 움직이기
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT: #전투기 왼쪽으로 이동

                elif event.key == pygame.K_RIGHT: #전투기 오른쪽으로 이동

                elif event.key == pygame.K_SPACE:  # Sae 미사일발사
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])









        # Sae 미사일 발사 화면에 그리기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):  # Sae 미사일요소에 대해 반복함
                bxy[1] -= 10  # Sae 총알의 y좌표 -10 (위로 이동)
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:  #Sae 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy)  #Sae 미사일 제거
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY += rockSpeed # 운석이 아래로 떨어질 때 y좌표 증가 - Yu

        # 운석이 지구로 떨어진 경우(화면 밖으로) - Yu
        if rockY > padHeight:
            # 새로운 운석 생성(랜덤)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0

        drawObject(rock, rockX, rockY) # 운석 그리기



       # Sae 운석 맞춘 점수 표시
        writeScore(shotCount)

        # 운석이 지구로 떨어진 경우
        if rockY > padHeight:
            # 새로운 운석(랜덤)

            rockPassed += 1

        # Sae 놓친 운석 수 표시
        writePassed(rockPassed)






initGame()
runGame()
