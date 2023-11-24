import pygame 

pygame.init()


#화면 크기 설정
screen_width = 1024 #가로 크기
screen_height = 1024#세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Title")
background = pygame.image.load("/Users/choi/Downloads/preview.jpg")

#캐릭터 불러오기
character = pygame.image.load("/Users/choi/Downloads/zo.png")
character_size = character.get_rect().size #캐릭터 이미지 사이즈 구하기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
#캐릭터의 기준 좌표를 캐릭터의 왼쪽 상단으로 둔다.
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반의 중간에 위치. 좌우로 움직이는 변수
character_y_pos = screen_height - character_height #이미지가 화면 세로의 가장 아래 위치

#캐릭터 이동 좌표
to_x = 0
to_y = 0

#FPS 설정
clock = pygame.time.Clock()

#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running:
    dt = clock.tick(60) #초당 프레임 수 fps 설정
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False
    
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT:
            to_x -= 0.3
        elif event.key == pygame.K_RIGHT:
            to_x += 0.3
        elif event.key == pygame.K_DOWN:
            to_y += 0.3
        elif event.key == pygame.K_UP:
            to_y -= 0.3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    print(character_x_pos)#50
    print(character_y_pos)#425
    # print(screen_width)#600
    # print(screen_height)#800
    print(character_width,'폭')#500
    print(character_height,'높이')#375
    

    #왼쪽, 오른쪽 경계 정하기
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #위, 아래쪽 경계 정하기
    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.fill((0,255,224))
    screen.blit(character, (character_x_pos, character_y_pos)) #배경에 캐릭터 그려주기
    pygame.display.update()





#pygame 종료
pygame.quit()



