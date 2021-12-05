#-*- coding:utf-8 -*-

import pygame
import sys
import random
from time import sleep

padWidth = 480 # 게임화면의 가로크기
padHeight = 640 # 게임화면의 세로크기

rockImage = ['icecream.png', 'fried-chicken.png ', 'pizza.png ', 'cake.png ', 'hamburger.png ',
             'egg.png', 'broccoli.png', 'cabbage.png', 'carrot.png', 'vegetable.png',
             'cola.png', 'candies.png', 'chocolate.png', 'hotdog.png', 'salad.png',
             'fish.png', 'nuts.png', 'bananas.png', 'corn.png','glass-of-water.png'] # 음식 이미지 추가 - Yu




explsionSound = ['eating1.wav','eating2.mp3','eating3.mp3']

choice = 0
# Sae 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    #font = pygame.font.Font("폰트 경로인가?", 20)

    # % 기존 코드가 안되서 다른 방법을 찾아봄. 시스템에서 쓸수있는 폰트리스트를 뽑아서 그중 가장 대중적인 것으로 지정
    ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    index = ableFonts.index("nanumgothic")
    font = pygame.font.SysFont(str(ableFonts[index]), 20, True, True)
    text = font.render('파괴한 운석 수:' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (10, 0))


# Sae 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    #font = pygame.font.Font("폰트", 20)

    # % 기존 코드가 안되서 다른 방법을 찾아봄. 시스템에서 쓸수있는 폰트리스트를 뽑아서 그중 가장 대중적인 것으로 지정
    ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    index = ableFonts.index("nanumgothic")
    font = pygame.font.SysFont(str(ableFonts[index]), 20, True, True)
    text = font.render('놓친 운석:' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (360, 0))


# Han 게임 메세지 출력
def writeMessage(text, textType, characterNum):
    global gamePad
    #textfont = pygame.font.Font('폰트', 80)
    ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    index = ableFonts.index("nanumgothic")
    font = pygame.font.SysFont(str(ableFonts[index]), 30, True, True)
    text = font.render(text, True, (255,0,0))

    if textType == 0 or textType == 1: #게임오버 / 충돌했을 때

        textpos = text.get_rect()
        textpos.center = (padWidth/2, padHeight/2)
        gamePad.blit(text, textpos)
        pygame.display.update()
        pygame.mixer.music.stop()
        gameOverSound.play()
        sleep(2)
        pygame.mixer.music.play(-1)
        runGame(1,characterNum)

    elif textType == 2: #캐릭터를 선택할 때
        textpos = text.get_rect()
        textpos.center = (padWidth / 2, padHeight / 5)
        gamePad.blit(text, textpos)
        pygame.display.update()

# Han 전투기가 운석과 충돌했을 때 메세지 출력
def crash(chracterNum):
    global gamePad
    writeMessage('전투기 파괴!', 0, chracterNum)

# Han 게임 오버 메세지 보이기
def gameOver(chracterNum):
    global gamePad
    writeMessage('게임 오버!', 1, chracterNum)

def choiceCharacter():
    global gamePad
    writeMessage('', 2, 0)


def help():
    global gamePad


def story():
    global gamePad





class Button2:  # 첫 시작화면 버튼 구성으로 새로 만들어봤어요.
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, type2):
        mouse2 = pygame.mouse.get_pos()
        click2 = pygame.mouse.get_pressed()

        drawObject(img_in, x, y)

        if x + width > mouse2[0] > x and y + height > mouse2[1] > y:  # 마우스가 캐릭터 위에 있을 때
            drawObject(img_act, x_act, y_act)  # 선택효과 있는 이미지로 그려줌
            if click2[0] and type2 == 1:  # play 버튼 눌렀을 때
                runGame(0,0)  # runGame 으로 들어가서 캐릭터 고르기

            elif click2[0] and type2 == 2:  # exit 버튼 눌렀을 때
                pygame.quit()  # 나가기
                sys.exit()

            elif click2[0] and type2 == 3:  # help 버튼 눌렀을 때
                pygame.quit()  # story 나오게 하기 #아직 그냥 나가기로 설정했어요.
                sys.exit()

            elif click2[0] and type2 == 4:  # story 버튼 눌렀을 때

                drawObject(storyline, 0, 0)
                pygame.display.update()

