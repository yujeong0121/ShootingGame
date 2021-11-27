
import pygame
import sys
from time import sleep



padWidth = 480 # 게임화면의 가로크기
padHeight = 640 # 게임화면의 세로크기



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
    pygame.init()   #Han
    gamePad = pygame #Han

    missile = pygame.image.load('spoon-and-fork.png') # Sae 미사일그림







def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound

    # Sae 무기좌표 리스트
    missileXY = []



    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in  [pygame.QUIT]: #게임 프로그램 종료
                pygame.quit()
                sys.exit()
        drawObject(background, 0, 0) #배경화면 그리기 -Han
        pygame.display.update() #게임화면을 다시 그림 -Han

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
