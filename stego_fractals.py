from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from random import randint
from random import seed
import sys,time
window = 0                                             
width, height = 1000, 800  
b_size=1000                             
class Tree:
    def __init__(self,tree_depth):
        self.branch_vertices=[]
        self.resize_ratio=0.40
        self.angle_reduction_ratio=0.75
        self.start_angle=55
        self.end_angle=75
        self.dex=0
        self.delta=2 #change in angle
        self.sigma=3 # change in arm length
        self.bits_capacity=1000
        seed()
        self.data=[randint(0,1) for b in range(1,self.bits_capacity+1)]
        print(self.data)
    def calc_vertices(self,point,source_direction,lth,depth,b_angle):
        #b_angle=randint(self.start_angle,self.end_angle)
        if self.data[self.dex] == 0:
            b_angle += self.delta
        else:
            b_angle -= self.delta
        self.dex += 1
        leftb_Larm_lth=leftb_Rarm_lth=rightb_Larm_lth=rightb_Rarm_lth=lth
        #if self.dex < len(self.data):
        '''if self.data[self.dex] == 0:
            #left > right
            seed()
            leftb_Larm_lth= lth/2 + randint(0,lth//self.sigma)
        else:
            seed()
            leftb_Rarm_lth= lth/2 + randint(0,lth//self.sigma)
        self.dex += 1
        '''
        point=np.array(point)
        #left branch
        left_branch_direction=self.norma(self.get_rotated_vec(source_direction,b_angle))
        leftb_center_point=point + lth*left_branch_direction
        leftb_Larm_direction=self.get_rotated_vec(left_branch_direction,b_angle*self.angle_reduction_ratio)
        self.branch_vertices.append([point,leftb_center_point])
        leftb_Larm_point=leftb_center_point + leftb_Larm_lth*leftb_Larm_direction
        self.branch_vertices.append([leftb_center_point,leftb_Larm_point])
        leftb_Rarm_direction=self.get_rotated_vec(left_branch_direction,-b_angle*self.angle_reduction_ratio)
        leftb_Rarm_point=leftb_center_point +leftb_Rarm_lth*leftb_Rarm_direction
        self.branch_vertices.append([leftb_center_point,leftb_Rarm_point])
        '''if self.data[self.dex] == 0:
            #left > right
            seed()
            rightb_Larm_lth= lth/2 + randint(0,lth//self.sigma)
        else:
            seed()
            rightb_Rarm_lth= lth/2 + randint(0,lth//self.sigma)
        '''
         #right branch
        right_branch_direction=self.norma(self.get_rotated_vec(source_direction,-b_angle))
        rightb_center_point=point + lth*right_branch_direction
        rightb_Larm_direction=self.get_rotated_vec(right_branch_direction,b_angle*self.angle_reduction_ratio)
        self.branch_vertices.append([point,rightb_center_point])
        rightb_Larm_point=rightb_center_point + rightb_Larm_lth*rightb_Larm_direction
        self.branch_vertices.append([rightb_center_point,rightb_Larm_point])
        rightb_Rarm_direction=self.get_rotated_vec(right_branch_direction,-b_angle*self.angle_reduction_ratio)
        rightb_Rarm_point=rightb_center_point + rightb_Rarm_lth*rightb_Rarm_direction
        self.branch_vertices.append([rightb_center_point,rightb_Rarm_point])
        #remove what you have added
        if self.data[self.dex] == 0:
            b_angle -= self.delta
        else:
            b_angle += self.delta
        if depth > 1:
            self.calc_vertices(leftb_Larm_point,leftb_Larm_direction,lth*self.resize_ratio,depth-1,b_angle*self.angle_reduction_ratio)
            self.calc_vertices(leftb_Rarm_point,leftb_Rarm_direction,lth*self.resize_ratio,depth-1,b_angle*self.angle_reduction_ratio)
            self.calc_vertices(rightb_Larm_point,rightb_Larm_direction,lth*self.resize_ratio,depth-1,b_angle*self.angle_reduction_ratio)
            self.calc_vertices(rightb_Rarm_point,rightb_Rarm_direction,lth*self.resize_ratio,depth-1,b_angle*self.angle_reduction_ratio)


    def get_rotated_vec(self,vect,angle):
        theta = np.radians(angle)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array([[c, -s], [s, c]]) # compose the rotation matrix
        #print(R)
        a = np.array(vect)# create object to get it transposed
        return R.dot(a)
    def norma(self,vect): # normalize a vector
        return vect/np.linalg.norm(vect)

def draw_lines(x1, y1, x2, y2):
    glBegin(GL_LINES)  
    glVertex2f(0,0)                                   # bottom left point                 # top right point
    glVertex2f(0,height/3)                                 # start drawing a rectangle
    j=0
    for line in branch.branch_vertices:
        if(j<b_size):
            glVertex2f(line[0][0], line[0][1])                                   # bottom left point                 # top right point
            glVertex2f(line[1][0], line[1][1])  
            j+=1                    
    glEnd()                                            # done drawing a rectangle

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(1.0,1.0,1.0,1.0)

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    glTranslated(width/2,0,0)
    glColor3f(0.0, 0.0, 0.0)                           # set color to blue
    glLineWidth(2)
    draw_lines(0, 0, 200, 100)   
    glutSwapBuffers()                                  # important for double buffering
def keyPressed(bkey, x, y):
    global b_size
    # Convert bytes object to string 
    key = bkey.decode("utf-8")
    # Allow to quit by pressing 'Esc' or 'q'
    if key == chr(27):
        sys.exit()
    if key == 'q':
        b_size += 1

# initialization
tree_depth=4
branch=Tree(tree_depth)
print("program started, we will calculate vertices")
branch.calc_vertices([0,height/3],[0,2],150,tree_depth,45)

glutInit(sys.argv)                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"Steganography Fractals")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)   
#glutKeyboardFunc(keyPressed)                                  # draw all the time
glutMainLoop()