class Button1:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, type):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        drawObject(img_in, x, y)

        if x + width > mouse[0] > x and y +height > mouse[1] > y: #마우스가 캐릭터 위에 있을 때
           drawObject(img_act, x_act, y_act) #선택효과 있는 이미지로 그려줌
           if click[0]: #클릭했을 시
              sleep(1)
              runGame(1, type) #캐릭터 선택시 캐릭선택여부와 선택한 캐릭 타입 전달해서 게임실행

           else:
              drawObject(img_in, x, y)





#Han 게임에 등장하는 객체 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))



def initGame():
    global gamePad, clock,play, exit, help, story, clickPlay, clickExit, clickHelp,clickStory,storyline, background, fighter, fighter2, clickFighter, clickFighter2, missile, explosion, missileSound, gameOverSound, character_choice_bg
    pygame.init()  # Han
    gamePad = pygame.display.set_mode((padWidth, padHeight)) #Han

    pygame.display.set_caption('PyShooting') # 게임 이름 추가 - Yu

    play = pygame.image.load('play.png')  # 플레이버튼
    exit = pygame.image.load('exit.png')  # 나가기버튼
    help = pygame.image.load('help.png')  # 도움말버튼
    story = pygame.image.load('story.png')  # 스토리버튼

    clickPlay = pygame.image.load('clickplay.png')  # 클릭한플레이버튼
    clickExit = pygame.image.load('clickexit.png')  # 클릭한나가기버튼
    clickHelp = pygame.image.load('clickhelp.png')  # 클릭한도움말버튼
    clickStory = pygame.image.load('clickstory.png')  # 클릭한스토리버튼

    storyline = pygame.image.load('storyline.png')

    character_choice_bg = pygame.image.load('characterchoicebg.png')
    fighter = pygame.image.load('player.png') # 뚠뚠캐릭
    fighter2 = pygame.image.load('player2.png') # 마른캐릭
    clickFighter = pygame.image.load('clickplayer.png') #클릭한 뚠뚠캐릭
    clickFighter2 = pygame.image.load('clickplayer2.png') #클릭한 마른캐릭
    missile = pygame.image.load('spoon-and-fork.png')  # Sae 미사일그림
    explosion = pygame.image.load('mouth.png') # 폭발 그림 - ho
    background = pygame.image.load('backgound2.png')  # Han
    introimage = pygame.image.load('pig.png')
    clock = pygame.time.Clock() # 시간 추척 추가 - Yu

    pygame.mixer.music.load('music.mp3')  # Chan 음악 재생
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('throwing.mp3')
    gameOverSound = pygame.mixer.Sound('gameover.mp3')


    introGame = True
    while introGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        drawObject(introimage, 0, 0)

        playButton = Button2(play, 200, 400, 60, 60, clickPlay, 200, 400, 1)
        exitButton = Button2(exit, 200, 440, 60, 60, clickExit, 200, 440, 2)
        helpButton = Button2(help, 200, 480, 60, 60, clickHelp,200,480, 3)
        storyButton = Button2(story, 200, 520, 60,60, clickStory,200,520, 4)
        pygame.display.update()







