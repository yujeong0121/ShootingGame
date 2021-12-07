#-*- coding:utf-8 -*-

import pygame
import sys
import random
from time import sleep
import math
import time

padWidth = 480 # 게임화면의 가로크기
padHeight = 640 # 게임화면의 세로크기


explsionSound = ['eating1.wav','eating2.mp3','eating3.mp3']

choice = 0
# Sae 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    #font = pygame.font.Font("폰트 경로인가?", 20)

    # # % 기존 코드가 안되서 다른 방법을 찾아봄. 시스템에서 쓸수있는 폰트리스트를 뽑아서 그중 가장 대중적인 것으로 지정
    # ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    # index = ableFonts.index("휴먼아미체")
    font = pygame.font.Font('NEXONFootballGothicB.ttf', 25)  # 폰트 설정
    text = font.render('증감 점수:' + str(count), True, (255, 20, 147))
    gamePad.blit(text, (10, 9))


# Sae 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    #font = pygame.font.Font("폰트", 20)
    font = pygame.font.Font('NEXONFootballGothicB.ttf', 25)  # 폰트 설정
    text = font.render('놓친 운석:' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (360, 9))

def writeUlt(times):
    global gamePad
    font = pygame.font.Font('NEXONFootballGothicB.ttf', 25)  # 폰트 설정
    text = font.render('궁극기:' + str(times), True, (255, 69, 0))
    gamePad.blit(text, (380, 9))



# Han 게임 메세지 출력
def writeMessage(text, textType, characterNum):
    global gamePad
    #textfont = pygame.font.Font('폰트', 80)

    font = pygame.font.Font('NEXONFootballGothicB.ttf', 40)  # 폰트 설정
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

def writeMessage1(text): #Chan 일시적으로 메세지 표현
    global gamePad
    #textfont = pygame.font.Font('폰트', 80)
    font = pygame.font.Font('NEXONFootballGothicB.ttf', 40)  # 폰트 설정
    text = font.render(text, True, (255,255,0))

    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)

# Han 전투기가 운석과 충돌했을 때 메세지 출력
def crash(chracterNum):
    global gamePad
    writeMessage('전투기 파괴!', 0, chracterNum)

# Han 게임 오버 메세지 보이기

#def gameOver(chracterNum):
#   global gamePad
#   writeMessage('게임 오버!', 1, chracterNum)


def choiceCharacter(text):
    global gamePad
    writeMessage(text, 2, 0)



def occur_explosion(surface, x, y):
    explosion_image = pygame.image.load('mouth.png')
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)



class Button2:  # 첫 시작화면 버튼 구성으로 새로 만들어봤어요.

    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, type2):
        mouse2 = pygame.mouse.get_pos()
        click2 = pygame.mouse.get_pressed()
        self.sound = pygame.mixer.Sound('click_sound.mp3')
        drawObject(img_in, x, y)

        if x + width > mouse2[0] > x and y + height > mouse2[1] > y:  # 마우스가 캐릭터 위에 있을 때
            drawObject(img_act, x_act, y_act)  # 선택효과 있는 이미지로 그려줌
            if click2[0] and type2 == 1:  # play 버튼 눌렀을 때
                self.sound.play()
                runGame(0,0)  # runGame 으로 들어가서 캐릭터 고르기

            elif click2[0] and type2 == 2:  # exit 버튼 눌렀을 때
                self.sound.play()
                pygame.quit()  # 나가기
                sys.exit()

            elif click2[0] and type2 == 3:  # help 버튼 눌렀을 때
                self.sound.play()
                drawObject(helpimg, 0,0)
                pygame.display.update()

            elif click2[0] and type2 == 4:  # story 버튼 눌렀을 때
                self.sound.play()
                drawObject(storyline, 0, 0)
                pygame.display.update()

class Button1:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, type):
        global total_time, start_ticks # 타이머 관련 변수
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.sound = pygame.mixer.Sound('click_sound.mp3')
        drawObject(img_in, x, y)

        if x + width > mouse[0] > x and y +height > mouse[1] > y: #마우스가 캐릭터 위에 있을 때
           drawObject(img_act, x_act, y_act) #선택효과 있는 이미지로 그려줌
           if click[0]: #클릭했을 시
              total_time = 120 #시간 초기화
              start_ticks = pygame.time.get_ticks()#시간 초기화

              self.sound.play()
              sleep(1)
              runGame(1, type) #캐릭터 선택시 캐릭선택여부와 선택한 캐릭 타입 전달해서 게임실행

           else:
              drawObject(img_in, x, y)


