import pygame
import sys
import random
from time import sleep

padWidth = 480 # 게임화면의 가로크기
padHeight = 640 # 게임화면의 세로크기

rockImage = ['icecream.png', 'fried-chicken.png ', 'pizza.png ', 'cake.png ', 'hamburger.png ',
             'egg.png', 'broccoli.png', 'cabbage', 'carrot.png', 'vegetable.png'] # 음식 이미지 추가 - Yu




explsionSound = []


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

# Han 게임 메세지 출력
def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font('폰트', 80)
    text = textfont.render(text, True, (55,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()

# Han 전투기가 운석과 충돌했을 때 메세지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴!')

# Han 게임 오버 메세지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')



#Han 게임에 등장하는 객체 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))



def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))

    pygame.display.set_caption('PyShooting') # 게임 이름 추가 - Yu
    clock = pygame.time.Clock() # 시간 추척 추가 - Yu

    pygame.mixer.music.load('music.wav')  # Chan 음악 재생
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('missile.wav')
    gameOverSound = pygame.mixer.Sound('gameover.wav')



    pygame.init()   #Han

    gamePad = pygame #Han

    gamePad = pygame.display.set.mode((padWidth, padHeight)) #Han
    background = pygame.image.load('pig.png')  #Han
    clock = pygame.time.Clock()  #Han
    pygame.display.set_caption('PyShooting')


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

        drawObject(background, 0, 0) #배경화면 그리기
        pygame.display.update() #Han 게임화면을 다시 그림


            # 전투기 움직이기
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT: #전투기 왼쪽으로 이동
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT: #전투기 오른쪽으로 이동
                    fighterX += 5

                elif event.key == pygame.K_SPACE:  # Sae 미사일발사
                    missileSound.play()
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0


        drawObject(background, 0, 0)  # 배경화면 그리기

            # Han 전투기가 운석과 충돌했는지 체크
            if y < rockY + rockHeight:
                if(rockX > x and rockX < x + fighterWidth) or ＼
                (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth)
                crash()

            drawObject(figther, x, y) #비행기를 게임 화면의 (x, y) 좌표에 그림

            if rockPassed == 3: # Han 운석 3개 놓치면 게임 오버
                gameOver()


            # 운석을 맞춘 경우
           if isShot:
                #운석 폭발
                drawObject(explosion, rockX, rockY)
                destroySound.play()

                #새로운 운석(랜덤)
                rock= pygame.image.load(random.choice(rockImage))
                rockSize = rock.get_rect().size
                rockWidth = rockSize[0]
                rockHeight = rockSize[1]
                rockX = random.randrange(0, padWidth - rockWidth)
                rockY = 0
                destroySound = pygame.mixer.Sound(random.choice(explsionSound))
                isShot = False

                # Han 운석 맞추면 속도 증가
                rockSpeed += 0.02
                if rockSpeed >= 10:
                    rockSpeed = 10






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