def runGame(gametypeNum, charterNum):
    global gamepad, clock, background, fighter, fighter2, clickFighter, clickFighter2, missile, explosion, missileSound, character_choice_bg
    pygame.mixer.music.load('music.mp3')  # Chan 음악 재생
    pygame.mixer.music.play()

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    # 전투기 초기 위치 (x,y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    fighterY = 0  # 플레이어 움직임 y값

    # Sae 무기좌표 리스트
    missileXY = []

    # 음식 랜덤 생성 - Yu
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size # 운석 실제 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explsionSound))


    # 운석 초기 위치 설정 - Yu
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    # 전투기 미사일에 운석이 맞았을 경우 True
    isShot = False
    shotCount = 0
    rockPassed = 0

    choice = 0

    onGame = False
    while not onGame:

        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:  # 게임 프로그램 종료
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # 전투기 왼쪽으로 이동
                    fighterX -= 5
                elif event.key == pygame.K_RIGHT:  # 전투기 오른쪽으로 이동
                    fighterX += 5
                elif event.key == pygame.K_UP:  # %플레이어가 위쪽으로 이동
                    fighterY -= 5
                elif event.key == pygame.K_DOWN:  # %플레이어가 아래쪽으로 이동
                    fighterY += 5
                elif event.key == pygame.K_SPACE:  # Sae 미사일발사
                    missileSound.play()
                    missileX = x + fighterWidth / 2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type == pygame.KEYUP:  # 방향키를 떼면
                # 플레이어가 멈춤
                # 위아래 움직임 추가
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighterX = 0
                    fighterY = 0






        if gametypeNum == 0: # 최초 캐릭터 선택

         drawObject(character_choice_bg, 0, 0)  # 배경화면 그리기 -Han
         fighter1Button = Button1(fighter, 100, 255, 60, 60, clickFighter, 97, 252, 1)
         fighter2Button = Button1(fighter2, 310, 230, 60, 60, clickFighter2, 307, 227, 2)
         choiceCharacter() #캐릭터를 선택해주세요 글씨


        elif gametypeNum == 1: # 캐릭터 선택이 끝난 이후

            drawObject(background, 0, 0)  # 배경화면 그리기 -Han

            if charterNum == 1: #뚠뚠 캐릭터 선택
                drawObject(fighter, x, y)
            else: #마른 캐릭터 선택
                drawObject(fighter2, x, y-23) # 머리만 나와서 -23해서 위치 조정함


            #미사일 오브젝트 그리기
            if len(missileXY) != 0:
                for bx, by in missileXY:
                    drawObject(missile, bx, by)


            # Sae 미사일 발사 화면에 그리기
            if len(missileXY) != 0:
                for i, bxy in enumerate(missileXY):  # Sae 미사일요소에 대해 반복함
                    bxy[1] -= 10  # Sae 총알의 y좌표 -10 (위로 이동)
                    missileXY[i][1] = bxy[1]

                    if bxy[1] < rockY:
                        if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                            missileXY.remove(bxy)
                            isShot = True
                            shotCount += 1

                    if bxy[1] <= 0:  #Sae 미사일이 화면 밖을 벗어나면
                        try:
                            missileXY.remove(bxy)  #Sae 미사일 제거
                        except:
                            pass



            # Sae 운석 맞춘 점수 표시
            writeScore(shotCount)

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
                rockPassed += 1



            if rockPassed == 3: # Han 운석 3개 놓치면 게임 오버
                gameOver(charterNum)

            # Sae 놓친 운석 수 표시
            writePassed(rockPassed)

            # 플레이어 위치 재조정
            x += fighterX
            if x < 0:
                x = 0
            elif x > padWidth - fighterWidth:
                x = padWidth - fighterWidth

            # 이게 게임패드 안에서만 움직이게 만드려고 하는 거 같은데
            y += fighterY
            if y < 0:
                y = 0
            elif y > padHeight - fighterHeight:
                y = padHeight - fighterHeight



            # Han 전투기가 운석과 충돌했는지 체크
            if y < rockY + rockHeight:
                if (rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
                    crash(charterNum)


            # 운석을 맞춘 경우
            if isShot:

               # 운석 폭발
               drawObject(explosion, rockX, rockY)
               destroySound.play()

               # 새로운 햣 운석(랜덤). 파괴되면 새로운 운석 생성
               rock = pygame.image.load(random.choice(rockImage))
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


            drawObject(rock, rockX, rockY)  # 장애물 그리기

            pygame.display.update() #게임화면을 다시 그림 -Han
            clock.tick(60) # 게임화면의 초당 프레임수를 60으로 설정 - Yu

    pygame.quit() # pygame 종료 - Yu

initGame()
runGame(0, 0)

