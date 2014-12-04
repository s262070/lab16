# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.destroy(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket = drawpad.create_rectangle(395,585,400,590)
direction = 5
r1fired = False
class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        #yolo swaggins and the quest for dank weed
        
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global r1fired
        global rocket
        px1,py1,px2,py2 = drawpad.coords(player)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy)
        rx1, ry1, rx2, ry2 = drawpad.coords(rocket)
        x = px1 - rx1
        y = py1 - ry1
        if ex2 > 800:
            direction = - 5
        elif ex1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        if r1fired == True:
            drawpad.move(rocket,0,-1)
            self.collisionDetect()
        if ry1 < 0:
            drawpad.move(rocket,x,y)
            r1fired = False
        drawpad.after(1,self.animate)

    def key(self,event):
        global player
        global r1fired
        global rocket
        x1,y1,x2,y2 = drawpad.coords(player)
        rx1,ry1,rx2,ry1 =drawpad.coords(rocket)
        
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-10)
                drawpad.move(rocket,0,-10)
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,10)
                drawpad.move(rocket,0,10)
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-10,0)
                drawpad.move(rocket,-10,0)
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,10,0)
                drawpad.move(rocket,10,0)
        if event.char == " ":
            r1fired = True
            if self.rockets > 0:
                self.rockets = self.rockets - 1
                self.rocketsTxt.configure(text = self.rockets)
            
                
                    
    def collisionDetect(self):
        global player
        global enemy
        global rocket
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        ex1, ey1, ex2, ey2 = drawpad.coords(enemy)
        print "debug"
        if (rx1 > ex1 and rx2 < ex2) and (ry1 > ey1 and ry2 < ey2):
            print "true"
            drawpad.delete(enemy)
app = myApp(root)
root.mainloop()