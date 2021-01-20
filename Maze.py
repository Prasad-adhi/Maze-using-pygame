import pygame
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def game():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    polygon=[]
    polygon.append(Polygon([(255,0),(265,0),(265,100),(255,100)]))
    polygon.append(Polygon([(230,97),(300,97),(300,110),(230,110)]))
    polygon.append(Polygon([(225,30),(240,30),(240,100),(225,100)]))
    polygon.append(Polygon([(202,0),(215,0),(215,60),(202,60)]))
    polygon.append(Polygon([(40,75),(230,75),(230,93),(40,93)]))
    polygon.append(Polygon([(173,40),(192,40),(192,90),(173,90)]))
    polygon.append(Polygon([(135,0),(150,0),(150,60),(135,60)]))
    polygon.append(Polygon([(35,30),(50,30),(50,80),(35,80)]))
    polygon.append(Polygon([(35,30),(85,30),(85,40),(35,40)]))
    polygon.append(Polygon([(0,127),(205,127),(205,140),(0,140)]))
    polygon.append(Polygon([(201,130),(215,130),(215,380),(201,380)]))
    polygon.append(Polygon([(40,165),(160,165),(160,180),(40,180)]))
    polygon.append(Polygon([(155,170),(170,170),(170,240),(155,240)]))
    polygon.append(Polygon([(75,235),(170,235),(170,250),(75,250)]))
    polygon.append(Polygon([(35,170),(50,170),(50,295),(35,295)]))
    polygon.append(Polygon([(40,290),(160,290),(160,305),(40,305)]))
    polygon.append(Polygon([(153,295),(170,295),(170,435),(153,435)]))
    polygon.append(Polygon([(160,430),(460,430),(460,445),(160,445)]))
    polygon.append(Polygon([(112,350),(130,350),(130,500),(112,500)]))
    polygon.append(Polygon([(45,345),(120,345),(120,360),(45,360)]))
    polygon.append(Polygon([(45,345),(60,345),(60,445),(45,445)]))
    polygon.append(Polygon([(345,435),(360,435),(360,500),(345,500)]))
    polygon.append(Polygon([(200,362),(240,362),(240,380),(200,380)]))
    polygon.append(Polygon([(235,280),(250,280),(250,380),(235,380)]))
    polygon.append(Polygon([(235,270),(300,270),(300,290),(235,290)]))
    polygon.append(Polygon([(300,213),(315,213),(315,290),(300,290)]))
    polygon.append(Polygon([(300,213),(385,213),(385,230),(300,230)]))
    polygon.append(Polygon([(225,213),(272,213),(272,230),(225,230)]))
    polygon.append(Polygon([(225,180),(240,180),(240,220),(225,220)]))
    polygon.append(Polygon([(225,175),(330,175),(330,190),(225,190)]))
    polygon.append(Polygon([(325,70),(340,70),(340,190),(325,190)]))
    polygon.append(Polygon([(285,65),(460,65),(460,80),(285,80)]))
    polygon.append(Polygon([(285,35),(300,35),(300,70),(285,70)]))
    polygon.append(Polygon([(335,35),(500,35),(500,50),(335,50)]))
    polygon.append(Polygon([(395,65),(410,65),(410,405),(395,405)]))
    polygon.append(Polygon([(395,395),(460,395),(460,410),(395,410)]))
    polygon.append(Polygon([(380,217),(400,217),(400,230),(395,230)]))
    polygon.append(Polygon([(425,195),(440,195),(440,400),(425,400)]))
    polygon.append(Polygon([(425,195),(460,195),(460,210),(425,210)]))
    polygon.append(Polygon([(455,345),(500,345),(500,360),(455,360)]))
    polygon.append(Polygon([(450,315),(470,315),(470,360),(450,360)]))
    polygon.append(Polygon([(425,145),(500,145),(500,160),(425,160)]))
    polygon.append(Polygon([(425,105),(440,105),(440,150),(425,150)]))
    polygon.append(Polygon([(425,105),(460,105),(460,120),(425,120)]))
    polygon.append(Polygon([(350,145),(360,145),(360,290),(350,290)]))
    polygon.append(Polygon([(350,145),(385,145),(385,160),(350,160)]))
    polygon.append(Polygon([(367,105),(385,105),(385,150),(367,150)]))
    polygon.append(Polygon([(335,105),(357,105),(357,120),(335,120)]))
    polygon.append(Polygon([(265,315),(280,315),(280,435),(265,435)]))
    polygon.append(Polygon([(265,315),(330,315),(330,330),(265,330)]))
    polygon.append(Polygon([(325,285),(340,285),(340,380),(325,380)]))
    polygon.append(Polygon([(305,375),(380,375),(380,390),(305,390)]))
    polygon.append(Polygon([(365,305),(380,305),(380,380),(365,380)]))

    def point_in_polygon(x,y):
        point=Point(x,y)
        for i in range(len(polygon)):
            if(polygon[i].contains(point)):
                return True
        return False

    done = False
    is_blue = False
    x=250
    y=11
    
    while not done:
            for event in pygame.event.get():
                color=(255, 100, 0)
                if event.type == pygame.QUIT:
                    done = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: 
                if y>10 and not point_in_polygon(x,y-3):
                    y -= 3
                #print(x,' ',y)
            if pressed[pygame.K_DOWN]:
                if y+3<485 and not point_in_polygon(x,y+3): 
                    y += 3
                #print(x,' ',y)
            if pressed[pygame.K_LEFT]:
                if x>10 and not point_in_polygon(x-3,y): 
                    x -= 3
                #print(x,' ',y)
            if pressed[pygame.K_RIGHT]: 
                if x+3<485 and not point_in_polygon(x+3,y):
                    x += 3
                #print(x,' ',y)
            
            point=Point(x,y)
            finish=Polygon([(330, 470), (350, 470), (350, 490), (330, 490)])
            if(finish.contains(point)):
                done=True
                
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
            
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, 10, 500))#box starting on (0,0) strecthing the entire y axis
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, 500, 10))#box starting on (0,0) strecthing the entire x axis
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 490, 500, 10))#box starting on (0,490) strecthing the entire x axis
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(490, 0, 10, 500))#box starting on (490,0) strecthing the entire y axis
            
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(260, 0, 10, 100))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(230, 100, 70, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(230, 30, 10, 70))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(205, 0, 10, 60))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 80, 190, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(180, 40, 10, 50))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(140, 0, 10, 60))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 35, 10, 45))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 35, 50, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 130, 205, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(205, 130, 10, 250))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 170, 120, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(160, 170, 10, 70))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(80, 240, 90, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 170, 10, 125))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 295, 120, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(160, 295, 10, 140))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(160, 435, 300, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(120, 350, 10, 150))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(50, 350, 70, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(50, 350, 10, 90))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(85, 390, 10, 110))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(350, 435, 10, 65))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(205, 370, 35, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(240, 280, 10, 100))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(240, 280, 65, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(305, 220, 10, 70))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(305, 220, 80, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(230, 220, 40, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(230, 180, 10, 40))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(230, 180, 100, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(330, 70, 10, 120))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(290, 70, 170, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(290, 40, 10, 30))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(340, 40, 160, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(400, 70, 10, 330))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(400, 400, 60, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(380, 220, 20, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(430, 200, 10, 200))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(430, 200, 30, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(460, 350, 40, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(460, 320, 10, 30))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(430, 150, 70, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(430, 110, 10, 40))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(430, 110, 30, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(355, 150, 10, 140))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(355, 150, 30, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(375, 110, 10, 40))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(340, 110, 17, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(270, 320, 10, 115))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(270, 320, 60, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(330, 290, 10, 90))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(310, 380, 70, 10))
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(370, 310, 10, 70))

            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(330, 470, 20, 20))
            pygame.display.flip()
            clock.tick(60)

game()