#음식 클래스
class Food(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Food, self).__init__()
        car_image1 = ['egg.png', 'broccoli.png', 'cabbage.png', 'carrot.png', 'vegetable.png',
                      'salad.png', 'fish.png', 'nuts.png', 'bananas.png', 'corn.png', 'glass-of-water.png']
        car_image2 = ['icecream.png', 'fried-chicken.png ', 'pizza.png ', 'cake.png ', 'hamburger.png ',
                      'cola.png', 'candies.png', 'chocolate.png', 'hotdog.png']

        # 이미지중에서 랜덤으로 선택한다.
        choiceNum = random.randint(0, 2)
        if choiceNum == 0:  # 몸에 좋은 음식
            self.image = pygame.image.load(random.choice(car_image1))
            self.add_minus_score = 2
        else: #몸에 나쁜 음식
            self.image = pygame.image.load(random.choice(car_image2))
            self.add_minus_score = -2


        #self.image = pygame.image.load(random.choice(rock_images))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self): # 음식이 떨어져서 화면밖으로 나갔을 때
        if self.rect.y > padHeight:
            return True



class Missile(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Missile, self).__init__()
        self.image = pygame.image.load('spoon-and-fork.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound('throwing.mp3')


    def launch(self):
        self.sound.play()   # 미사일 날라갈때 소리

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0:
            self.kill()

    def collide(self, sprites): #미사일이 충돌했을 때
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite




#Han 게임에 등장하는 객체 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))



def initGame():
    global gamePad, clock,title, play, exit, help, story, clickPlay, clickExit, clickHelp, clickStory, helpimg, storyline, background, fighter, \
        fighter2, clickFighter, clickFighter2, missile, explosion, missileSound, gameOverSound, character_choice_bg, replaybuttonimg, exitbottonimg, \
        clearimg, overimg, ultSound, clickSound, restart, clickrestart, oversound, clearsound, start_ticks, total_time, timeOutImage, timeOutSound
    pygame.init()  # Han
    gamePad = pygame.display.set_mode((padWidth, padHeight)) #Han

    pygame.display.set_caption('Diet Go!') # 게임 이름 추가 - Yu
    title = pygame.image.load('title.png') #게임 제목

    play = pygame.image.load('play.png')  # 플레이버튼
    exit = pygame.image.load('exit.png')  # 나가기버튼
    help = pygame.image.load('help.png')  # 도움말버튼
    story = pygame.image.load('story.png')  # 스토리버튼

    clickPlay = pygame.image.load('clickplay.png')  # 클릭한플레이버튼
    clickExit = pygame.image.load('clickexit.png')  # 클릭한나가기버튼
    clickHelp = pygame.image.load('clickhelp.png')  # 클릭한도움말버튼
    clickStory = pygame.image.load('clickstory.png')  # 클릭한스토리버튼

    helpimg = pygame.image.load('helpimg.png')        # 조작법 이미지
    storyline = pygame.image.load('storyline.png')  # 스토리라인 이미지

    character_choice_bg = pygame.image.load('characterchoicebg.png')
    fighter = pygame.image.load('player.png') # 뚠뚠 캐릭
    fighter2 = pygame.image.load('player2.png') # 마른 캐릭
    clickFighter = pygame.image.load('clickplayer.png') #클릭한 뚠뚠캐릭
    clickFighter2 = pygame.image.load('clickplayer2.png') #클릭한 마른캐릭
    missile = pygame.image.load('spoon-and-fork.png')  # Sae 미사일그림
    explosion = pygame.image.load('mouth.png') # 폭발 그림 - ho
    background = pygame.image.load('backgound2.png')  # Han
    introimage = pygame.image.load('pig.png')
    clock = pygame.time.Clock() # 시간 추척 추가 - Yu
    restart = pygame.image.load('restart.png')
    clickrestart = pygame.image.load('clickrestart.png')
    exitbottonimg = pygame.image.load('exit2.jpg')
    clearimg = pygame.image.load('couple2.jpg')
    overimg = pygame.image.load('over5.jpg')
    timeOutImage = pygame.image.load('time_out.png')

    pygame.mixer.music.load('music.mp3')  # Chan 음악 재생
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('throwing.mp3')
    gameOverSound = pygame.mixer.Sound('gameover.mp3')
    timeOutSound = pygame.mixer.Sound('gameover.mp3')
    ultSound = pygame.mixer.Sound('ult_sound.mp3')
    clickSound = pygame.mixer.Sound('click_sound.mp3')
    oversound = pygame.mixer.Sound('gameov.mp3')
    clearsound = pygame.mixer.Sound('gamecl.mp3')

    # 시간 정보
    total_time = 10
    start_ticks = pygame.time.get_ticks()

    introGame = True
    while introGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        drawObject(introimage, 0, 0)

        drawObject(title, 130, 40)

        playButton = Button2(play, 200, 400, 60, 60, clickPlay, 200, 400, 1)
        exitButton = Button2(exit, 200, 440, 60, 60, clickExit, 200, 440, 2)
        helpButton = Button2(help, 200, 480, 60, 60, clickHelp,200,480, 3)
        storyButton = Button2(story, 200, 520, 60,60, clickStory,200,520, 4)
        pygame.display.update()




def gameclear():
    clear = True

    while clear:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        drawObject(clearimg,0,0)


        replayButton = Button2(restart, 200, 400, 60, 60, clickrestart, 200, 400, 1)
        exitButton = Button2(exit, 200, 440, 60, 60, clickExit, 200, 440, 2)
        pygame.display.update()
        clock.tick(15)

def gameover(type):

    over = True

    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if type == 0:
            drawObject(overimg, 0, 0)
        else:
            drawObject(timeOutImage, 0, 0)



        replayButton = Button2(restart, 200, 400, 60, 60, clickrestart, 200, 400, 1)
        exitButton = Button2(exit, 200, 440, 60, 60, clickExit, 200, 440, 2)
        pygame.display.update()
        clock.tick(15)



def Timer():
    global total_time, start_ticks, gamePad
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    # 타이머
    font = pygame.font.Font('NEXONFootballGothicB.ttf', 25)  # 폰트 설정
    timer = font.render("timer: " + str(int(total_time - elapsed_time)), True, (255, 0, 0))
    gamePad.blit(timer, (150, 10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        timeOutSound.play()
        gameover(1)




def runGame(gametypeNum, charterNum):
    global gamepad, clock, background, fighter, fighter2, clickFighter, clickFighter2, missile, explosion, missileSound, character_choice_bg, speed, ult_times, start_ticks, total_time
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

    # # Sae 무기좌표 리스트
    # missileXY = []


    #미사일, 음식들 세팅
    missiles = pygame.sprite.Group()
    foods = pygame.sprite.Group()
    # start_ticks = pygame.time.get_ticks()

    # 점수
    score = 1
    ult_times = 3

    # 음식 랜덤 생성 - Yu
    # rock = pygame.image.load(random.choice(rockImage))
    # rockSize = rock.get_rect().size # 운석 실제 크기
    # rockWidth = rockSize[0]
    # rockHeight = rockSize[1]
    # destroySound = pygame.mixer.Sound(random.choice(explsionSound))


    # 운석 초기 위치 설정 - Yu
    # rockX = random.randrange(0, padWidth - rockWidth)
    # rockY = 0
    # rockSpeed = 2

    # 전투기 미사일에 운석이 맞았을 경우 True
    #isShot = False
    shotCount = 0
    rockPassed = 0



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
                    missile = Missile(x + fighterWidth / 2, y - fighterHeight, 10)  # x의 정 가운데에서 미사일이 나간다
                    missile.launch()
                    missiles.add(missile)  # 미사일스 에 미사일 그룹을 추가
                elif event.key == pygame.K_a:  # 궁극기 추가
                    if ult_times > 0:
                        ultSound.play()
                        for i in foods:
                            if i.add_minus_score == -2:
                                i.kill()
                        ult_times -= 1
                    else:
                        pass

                    # missileX = x + fighterWidth / 2
                    # missileY = y - fighterHeight
                    # missileXY.append([missileX, missileY]



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
         choiceCharacter("") # 없애면 안움직여서 놔둠 ㅠ


        elif gametypeNum == 1: # 캐릭터 선택이 끝난 이후


            #choiceCharacter(str(start_time))
            drawObject(background, 0, 0)  # 배경화면 그리기 -Han

            if charterNum == 1: #뚠뚠 캐릭터 선택
                drawObject(fighter, x, y)
            else: #마른 캐릭터 선택
                drawObject(fighter2, x, y-23) # 머리만 나와서 -23해서 위치 조정함


            # #미사일 오브젝트 그리기
            # if len(missileXY) != 0:
            #     for bx, by in missileXY:
            #         drawObject(missile, bx, by)
            #
            #
            # # Sae 미사일 발사 화면에 그리기
            # if len(missileXY) != 0:
            #     for i, bxy in enumerate(missileXY):  # Sae 미사일요소에 대해 반복함
            #         bxy[1] -= 10  # Sae 총알의 y좌표 -10 (위로 이동)
            #         missileXY[i][1] = bxy[1]
            #
            #         if bxy[1] < rockY:
            #             if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
            #                 missileXY.remove(bxy)
            #                 isShot = True
            #                 shotCount += 1
            #
            #         if bxy[1] <= 0:  #Sae 미사일이 화면 밖을 벗어나면
            #             try:
            #                 missileXY.remove(bxy)  #Sae 미사일 제거
            #             except:
            #                 pass


            if score < 21:  # 스피드 조절
                speed = 2

            elif score == 21:
                speed = 4
                writeMessage1("speed up!")

            elif score == 41:
                speed = 5
                writeMessage1("speed up!")




            #음식 생성되고 랜덤으로 스피드 주는 곳
            if random.randint(1, 100) == 1:
                for i in range(2):
                    food = Food(random.randint(0, padWidth - 30), 0, speed)
                    foods.add(food)



            #미사일 생성
            for missile in missiles:
                food = missile.collide(foods)
                if food: # 음식 맞추면
                    score += food.add_minus_score #좋은음식 +2, 나쁜음식 -2
                    missile.kill()
                    food.kill()
                    occur_explosion(gamePad, food.rect.x, food.rect.y)


            # 감량/증량 값이 0이면 게임오버
            if score <= 0:
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(oversound)
                gameover(0)

            if score >= 50:  #50넘었을 때 게임 클리어
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(clearsound)
                gameclear()

            # 감량/증량 점수 표시
            writeScore(score)
            writeUlt(ult_times)
            Timer()

            foods.update()
            foods.draw(gamePad)
            missiles.update()
            missiles.draw(gamePad)
            pygame.display.flip()


            #
            # rockY += rockSpeed # 운석이 아래로 떨어질 때 y좌표 증가 - Yu
            # # 운석이 지구로 떨어진 경우(화면 밖으로) - Yu
            # if rockY > padHeight:
            #     # 새로운 운석 생성(랜덤)
            #     rock = pygame.image.load(random.choice(rockImage))
            #     rockSize = rock.get_rect().size
            #     rockWidth = rockSize[0]
            #     rockHeight = rockSize[1]
            #     rockX = random.randrange(0, padWidth - rockWidth)
            #     rockY = 0
            #     rockPassed += 1

            # if rockPassed == 3: # Han 운석 3개 놓치면 게임 오버

            # Sae 놓친 운석 수 표시
            #writePassed(rockPassed)


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
            # if y < rockY + rockHeight:
            #     if (rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
            #         crash(charterNum)


            # # 운석을 맞춘 경우
            # if isShot:
            #
            #    # 운석 폭발
            #    drawObject(explosion, rockX, rockY)
            #    destroySound.play()
            #
            #    # 새로운 햣 운석(랜덤). 파괴되면 새로운 운석 생성
            #    rock = pygame.image.load(random.choice(rockImage))
            #    rockSize = rock.get_rect().size
            #    rockWidth = rockSize[0]
            #    rockHeight = rockSize[1]
            #    rockX = random.randrange(0, padWidth - rockWidth)
            #    rockY = 0
            #    destroySound = pygame.mixer.Sound(random.choice(explsionSound))
            #    isShot = False
            #
            #    # Han 운석 맞추면 속도 증가
            #    rockSpeed += 0.02
            #    if rockSpeed >= 10:
            #        rockSpeed = 10


            #drawObject(rock, rockX, rockY)  # 장애물 그리기

            pygame.display.update() #게임화면을 다시 그림 -Han
            clock.tick(60) # 게임화면의 초당 프레임수를 60으로 설정 - Yu

    pygame.quit() # pygame 종료 - Yu

initGame()
runGame(0, 0)

