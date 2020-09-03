from tkinter import *   
from PIL import ImageTk,Image
top = Tk()  
  
top.geometry("760x1560")  

#creating a simple canvas  
c = Canvas(top,bg = "brown",height = "760",width = 1560)  

photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\boh.PNG')

c.create_image(0,0, image= photo, anchor = NW)

def about():
    messagebox.showinfo("About the game?", "* About the game: This is a Harry Potter trivia game, in which you help harry destroy the horcruxes and finally Voldemort by giving the correct answers. May the nerdvana knowledge be with you :)")

def Rules():
    messagebox.showinfo("Rules of the game:", "* A total of 18 questions available to finish the game. \n\n One horcrux will get destroyed with every 2 correct answers.\n\n After the first 14 questions which will help in destroying the horcruxes will be 4 more questions to finally kill Voldemort.\n\n Even one wrong answer will kill harry and the game will be over.")    
    
def open():
    global c
    global photo
    top= Toplevel()
    top.title('Start game')
    c = Canvas(top,bg = "dark green",height = "760",width = 1560)  
    
    def Nextquestion():
        global c
        global photo
        top= Toplevel()
        top.title('2nd question')
        c = Canvas(top,bg = "dark green",height = "760",width = 1560)
        
        Label(top, text = 'Which creatures pull the carriages \n\n  that take students from the Hogwarts \n\n Express to the Castle?',fg = "white",bg = "black",font =('Algerian', 20)).place(x = 500,y = 140)
        bluebutton = Button(top, text = "Hippogriffs",command = Gameover, fg = "black", height = "1",width = 30 ).place(x = 656,y = 370)
        bluebutton = Button(top, text = "Centaurs",command = Gameover, fg = "black", height = "1",width = 30 ).place(x = 656,y = 430)
        bluebutton = Button(top, text = "Thestrals",command= Horcrux1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 490)
        bluebutton = Button(top, text = "Manticores",command = Gameover, fg = "black", height = "1",width = 30 ).place(x = 656,y = 550)
        
        photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\horcrux1.png')
        c.create_image(200,250, image= photo, anchor = NW)
        c.pack()
        
    def Horcrux1():
        global c
        global photo
        top= Toplevel()
        top.title('2nd question')
        c = Canvas(top,bg = "dark green",height = "760",width = 1560)
        Label(top, text = 'CONGRATULATIONS!!\n\n YOU HAVE SUCCESSFULLY DESTROYED THE FIRST HORCRUX!!',fg = "White",bg = "black",font =('Algerian', 20)).place(x = 400,y = 500)
        bluebutton = Button(top, text = "Continue",command= secondhorcrux, fg = "black", height = "2",width = 30 ).place(x = 656,y = 650)
        photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\killhorcrux1.png')
        c.create_image(200,0, image= photo, anchor = NW)
        c.pack()
    
    def secondhorcrux():
        global c
        global photo
        top= Toplevel()
        top.title('3rd question')
        c = Canvas(top,bg = "Yellow",height = "760",width = 1560)
        Label(top, text = "What is the name of the room Harry uses to teach Dumbledore's Army?",fg = "white",bg = "black",font =('Algerian', 20)).place(x = 350,y = 140)
        Label(top, text = 'Score: 1\n\n You have destroyed the first horcrux',fg = "black",font =('Algerian', 15)).place(x = 0,y = 0)
        bluebutton = Button(top, text = "The restricted section of the library",command = Gameover1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 270)
        bluebutton = Button(top, text = "The girls bathroom on the first floor",command = Gameover1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 330)
        bluebutton = Button(top, text = "The prefect's bathroom",command= Gameover1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 390)
        bluebutton = Button(top, text = "The room of requirement",command = secondhorcrux2, fg = "black", height = "1",width = 30 ).place(x = 656,y = 450)
        photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\horcrux2.png')
        c.create_image(200,250, image= photo, anchor = NW)
        c.pack()
        
    def secondhorcrux2():
        global c
        global photo
        top= Toplevel()
        top.title('4th question')
        c = Canvas(top,bg = "Yellow",height = "760",width = 1560)
        Label(top, text = "Who was the headmaster of Hogwarts\n\n when the Chamber of Secrets was\n\n opened for the first time?",fg = "white",bg = "black",font =('Algerian', 20)).place(x = 480,y = 80)
        Label(top, text = 'Score: 1\n\n You have destroyed the first horcrux',fg = "black",font =('Algerian', 15)).place(x = 0,y = 0)
        bluebutton = Button(top, text = "Armando Dippet",command = Horcrux2, fg = "black", height = "1",width = 30 ).place(x = 656,y = 270)
        bluebutton = Button(top, text = "Albus Dumbledore",command = Gameover1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 330)
        bluebutton = Button(top, text = "Phineus Nigellus Black",command= Gameover1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 390)
        bluebutton = Button(top, text = "Brutus Scrimgeour",command = Gameover1, fg = "black", height = "1",width = 30 ).place(x = 656,y = 450)
        photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\horcrux2.png')
        c.create_image(200,250, image= photo, anchor = NW)
        c.pack()
        
    def Horcrux2():
        global c
        global photo
        top= Toplevel()
        top.title('Continue')
        c = Canvas(top,bg = "dark green",height = "760",width = 1560)
        Label(top, text = 'CONGRATULATIONS!!\n\n YOU HAVE SUCCESSFULLY DESTROYED THE SECOND HORCRUX!!',fg = "White",bg = "black",font =('Algerian', 20)).place(x = 400,y = 550)
        bluebutton = Button(top, text = "Continue",command= secondhorcrux, fg = "black", height = "2",width = 30 ).place(x = 656,y = 700)
        photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\killhorcrux2.png')
        c.create_image(120,0, image= photo, anchor = NW)
        c.pack()
        
    def Gameover1():
        global c
        top= Toplevel()
        top.title('Game over')
        c = Canvas(top,bg = "Red",height = "760",width = 1560) 
        Label(top, text = 'GAME OVER!',fg = "red",bg = "black",font =('Algerian', 20)).place(x = 650,y = 350)
        Label(top, text = 'As per the rules you lose the game, i.e harry dies if your answer is wrong',fg = "black",font =('Algerian', 20)).place(x = 260,y = 450)
        Label(top, text = 'Better luck next time :)',fg = "black",font =('Algerian', 20)).place(x = 580,y = 480)
        Label(top, text = 'Score: 1\n\n you lost after destroying the first horcrux',fg = "black",font =('Algerian', 15)).place(x = 0,y = 0)
        
        c.pack()
        
    
    def Gameover():
        global c
        top= Toplevel()
        top.title('Game over')
        c = Canvas(top,bg = "Red",height = "760",width = 1560) 
        Label(top, text = 'GAME OVER!',fg = "red",bg = "black",font =('Algerian', 20)).place(x = 650,y = 350)
        Label(top, text = 'As per the rules you lose the game, i.e harry dies if your answer is wrong',fg = "black",font =('Algerian', 20)).place(x = 260,y = 450)

        
        c.pack()
    
    Label(top, text = 'What is the name of the book \n\n Hermione supposes Voldemort used \n\n to learn about Horcruxes?',fg = "white",bg = "black",font =('Algerian', 20)).place(x = 500,y = 140)
    bluebutton = Button(top, text = "Magik moste evil",command = Gameover, fg = "black", height = "1",width = 30 ).place(x = 656,y = 370)
    bluebutton = Button(top, text = "Secrets of the darkest art",command = Nextquestion, fg = "black", height = "1",width = 30 ).place(x = 656,y = 430)
    bluebutton = Button(top, text = "Moste potente potions",command = Gameover, fg = "black", height = "1",width = 30 ).place(x = 656,y = 490)
    
    photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\horcrux1.png')
    c.create_image(200,250, image= photo, anchor = NW)
    c.pack() 
    

bluebutton = Button(top, text = "Rules",command = Rules,fg = "black", height = "1",width = 30 ).place(x = 656,y = 450)
bluebutton = Button(top, text = "Start Game",command = open,fg = "black", height = "1",width = 30 ).place(x = 656,y = 520)
#bluebutton = Button(top, text = "Multi Player",fg = "black", height = "1",width = 30 ).place(x = 656,y = 520)

bluebutton = Button(top, text = "Share",fg = "black", height = "1",width = 5 ).place(x = 656,y = 640)

bluebutton = Button(top, text = "About",command = about,fg = "black", height = "1",width = 5 ).place(x = 738,y = 640)

bluebutton = Button(top, text = "Settings",fg = "black", height = "1",width = 5 ).place(x = 832,y = 640)

Label(top, text = 'The quest for horcruxes',fg = "white",bg = "black",font =( 
  'Algerian', 20)).place(x = 590,y = 200)

c.pack()  
  
mainloop()
