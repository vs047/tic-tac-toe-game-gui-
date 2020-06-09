import pygame
import random
import pymongo
obj=pymongo.MongoClient("localhost",27017)
db=obj.stats
pygame.init()
font1=pygame.font.SysFont(pygame.font.get_fonts()[1],20,False,False)
font2=pygame.font.SysFont(pygame.font.get_fonts()[2],30,True,False)
screen_width,screen_height=600,600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic Tac Toe")
class game:
    @staticmethod
    def checkpoint(movesused,moveused2):
        if ((3*screen_width//20,7*screen_height//60) in movesused and (screen_width//3+(3*screen_width//20),7*screen_height//60) in movesused and (2*screen_width//3+(3*screen_width//20),7*screen_height//60) in movesused) or ((90,screen_height//4+(7*screen_height//60)) in movesused and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in movesused) or ((90,screen_height//2+(7*screen_height//60)) in movesused and (screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in movesused):
            return True
        elif ((3*screen_width//20,7*screen_height//60) in movesused and (3*screen_width//20,screen_height//4+(7*screen_height//60)) in movesused and (3*screen_width//20,screen_height//2+(7*screen_height//60)) in movesused) or ((screen_width//3+(3*screen_width//20),7*screen_height//60) in movesused and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in movesused and (screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in movesused) or ((2*screen_width//3+(3*screen_width//20),7*screen_height//60) in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in movesused):
            return True
        elif ((3*screen_width//20,7*screen_height//60) in movesused and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in movesused) or ((3*screen_width//20,screen_height//2+(7*screen_height//60)) in movesused and  (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in movesused and (2*screen_width//3+(3*screen_width//20),7*screen_height//60) in movesused):
            return True
        elif ((3*screen_width//20,7*screen_height//60) in moveused2 and (screen_width//3+(3*screen_width//20),7*screen_height//60) in moveused2 and (2*screen_width//3+(3*screen_width//20),7*screen_height//60) in moveused2) or ((90,screen_height//4+(7*screen_height//60)) in moveused2 and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in moveused2 and (2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in moveused2) or ((90,screen_height//2+(7*screen_height//60)) in moveused2 and (screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in moveused2 and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in moveused2):
            return False
        elif ((3*screen_width//20,7*screen_height//60) in moveused2 and (3*screen_width//20,screen_height//4+(7*screen_height//60)) in moveused2 and (3*screen_width//20,screen_height//2+(7*screen_height//60)) in moveused2) or ((screen_width//3+(3*screen_width//20),7*screen_height//60) in moveused2 and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in moveused2 and (screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in moveused2) or ((2*screen_width//3+(3*screen_width//20),7*screen_height//60) in moveused2 and (2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in moveused2 and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in moveused2):
            return False
        elif ((3*screen_width//20,7*screen_height//60) in moveused2 and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in moveused2 and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) in moveused2) or ((3*screen_width//20,screen_height//2+(7*screen_height//60)) in moveused2 and  (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) in moveused2 and (2*screen_width//3+(3*screen_width//20),7*screen_height//60) in moveused2):
            return False
    @staticmethod
    def gameloop():
        movesused=[]
        moveused2=[]
        start=True
        exit_game=False
        computer=False
        multiplayer=False
        mode=False
        totalgames,wins,defeat=0,0,0
        gameplay=False
        chance=0
        stats=False
        actions={"PLAY":(5*screen_width//12,5*screen_height//12,screen_width//6,screen_height//12),"STATS":(5*screen_width//12,7*screen_height//12,screen_width//6+10,screen_height//12),"EXIT":(5*screen_width//12,9*screen_height//12,screen_width//6,screen_height//12)}
        image1=pygame.image.load("94455342-xo-neon-sign-a-purple-background-valentines-background-3d-rendering.png")
        image1=pygame.transform.scale(image1,(screen_width,screen_height))
        image2=pygame.image.load("376-3762235_tic-tac-toe-game-vector-tic-tac-toe.png")
        image2=pygame.transform.scale(image2,(400,250))
        choices={1:(3*screen_width//20,7*screen_height//60),2:(screen_width//3+(3*screen_width//20),7*screen_height//60),3:(2*screen_width//3+(3*screen_width//20),7*screen_height//60),4:(90,screen_height//4+(7*screen_height//60)),5:(screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)),6:(2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)),7:(90,screen_height//2+(7*screen_height//60)),8:(screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)),9:(2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60))}
        x=None
        while not(exit_game):
            if start:
                screen.fill((0,0,0))
                screen.blit(image2,(80,-20))
                for i in actions:
                    pygame.draw.rect(screen,(255,0,0),actions[i])
                if actions["PLAY"][0]<=pygame.mouse.get_pos()[0]<=actions["PLAY"][0]+actions["PLAY"][2] and actions["PLAY"][1]<=pygame.mouse.get_pos()[1]<=actions["PLAY"][1]+actions["PLAY"][3]:
                    pygame.draw.rect(screen,(0,0,255),actions["PLAY"])
                elif actions["STATS"][0]<=pygame.mouse.get_pos()[0]<=actions["STATS"][0]+actions["STATS"][2] and actions["STATS"][1]<=pygame.mouse.get_pos()[1]<=actions["STATS"][1]+actions["STATS"][3]:
                    pygame.draw.rect(screen,(0,0,255),actions["STATS"])
                elif actions["EXIT"][0]<=pygame.mouse.get_pos()[0]<=actions["EXIT"][0]+actions["EXIT"][2] and actions["EXIT"][1]<=pygame.mouse.get_pos()[1]<=actions["EXIT"][1]+actions["EXIT"][3]:
                    pygame.draw.rect(screen,(0,0,255),actions["EXIT"])
                for i in actions:
                    text1=font2.render(i,1,(255,255,255))
                    screen.blit(text1,(actions[i][0]+2,actions[i][1]+5))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if actions["PLAY"][0]<=pygame.mouse.get_pos()[0]<=actions["PLAY"][0]+actions["PLAY"][2] and actions["PLAY"][1]<=pygame.mouse.get_pos()[1]<=actions["PLAY"][1]+actions["PLAY"][3]:
                            start=False
                            mode=True
                        elif actions["STATS"][0]<=pygame.mouse.get_pos()[0]<=actions["STATS"][0]+actions["STATS"][2] and actions["STATS"][1]<=pygame.mouse.get_pos()[1]<=actions["STATS"][1]+actions["STATS"][3]:
                            stats=True
                            start=False
                        elif actions["EXIT"][0]<=pygame.mouse.get_pos()[0]<=actions["EXIT"][0]+actions["EXIT"][2] and actions["EXIT"][1]<=pygame.mouse.get_pos()[1]<=actions["EXIT"][1]+actions["EXIT"][3]:
                            exit_game=True
            elif stats:
                screen.fill((0,0,0))
                pygame.draw.rect(screen,(255,0,0),(5*screen_width//12,5*screen_height//6,screen_width//6,screen_height//12))
                pygame.draw.rect(screen,(255,0,0),(5*screen_width//6-30,5*screen_height//6,screen_width//6,screen_height//12))
                database=db.performance.find()
                for i in database:
                    text1=font1.render("total matches:=>{}".format(int(i["total games"])),1,(255,255,255))
                    screen.blit(text1,(5*screen_width//12,5*screen_width//12))
                    text1=font1.render("matches won:=>{}".format(int(i["wins"])),1,(255,255,255))
                    screen.blit(text1,(5*screen_width//12,6*screen_width//12))
                    text1=font1.render("matches lost:=>{}".format(int(i["defeat"])),1,(255,255,255))
                    screen.blit(text1,(5*screen_width//12,7*screen_width//12))
                if 5*screen_width//12<=pygame.mouse.get_pos()[0]<=5*screen_width//12+screen_width//6 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                    pygame.draw.rect(screen,(0,0,255),(5*screen_width//12,5*screen_height//6,screen_width//6,screen_height//12))
                elif 5*screen_width//6<=pygame.mouse.get_pos()[0]<=5*screen_width//6+2*screen_width//15 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                    pygame.draw.rect(screen,(0,0,255),(5*screen_width//6-30,5*screen_height//6,screen_width//6,screen_height//12))
                text1=font2.render("BACK",1,(255,255,255))
                screen.blit(text1,(5*screen_width//12+10,5*screen_height//6+4))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if 5*screen_width//12<=pygame.mouse.get_pos()[0]<=5*screen_width//12+screen_width//6 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                            stats=False
                            start=True
                        elif 5*screen_width//6<=pygame.mouse.get_pos()[0]<=5*screen_width//6+2*screen_width//15 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                            db.performance.update_one({"_id":1},{"$set": {"total games":0,"wins":0,"defeat":0}})
                text1=font2.render("RESET",1,(255,255,255))
                screen.blit(text1,(5*screen_width//6-30,5*screen_height//6+3))
            elif mode:
                screen.blit(image1,(0,0))
                pygame.draw.rect(screen,(184,176,155),(screen_width//6,5*screen_height//6,screen_width//3,screen_height//12))
                pygame.draw.rect(screen,(184,176,155),(4*screen_width//6,5*screen_height//6,screen_width//4,screen_height//12))
                if screen_width//6<=pygame.mouse.get_pos()[0]<=screen_width//6+screen_width//3 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                    pygame.draw.rect(screen,(205,127,50),(screen_width//6,5*screen_height//6,screen_width//3,screen_height//12))
                elif 4*screen_width//6<=pygame.mouse.get_pos()[0]<=4*screen_width//6+screen_width//4 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                    pygame.draw.rect(screen,(205,127,50),(4*screen_width//6,5*screen_height//6,screen_width//4,screen_height//12))
                text1=font1.render("MULTIPLAYER",1,(0,0,0))
                screen.blit(text1,(screen_width//6+5,5*screen_width//6+5))
                text1=font1.render("COMPUTER",1,(0,0,0))
                screen.blit(text1,(2*screen_width//3+5,5*screen_width//6+5))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if screen_width//6<=pygame.mouse.get_pos()[0]<=screen_width//6+screen_width//3 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                            multiplayer=True
                            mode=False
                            gameplay=True
                        elif 4*screen_width//6<=pygame.mouse.get_pos()[0]<=4*screen_width//6+screen_width//4 and 5*screen_height//6<=pygame.mouse.get_pos()[1]<=5*screen_height//6+screen_height//12:
                            computer=True
                            mode=False
                            gameplay=True
            elif gameplay:
                screen.fill((255,255,255))
                pygame.draw.line(screen,(0,0,0),(screen_width//3,0),(screen_width//3,3*screen_height//4),5)
                pygame.draw.line(screen,(0,0,0),(2*screen_width//3,0),(2*screen_width//3,3*screen_height//4),5)
                pygame.draw.line(screen,(0,0,0),(0,screen_height//4),(screen_width,screen_height//4),5)
                pygame.draw.line(screen,(0,0,0),(0,screen_height//2),(screen_width,screen_height//2),5)
                pygame.draw.rect(screen,(0,0,0),(0,3*screen_height//4,screen_width,screen_height//4))
                x=game.checkpoint(movesused,moveused2)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN and chance==9:
                            screen.fill((255,255,255))
                            movesused=[]
                            moveused2=[]
                            if x==True and computer:
                                db.performance.update_one({"_id":1},{ '$inc':{"total games":1}})
                                db.performance.update_one({"_id":1},{ '$inc':{"wins":1}})
                            elif x==False and computer:
                                db.performance.update_one({"_id":1},{ '$inc':{"total games":1}})
                                db.performance.update_one({"_id":1},{ '$inc':{"defeat":1}})
                            elif chance==9 and computer:
                                db.performance.update_one({"_id":1},{ '$inc':{"total games":1}})
                            chance=0
                            x=None
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if x==None:
                            if 0<=pygame.mouse.get_pos()[0]<=screen_width//3 and 0<=pygame.mouse.get_pos()[1]<=screen_height//4:
                                if (3*screen_width//20,7*screen_height//60) not in movesused and (3*screen_width//20,7*screen_height//60) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((3*screen_width//20,7*screen_height//60))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((3*screen_width//20,7*screen_height//60))
                                    chance+=1
                            elif screen_width//3+1<=pygame.mouse.get_pos()[0]<=2*screen_width//3 and 0<=pygame.mouse.get_pos()[1]<=screen_height//4:
                                if (screen_width//3+(3*screen_width//20),7*screen_height//60) not in movesused and (screen_width//3+(3*screen_width//20),7*screen_height//60) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((screen_width//3+(3*screen_width//20),7*screen_height//60))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((screen_width//3+(3*screen_width//20),7*screen_height//60))
                                    chance+=1
                            elif 2*screen_width//3+1<=pygame.mouse.get_pos()[0]<=screen_width and 0<=pygame.mouse.get_pos()[1]<=screen_height//4:
                                if (2*screen_width//3+(3*screen_width//20),7*screen_height//60) not in movesused and (2*screen_width//3+(3*screen_width//20),7*screen_height//60) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((2*screen_width//3+(3*screen_width//20),7*screen_height//60))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((2*screen_width//3+(3*screen_width//20),7*screen_height//60))
                                    chance+=1
                            elif 0<=pygame.mouse.get_pos()[0]<=screen_width//3 and screen_height//4+1<=pygame.mouse.get_pos()[1]<=screen_height//2:
                                if (90,screen_height//4+(7*screen_height//60)) not in movesused and (90,screen_height//4+(7*screen_height//60)) not in moveused2:
                                    if chance%2==0: 
                                        movesused.append((90,screen_height//4+(7*screen_height//60)))
                                    elif chance%2!=0 and multiplayer: 
                                        moveused2.append((90,screen_height//4+(7*screen_height//60)))
                                    chance+=1
                            elif screen_width//3+1<=pygame.mouse.get_pos()[0]<=2*screen_width//3 and screen_height//4+1<=pygame.mouse.get_pos()[1]<=screen_height//2:
                                if (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) not in movesused and (screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)))
                                    chance+=1
                            elif 2*screen_width//3+1<=pygame.mouse.get_pos()[0]<=screen_width and screen_height//4+1<=pygame.mouse.get_pos()[1]<=screen_height//2:
                                if (2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) not in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((2*screen_width//3+(3*screen_width//20),screen_height//4+(7*screen_height//60)))
                                    chance+=1    
                            elif 0<=pygame.mouse.get_pos()[0]<=screen_width//3 and screen_height//2+1<=pygame.mouse.get_pos()[1]<=3*screen_height//4:
                                if (90,screen_height//2+(7*screen_height//60)) not in movesused and (90,screen_height//2+(7*screen_height//60)) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((90,screen_height//2+(7*screen_height//60)))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((90,screen_height//2+(7*screen_height//60)))
                                    chance+=1
                            elif screen_width//3+1<=pygame.mouse.get_pos()[0]<=2*screen_width//3 and screen_height//2+1<=pygame.mouse.get_pos()[1]<=3*screen_height//4:
                                if (screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) not in movesused and (screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)))
                                    chance+=1
                            elif 2*screen_width//3+1<=pygame.mouse.get_pos()[0]<=screen_width and screen_height//2+1<=pygame.mouse.get_pos()[1]<=3*screen_height//4:
                                if (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) not in movesused and (2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)) not in moveused2:
                                    if chance%2==0:
                                        movesused.append((2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)))
                                    elif chance%2!=0 and multiplayer:
                                        moveused2.append((2*screen_width//3+(3*screen_width//20),screen_height//2+(7*screen_height//60)))
                                    chance+=1
                if chance%2!=0 and x==None and chance!=9 and computer==True:
                    num=random.randint(1,9)
                    while choices[num] in movesused or choices[num] in moveused2:
                        num=random.randint(1,9)
                    moveused2.append(choices[num])
                    chance+=1
                if x:
                    text1=font1.render("Player 1 wins",1,(255,255,255))
                    chance=9
                elif x==False:
                    text1=font1.render("Player 2 wins",1,(255,255,255))
                    chance=9
                elif chance%2==0:
                    text1=font1.render("Player 1 turn",1,(255,255,255))
                elif chance%2!=0:
                    if chance==9:
                        text1=font1.render("Tie Game",1,(255,255,255))
                    else:
                        text1=font1.render("Player 2 turn",1,(255,255,255))
                screen.blit(text1,(screen_width//3,5*screen_height//6))
                for i in movesused:
                    pygame.draw.circle(screen,(0,0,50),i,60,4)
                for i in moveused2:
                    pygame.draw.line(screen,(150,0,0),(i[0]-90,i[1]-60),(i[0]+110,i[1]+70),4)
                    pygame.draw.line(screen,(150,0,0),(i[0]-90,i[1]+70),(i[0]+110,i[1]-60),4)
            pygame.display.update()
        pygame.quit()

game.gameloop()
