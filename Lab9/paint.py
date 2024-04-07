import pygame
import math
pygame.init()
def main():
    # Set up the Pygame screen
    screen=pygame.display.set_mode((700,600))
    pygame.display.set_caption("Drawing with Pygame")
    clock=pygame.time.Clock()
    FPS=60
    # Define color constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # Variables to control drawing modes
    drawing = False
    draw=False
    square=False
    rtriangle=False
    etriangle=False
    rhombus=False
    # Initialize variables for drawing
    last_pos = None
    color = WHITE
    brush_size = 5
    # Define rectangles for color palette and drawing mode buttons
    regim=[pygame.Rect(287+i*65,10,55,50) for i in range(6)]
    block = [pygame.Rect(10+j,10+i*20,1,10) for i in range(3) for j in range (256)]
    color1=[(0,0,i)for i in range(256)]
    colregim=[(255,255,255)for i in range(6)]
    for i in range(256):
        color1.append((0,i,0))
    for i in range(256):
        color1.append((i,0,0))
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = event.pos
                if event.button == 1 and draw==True:
                    drawing=True  
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and draw==True:  # Left mouse button
                    drawing = False
                    # Add similar logic for other shapes (right triangle, equilateral triangle, rhombus)
                elif event.button == 1 and square==True:  # Left mouse button
                    if abs(last_pos[0]-event.pos[0])>abs(last_pos[1]-event.pos[1]):
                        sqw=abs(last_pos[1]-event.pos[1])
                    else:
                        sqw=abs(last_pos[0]-event.pos[0])
                    if(last_pos[0]<event.pos[0] and last_pos[1]<event.pos[1]):
                        pygame.draw.rect(screen,color,(last_pos[0],last_pos[1],sqw,sqw))
                    elif(last_pos[0]<event.pos[0] and last_pos[1]>event.pos[1]):
                        pygame.draw.rect(screen,color,(last_pos[0],last_pos[1]-sqw,sqw,sqw))
                    elif(last_pos[0]>event.pos[0] and last_pos[1]<event.pos[1]):
                        pygame.draw.rect(screen,color,(last_pos[0]-sqw,last_pos[1],sqw,sqw))
                    else:
                        pygame.draw.rect(screen,color,(last_pos[0]-sqw,last_pos[1]-sqw,sqw,sqw))
                elif event.button == 1 and rtriangle==True:  # Left mouse button
                    if abs(last_pos[0]-event.pos[0])>abs(last_pos[1]-event.pos[1]):
                        sqw=abs(last_pos[1]-event.pos[1])
                    else:
                        sqw=abs(last_pos[0]-event.pos[0])
                    if(last_pos[0]<event.pos[0] and last_pos[1]<event.pos[1]):
                        points = [(last_pos[0], last_pos[1]),
                            (last_pos[0] + sqw, last_pos[1]),
                            (last_pos[0], last_pos[1] + sqw)]
                        pygame.draw.polygon(screen, color, points)
                    elif(last_pos[0]<event.pos[0] and last_pos[1]>event.pos[1]):
                        points = [(last_pos[0], last_pos[1]),
                            (last_pos[0] + sqw, last_pos[1]),
                            (last_pos[0], last_pos[1] - sqw)]
                        pygame.draw.polygon(screen, color, points)
                    elif(last_pos[0]>event.pos[0] and last_pos[1]<event.pos[1]):
                        points = [(last_pos[0], last_pos[1]),
                            (last_pos[0] - sqw, last_pos[1]),
                            (last_pos[0], last_pos[1] + sqw)]
                        pygame.draw.polygon(screen, color, points)
                    else:
                        points = [(last_pos[0], last_pos[1]),
                            (last_pos[0] - sqw, last_pos[1]),
                            (last_pos[0], last_pos[1] - sqw)]
                        pygame.draw.polygon(screen, color, points)
                elif event.button == 1 and etriangle==True:  # Left mouse button
                    if abs(last_pos[0]-event.pos[0])>abs(last_pos[1]-event.pos[1]):
                        sqw=abs(last_pos[1]-event.pos[1])
                    else:
                        sqw=abs(last_pos[0]-event.pos[0])
                    triangle_height=math.sqrt(3) / 2 * sqw
                    if(last_pos[0]<event.pos[0] and last_pos[1]<event.pos[1]):
                        points = [(last_pos[0]+sqw/2, last_pos[1]),
                                (last_pos[0], last_pos[1] + triangle_height),
                                (last_pos[0] + sqw, last_pos[1] + triangle_height)]
                        pygame.draw.polygon(screen, color, points)
                    elif(last_pos[0]<event.pos[0] and last_pos[1]>event.pos[1]):
                        points = [(last_pos[0]+sqw/2, last_pos[1]-triangle_height),
                                (last_pos[0], last_pos[1]),
                                (last_pos[0] + sqw, last_pos[1])]
                        pygame.draw.polygon(screen, color, points)
                    elif(last_pos[0]>event.pos[0] and last_pos[1]<event.pos[1]):
                        points = [(last_pos[0]-sqw/2, last_pos[1]),
                                (last_pos[0], last_pos[1] + triangle_height),
                                (last_pos[0] - sqw, last_pos[1] + triangle_height)]
                        pygame.draw.polygon(screen, color, points)
                    else:
                        points = [(last_pos[0]-sqw/2, last_pos[1]-triangle_height),
                                (last_pos[0], last_pos[1]),
                                (last_pos[0] - sqw, last_pos[1])]
                        pygame.draw.polygon(screen, color, points) 
                elif event.button == 1 and rhombus==True:  # Left mouse button
                    if abs(last_pos[0]-event.pos[0])>abs(last_pos[1]-event.pos[1]):
                        sqw=abs(last_pos[1]-event.pos[1])
                    else:
                        sqw=abs(last_pos[0]-event.pos[0])
                    if(last_pos[0]<event.pos[0] and last_pos[1]<event.pos[1]):
                        points = [(last_pos[0]+sqw/2, last_pos[1]),
                                (last_pos[0]+sqw, last_pos[1]+sqw/2),
                                (last_pos[0] + sqw/2, last_pos[1]+sqw),
                                (last_pos[0],last_pos[1]+sqw/2)]
                        pygame.draw.polygon(screen, color, points)
                    elif(last_pos[0]<event.pos[0] and last_pos[1]>event.pos[1]):
                        points = [(last_pos[0]+sqw/2, last_pos[1]-sqw),
                                (last_pos[0]+sqw, last_pos[1]-sqw/2),
                                (last_pos[0] + sqw/2, last_pos[1]),
                                (last_pos[0],last_pos[1]-sqw/2)]
                        pygame.draw.polygon(screen, color, points)
                    elif(last_pos[0]>event.pos[0] and last_pos[1]<event.pos[1]):
                        points = [(last_pos[0]-sqw/2, last_pos[1]),
                                (last_pos[0], last_pos[1]+sqw/2),
                                (last_pos[0] - sqw/2, last_pos[1]+sqw),
                                (last_pos[0]-sqw,last_pos[1]+sqw/2)]
                        pygame.draw.polygon(screen, color, points)
                    else:
                        points = [(last_pos[0]-sqw/2, last_pos[1]-sqw),
                                (last_pos[0], last_pos[1]-sqw/2),
                                (last_pos[0] - sqw/2, last_pos[1]),
                                (last_pos[0]-sqw,last_pos[1]-sqw/2)]
                        pygame.draw.polygon(screen, color, points)  
            elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pos()[1]>80:
                if drawing:
                    new_pos = event.pos
                    pygame.draw.line(screen, color, last_pos, new_pos, brush_size)
                    last_pos = new_pos
                    # If mouse movement occurs within the drawing area, and drawing mode is enabled, draw
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                elif event.key == pygame.K_w:
                    color = WHITE
                elif event.key == pygame.K_k:
                    color = BLACK
                elif event.key == pygame.K_UP:
                    brush_size += 1
                elif event.key == pygame.K_DOWN:
                    brush_size = max(1, brush_size - 1)
        [pygame.draw.rect(screen, color1[i],block1) for i,block1 in enumerate (block)]
        [pygame.draw.rect(screen, colregim[i],j) for i,j in enumerate (regim)]
        mouse_button=pygame.mouse.get_pressed()
        pos=pygame.mouse.get_pos()
        # Check for button clicks and change drawing mode accordingly
        if mouse_button[0] and pos[0]>352 and pos[1]>10 and pos[0]<407 and pos[1]<60:
            draw=True
            square=False
            rtriangle=False
            etriangle=False
            rhombus=False
            for i in range(1,6):
                colregim[i]=(255,255,255)
            colregim[1]=(120,120,120)
        if mouse_button[0] and pos[0]>417 and pos[1]>10 and pos[0]<472 and pos[1]<60:
            draw=False
            drawing = False
            square=True
            rtriangle=False
            etriangle=False
            rhombus=False
            for i in range(1,6):
                colregim[i]=(255,255,255)
            colregim[2]=(120,120,120)
        if mouse_button[0] and pos[0]>482 and pos[1]>10 and pos[0]<537 and pos[1]<60:
            draw=False
            drawing = False
            square=False
            rtriangle=True
            etriangle=False
            rhombus=False
            for i in range(1,6):
                colregim[i]=(255,255,255)
            colregim[3]=(120,120,120)
        if mouse_button[0] and pos[0]>547 and pos[1]>10 and pos[0]<602 and pos[1]<60:
            draw=False
            drawing = False
            square=False
            rtriangle=False
            etriangle=True
            rhombus=False
            for i in range(1,6):
                colregim[i]=(255,255,255)
            colregim[4]=(120,120,120)
        if mouse_button[0] and pos[0]>612 and pos[1]>10 and pos[0]<667 and pos[1]<60:
            draw=False
            drawing = False
            square=False    
            rtriangle=False
            etriangle=False
            rhombus=True
            for i in range(1,6):
                colregim[i]=(255,255,255)
            colregim[5]=(120,120,120)
        #Changing draw color
        if mouse_button[0] and pos[0]>10 and pos[0]<257 and pos[1]>10 and pos[1]<20:
            color=(color[0],color[1],pos[0])
            colregim[0]=color
        if mouse_button[0] and pos[0]>10 and pos[0]<257 and pos[1]>30 and pos[1]<40:
            color=(color[0],pos[0],color[2])
            colregim[0]=color
        if mouse_button[0] and pos[0]>10 and pos[0]<257 and pos[1]>50 and pos[1]<60:
            color=(pos[0],color[1],color[2])
            colregim[0]=color

        pygame.display.flip()
        clock.tick(FPS)
main()
