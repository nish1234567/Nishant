import pygame
import random
import os

pygame.mixer.init()
pygame.init()

#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#create window
screen_width=900
screen_height=600
game_window=pygame.display.set_mode((screen_width,screen_height))

#Background image
bgimg=pygame.image.load("img2.jpeg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

#Game title
pygame.display.set_caption("Saanp Ka Khel")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])
    
def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])
        
def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill((233,210,229))
        #text_screen("Welcome To Snake World",black,200,245)
        text_screen("Press space Bar To Play",black,215,285)
        text_screen("Snake By Nishant",black,243,205)
        
        for event in pygame.event.get():
            if event.type==pygame.quit:
                exit_game=True
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('bg.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
#Game loop
def gameloop():
    #Game specific variables
    exit_game= False
    game_over= False
    snake_x=70
    snake_y=90
    snake_size= 10
    fps=30
    velocity_x=0
    velocity_y=0
    init_velocity=5
    #init_velocity=5
    score=0
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    snk_list=[]
    snk_length=1
    #Check if hiscore file exists
    if(not os.path.exists("highscore.txt")):
        with open("hiscore.txt","w")as f:
            f.write("0")
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
    while not exit_game:
            if game_over:
                with open("hiscore.txt","w")as f:
                    f.write(str(hiscore))
                    game_window.fill((200,250,233))
                
                text_screen("Game Over! Press Enter To Continue",red,100,200)
                text_screen("Your Score Is :"+str(hiscore),red,255,250)
                
                        
                for event in pygame.event.get():
                    if event.type==pygame.quit:
                        exit_game = True
                            
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            welcome()
            else:
                for event in pygame.event.get():
                    if event.type==pygame.quit:
                        exit_game=True
                            
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            velocity_x=init_velocity
                            velocity_y=0
                            
                        if event.key==pygame.K_LEFT:
                                velocity_x= -init_velocity
                                velocity_y=0
                                
                        if event.key==pygame.K_UP:
                            velocity_y=-init_velocity
                            velocity_x=0
                                
                        if event.key==pygame.K_DOWN:
                            velocity_y=init_velocity
                            velocity_x=0

                        if event.key==pygame.K_n:
                            score+=10

                        if event.key==pygame.K_s:
                            score-=10
                            
                snake_x=snake_x+velocity_x
                snake_y=snake_y+velocity_y

                if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                    score+=10
                    food_x=random.randint(20,screen_width/2)
                    food_y=random.randint(20,screen_height/2)
                    snk_length+=5
                    if score>int(hiscore):
                        hiscore=score
                    
                game_window.fill((233,210,229))
                game_window.blit(bgimg,(0,0))
                text_screen("score:"+ str(score)+"  Hiscore:  "+str(hiscore),red,7,7)    
                pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
                    
                head=[]
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
                    
                if len(snk_list)>snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_over=True
                        
                    #game over music
                    pygame.mixer.music.load("end.mp3")
                    pygame.mixer.music.play()
                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                        game_over=True
                        pygame.mixer.music.load("end.mp3")
                        pygame.mixer.music.play()
                plot_snake(game_window,black,snk_list,snake_size)
            pygame.display.update()
            clock.tick(fps)
    pygame.quit()
    quit()
welcome()
