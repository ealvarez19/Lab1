#CS2302
#Author: Emmanuel Alvarez 80567137
#Lab1
# Instructor: Olac Fuentes
# Last modification date: 02-10-2019
# The purpose of this program is to practice how to code figures using 
#matplotlib.pyplot library.
import numpy as np
import matplotlib.pyplot as plt
import math
#############################################################################
# The following code draws the first exercise
def draw_squares(ax,n,p,size):
    if n>0:
       
        q = np.array([[p[1,0],p[1,1]], # Draws the lower left corner square in each recursion call
                     [p[1,0] - size//2,p[1,1] - size//2],
                     [p[1,0] - size//2,p[1,1] + size//2],
                     [p[1,0] + size//2,p[1,1] + size//2],
                     [p[1,0] + size//2,p[1,1] - size//2],
                     [p[1,0] - size//2,p[1,1] - size//2]])
        ax.plot(q[1:,0],q[1:,1],color='b')
        draw_squares(ax,n-1,q,size//2)
        
        q2 = np.array([[p[2,0],p[2,1]], #Draws the left upper corner square in each recursion call
                     [p[2,0] - size//2,p[2,1] - size//2],
                     [p[2,0] - size//2,p[2,1] + size//2],
                     [p[2,0] + size//2,p[2,1] + size//2],
                     [p[2,0] + size//2,p[2,1] - size//2],
                     [p[2,0] - size//2,p[2,1] - size//2]])
        ax.plot(q2[1:,0],q2[1:,1],color='b')
        draw_squares(ax,n-1,q2,size//2)
        
        q3 = np.array([[p[3,0],p[3,1]], #Draws the right upper corner square in each recursion call
                     [p[3,0] - size//2,p[3,1] - size//2],
                     [p[3,0] - size//2,p[3,1] + size//2],
                     [p[3,0] + size//2,p[3,1] + size//2],
                     [p[3,0] + size//2,p[3,1] - size//2],
                     [p[3,0] - size//2,p[3,1] - size//2]])
        ax.plot(q3[1:,0],q3[1:,1],color='b')
        draw_squares(ax,n-1,q3,size//2)
        
        q4 = np.array([[p[4,0],p[4,1]], # Draws the lower right corner square in each recursion call
                     [p[4,0] - size//2,p[4,1] - size//2],
                     [p[4,0] - size//2,p[4,1] + size//2],
                     [p[4,0] + size//2,p[4,1] + size//2],
                     [p[4,0] + size//2,p[4,1] - size//2],
                     [p[4,0] - size//2,p[4,1] - size//2]])
        ax.plot(q4[1:,0],q4[1:,1],color='b')
        draw_squares(ax,n-1,q4,size//2)       
        
        ax.plot(p[1:,0],p[1:,1],color='b') #Draws the biggest square
        draw_squares(ax,n-1,q,size//2)
        
        

#plt.close("all") 
orig_size = 50
p = np.array([[0,0],[-50,-50],[-50,50],[50,50],[50,-50],[-50,-50]]) #Biggest square coordinates
fig, ax = plt.subplots()
draw_squares(ax,3,p,orig_size)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squares.png')

##############################################################################
#The following code draws the second exercise
def circle(center,rad):
        n = int(4*rad*math.pi)
        t = np.linspace(0,6.3,n)
        x = center[0]+rad*np.sin(t)
        y = center[1]+rad*np.cos(t)
        return x,y
    
def draw_circles(ax,n,center,radius):
        if n>0:
            x,y = circle(center,radius)
            ax.plot(x,y,color='k')
            oldCenter = center[0] # Saves the current center coordinates
            center [0] = center[0]*1.1 # Moves the circle to the right on the x-axis
            newCenter = center[0] - oldCenter #Saves the new center coordinates
            radius = radius + newCenter # New radius value in order to cross with the previus circles
            
            draw_circles(ax,n-1,center,radius) #Recursion call with the new center and radius
          
#plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 40, [100,0], 2)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')

##############################################################################
#The following code draws the third exercise
def draw_binaryTree(root,depth,wide):
    if depth > 0: 
        left = np.array([root[0]-wide,root[1] - wide*2])# Takes the coordinates of the left sub-tree
        rigth = np.array([root[0]+wide,root[1]-wide*2]) # Takes the coordinates of the right sub-tree
        #print('root',root)
        #print('left',left)
        #print('rigth', rigth)
       #print('----------------')
        ax.plot([root[0], left[0]],[root[1], left [1]],color='r')
        ax.plot([root[0], rigth[0]],[root[1], rigth [1]],color='r')
        draw_binaryTree(left,depth-1,wide/2)
        draw_binaryTree(rigth,depth-1,wide/2)    
#plt.close("all")
fig, ax = plt.subplots()
root = np.array([0,0])#Root coordinates
wide = 10#
draw_binaryTree(root,6,1000)
ax.set_aspect(1.0)
plt.show()
fig.savefig('binaryTree')
##############################################################################
#The following code draws the fourth exercise
def draw_sixCircles(n,center,radius):
    if(n>0):
        x,y = circle(center,radius) #Biggest Circle
        ax.plot(x,y,color='k')        
    
        x,y = circle(center,radius//3) # Circle in the middle
        ax.plot(x,y,color='k')
        
        left = np.array([center[0]-((radius//3)*2),center[1]])#Takes the coordinates of the left circle
        x,y = circle(left,radius//3)
        ax.plot(x,y,color='k')
        
        rigth = np.array([center[0]+((radius//3)*2),center[1]])#takes the coordinates of the right circle
        x,y = circle(rigth,radius//3)
        ax.plot(x,y,color='k')
        
        upper = np.array([center[0],center[1]+((radius//3)*2)])#takes the coordinates of the upper circle
        x,y = circle(upper,radius//3)
        ax.plot(x,y,color='k')
        
        lower = np.array([center[0],center[1]-((radius//3)*2)])#takes the coordinates of the lower circle
        x,y = circle(lower,radius//3)
        ax.plot(x,y,color='k')

        draw_sixCircles(n-1,left,radius//3)#Draws the left circle on each recursive call
        draw_sixCircles(n-1,rigth,radius//3)#Draws the right circle on each recursive call
        draw_sixCircles(n-1,center,radius//3)#Draws the middle circle on each recursive call
        draw_sixCircles(n-1,upper,radius//3)#Draws the upper circle on each recursive call
        draw_sixCircles(n-1,lower,radius//3)#Draws the lower circle on each recursive call
    
#plt.close("all")
fig, ax = plt.subplots()
center = np.array([0,0])
radius = 1000 
draw_sixCircles(4,center,radius)
ax.set_aspect(1.0)
plt.show()
fig.savefig('sixCircles')
    
    






